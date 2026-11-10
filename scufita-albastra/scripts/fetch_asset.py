"""Fetch an authorized completed image result for local Photoshop import."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


MIMES = {"image/png": {".png"}, "image/jpeg": {".jpg", ".jpeg"}, "image/webp": {".webp"}}
DEFAULT_ROOT = Path.cwd()


def checked_url(value):
    parts = urlsplit(value)
    if parts.scheme.lower() != "https" or not parts.hostname or parts.username or parts.password:
        raise ValueError("Use an authorized HTTPS result URL without embedded credentials")
    return parts


class HTTPSRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, newurl):
        checked_url(newurl)
        return super().redirect_request(request, response, code, message, headers, newurl)


def inspect_image(path, mime, max_pixels):
    with path.open("rb") as stream:
        head = stream.read(16)
    actual = None
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        actual = "image/png"
    elif head.startswith(b"\xff\xd8\xff"):
        actual = "image/jpeg"
    elif head.startswith(b"RIFF") and head[8:12] == b"WEBP":
        actual = "image/webp"
    if actual != mime:
        raise ValueError("Response MIME and image signature do not agree")
    try:
        from PIL import Image
    except ImportError:
        decoder = shutil.which("sips")
        if not decoder:
            raise ValueError("Image decoding needs Pillow or the macOS sips utility")
        result = subprocess.run([decoder, "-g", "pixelWidth", "-g", "pixelHeight", str(path)], capture_output=True, text=True, timeout=30)
        width = re.search(r"pixelWidth:\s*(\d+)", result.stdout)
        height = re.search(r"pixelHeight:\s*(\d+)", result.stdout)
        if result.returncode or not width or not height:
            raise ValueError("The system image decoder rejected the downloaded file")
        width, height = int(width.group(1)), int(height.group(1))
        if width <= 0 or height <= 0 or width * height > max_pixels:
            raise ValueError("Invalid image dimensions or configured pixel limit exceeded")
        with tempfile.TemporaryDirectory(dir=path.parent) as decode_dir:
            decoded_path = Path(decode_dir) / "decoded.png"
            result = subprocess.run([decoder, "-s", "format", "png", str(path), "--out", str(decoded_path)], capture_output=True, text=True, timeout=30)
            if result.returncode or not decoded_path.is_file() or decoded_path.stat().st_size == 0:
                raise ValueError("The system image decoder rejected the downloaded pixels")
        method = "macOS sips dimension probe and PNG decode"
    else:
        with Image.open(path) as decoded:
            width, height = decoded.size
            if width * height > max_pixels:
                raise ValueError("Image exceeds the configured pixel limit")
            decoded.verify()
        with Image.open(path) as decoded:
            decoded.load()
        method = "Pillow verify and load"
    if width <= 0 or height <= 0 or width * height > max_pixels:
        raise ValueError("Invalid image dimensions or configured pixel limit exceeded")
    return width, height, method


def fetch_asset(url, destination, root=DEFAULT_ROOT, max_bytes=100 * 1024 * 1024, max_pixels=100_000_000, opener=None):
    parts = checked_url(url)
    root = Path(root).resolve()
    destination = Path(destination).expanduser().resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        raise ValueError("Destination must be inside the explicitly selected workspace root")
    if not destination.parent.is_dir() or destination.exists():
        raise ValueError("Use an existing authorized parent directory and a new destination filename")
    opener = opener or build_opener(HTTPSRedirects())
    temporary = None
    try:
        request = Request(url, headers={"User-Agent": "ScufitaAlbastra-AssetImport/1.0", "Accept": "image/png,image/jpeg,image/webp"})
        with opener.open(request, timeout=60) as response:
            checked_url(response.geturl())
            if response.status != 200:
                raise ValueError("Provider did not return HTTP 200")
            mime = response.headers.get_content_type()
            if mime not in MIMES or destination.suffix.lower() not in MIMES[mime]:
                raise ValueError("Use PNG, JPEG or WebP with an extension matching the response MIME")
            length = response.headers.get("Content-Length")
            if length and int(length) > max_bytes:
                raise ValueError("Response exceeds the configured byte limit")
            size, digest = 0, hashlib.sha256()
            with tempfile.NamedTemporaryFile(dir=destination.parent, suffix=destination.suffix, delete=False) as output:
                temporary = Path(output.name)
                while True:
                    block = response.read(65536)
                    if not block:
                        break
                    size += len(block)
                    if size > max_bytes:
                        raise ValueError("Response exceeds the configured byte limit")
                    digest.update(block)
                    output.write(block)
            if not size or (length and size != int(length)):
                raise ValueError("Empty or truncated response")
        width, height, decoder = inspect_image(temporary, mime, max_pixels)
        os.link(temporary, destination)  # Exclusive creation: never replace an existing asset.
        return {
            "ok": True, "path": str(destination), "source_url": urlunsplit((parts.scheme, parts.netloc, parts.path, "", "")),
            "signed_query_omitted": bool(parts.query), "mime": mime, "bytes": size,
            "width_px": width, "height_px": height, "sha256": digest.hexdigest(), "decoder": decoder,
            "limits": "Local transfer/decode evidence only; inspect visual quality, transparency and provider provenance separately."
        }
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Actual completed authorized HTTPS provider result URL")
    parser.add_argument("destination", type=Path, help="New absolute local image path")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Explicitly authorized destination workspace")
    parser.add_argument("--max-bytes", type=int, default=100 * 1024 * 1024)
    parser.add_argument("--max-pixels", type=int, default=100_000_000)
    args = parser.parse_args()
    try:
        if args.max_bytes <= 0 or args.max_pixels <= 0:
            raise ValueError("Limits must be positive")
        print(json.dumps(fetch_asset(args.url, args.destination, args.root, args.max_bytes, args.max_pixels)))
    except Exception as error:
        # Do not echo signed URL queries, tokens or response bodies into logs.
        message = str(error) if isinstance(error, ValueError) else "Asset import failed: " + type(error).__name__
        print(json.dumps({"ok": False, "error": message}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
