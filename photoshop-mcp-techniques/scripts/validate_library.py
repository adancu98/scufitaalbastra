"""Validate the portable library without private local fixtures or account access."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

parser = argparse.ArgumentParser()
parser.add_argument('--expect-cards', type=int)
parser.add_argument('--tools', type=Path, help='Optional fresh MCP tools/list JSON; otherwise use the bundled interface snapshot')
args = parser.parse_args()
skill = Path(__file__).resolve().parents[1]
ref = skill / 'references'
catalog = json.loads((ref / 'catalog.json').read_text())
if args.tools:
    discovery = json.loads(args.tools.read_text())
    names = {t['name'] for t in discovery['tools']}
else:
    names = set(json.loads((ref / 'server-inventory.json').read_text())['tool_names'])
cards = catalog['cards']
errors = []
if args.expect_cards is not None and len(cards) != args.expect_cards:errors.append('Unexpected card count')
if len({c['id'] for c in cards}) != len(cards):errors.append('Duplicate card ids')
required = ['id','title','theme','problem','when_to_use','avoid','preconditions','limits','essential_steps','adapt_parameters','visual_check','adobe_evidence','mcp','runtime']
for c in cards:
    for key in required:
        if not c.get(key):errors.append(c['id'] + ': missing ' + key)
    host = urlparse(c['adobe_evidence']['url']).hostname or ''
    if not(host == 'adobe.com' or host.endswith('.adobe.com')):errors.append('Non-Adobe primary source: ' + c['id'])
    for name in c['mcp'].get('tools', []):
        if name not in names:errors.append('Tool not advertised in selected schema: ' + name)
    if c['runtime']['status'] == 'historical_report_not_reproduced_here':
        if not c['runtime'].get('limits') or not c['runtime'].get('reported_status'):errors.append('Unbounded historical report: ' + c['id'])
    elif c['runtime']['status'] != 'not_run':
        log = c['runtime'].get('raw_log')
        if not log or not Path(log).is_file():errors.append('Missing new runtime evidence: ' + c['id'])
    if not(ref / 'cards' / (c['id'] + '.md')).is_file():errors.append('Missing card: ' + c['id'])
for folder in [skill, skill.parent / 'scufita-albastra']:
    for path in folder.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#') and not(path.parent / target.split('#')[0]).exists():errors.append('Broken relative link: ' + str(path.relative_to(skill.parent)) + ' -> ' + target)
progress = json.loads((ref / 'progress.json').read_text())
if progress['catalog_complete'] is not False:errors.append('Initial distribution must not claim whole-catalog coverage')
records = [json.loads(line) for line in (ref / 'experience.jsonl').read_text().splitlines() if line]
if any(v['card_id'] not in {c['id'] for c in cards} for v in records):errors.append('Unknown experience card')
print(json.dumps({'cards':len(cards),'themes':len({c['theme'] for c in cards}),'snapshot_tools':len(names),'live_schema_used':bool(args.tools),'historical_records':len(records),'errors':errors}))
raise SystemExit(bool(errors))
