# ScufitaAlbastra

Două skill-uri pentru design și editare în Photoshop prin MCP:

- **`scufita-albastra`**: compoziție, direcție vizuală, imagini generate când ajută, verificare vizuală și livrare PSD editabil.
- **`photoshop-mcp-techniques`**: biblioteca Adobe și alegerea tehnicilor potrivite pentru selecții, măști, layere, culoare, retuș, compoziție, text, Smart Objects, funcții generative și export.

Pachetul conține instrucțiuni, fișe și scripturi. Nu include Photoshop, conturi, autentificări, credite, conversații sau proiecte personale.

## Instalare

Ai nevoie de Codex, Python 3.10+ și, pentru execuție, Photoshop desktop pe macOS sau Windows și Node.js 18+.

1. Descarcă repository-ul prin **Code → Download ZIP** și dezarhivează-l, sau copiază URL-ul său din GitHub și folosește `git clone`.
2. Deschide terminalul în folderul descărcat.
3. Verifică planul, apoi instalează ambele skill-uri:

```bash
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

Pe Windows poți folosi `py -3` în loc de `python3`.

Instalatorul folosește implicit `~/.codex/skills`, pentru gazdele compatibile cu această locație. Documentația Codex actuală indică `~/.agents/skills`; poți selecta explicit această destinație:

```bash
python3 scripts/install.py --skills-dir "~/.agents/skills"
```

Alege o singură locație descoperită de versiunea ta de Codex, ca să eviți apariția dublă a acelorași skill-uri. Instalatorul copiază cele două directoare alăturat, astfel încât legăturile dintre ele să funcționeze. Nu modifică setările MCP sau conturile. Dacă există deja, le păstrează; `--replace` creează copii de siguranță înainte de înlocuire, într-un director `skills-backups` alăturat celui de instalare, în afara locației scanate pentru skill-uri.

Deschide o conversație nouă după instalare; dacă skill-urile nu apar, repornește aplicația. Vezi [documentația oficială pentru skill-uri](https://learn.chatgpt.com/docs/build-skills).

## Conectarea Photoshop

Folosește propriul Photoshop instalat și pornește aplicația. Serverul compatibil este [photoshop-mcp](https://github.com/alisaitteke/photoshop-mcp), instalat separat. Exemplu pentru Codex CLI:

```bash
codex mcp add photoshop --env ANALYTICS_DISABLED=1 --env PSMCP_FEEDBACK=0 --env PSMCP_UPDATE_CHECK=0 -- npx -y @alisaitteke/photoshop-mcp@1.7.37
```

Comanda înregistrează serverul în propriul Codex; `npx` descarcă pachetul la utilizare. Verifică documentația serverului pentru permisiunile de automatizare ale sistemului. Dacă ai deja un server `photoshop` funcțional, păstrează configurarea existentă. Pentru clienții care folosesc configurație JSON, [mcp.example.json](mcp.example.json) este un exemplu fără căi specifice unui calculator.

Într-o cerere Photoshop, agentul verifică legătura, instrumentele disponibile, versiunea și documentul vizat înainte să editeze. Biblioteca nu garantează disponibilitatea unei funcții doar din numele ei.

## Utilizare

Poți cere explicit:

```text
Folosește $scufita-albastra pentru un afiș în Photoshop, cu text editabil și PSD final pe layere.
```

Pentru o operație simplă:

```text
Folosește $photoshop-mcp-techniques și redimensionează imaginea la 1200 × 800 px.
```

Redimensionarea nu declanșează automat retuș, efecte sau generare. Pentru lucrările creative, imaginile, textul, măștile și ajustările se păstrează editabile unde instrumentele permit, iar livrarea trebuie verificată vizual și structural în fișierul salvat.

## Generare opțională

Rutarea include profiluri pentru GPT Image 2.6 Sunburst, Nano Banana 2.1 și Flare, prin Higgsfield atunci când conectorul și modelele sunt disponibile în contul tău. Descoperirea lor se verifică la utilizare. Folosește propriile conturi și credite; accesul altui utilizator nu se transferă prin acest repository. Poate fi folosită și generarea nativă oferită de gazdă, când este disponibilă și potrivită cererii.

Qwen, Ming și Ideogram sunt opțiuni de cercetare, nu integrări incluse. Instalarea nu pornește generări și nu activează abonamente.

## Biblioteca și limitele ei

[Indexul tehnicilor](photoshop-mcp-techniques/references/index.md) acoperă 20 de fișe fundamentale, cu surse [Adobe Learn](https://www.adobe.com/uk/learn/photoshop), condiții, parametri și verificări. Catalogul Adobe nu este parcurs integral; progresul și materialele restante sunt păstrate separat.

Fișele disting documentarea Adobe, suportul MCP inspectat și verificările istorice ale unor componente. Dovezile locale și imaginile de probă ale autorului nu sunt distribuite. Aceste rezultate istorice nu certifică instalarea ta; testează tehnicile noi pe copii și verifică vizual rezultatul. Generările plătite nu sunt declarate testate de acest pachet.

Regulile și limitele tehnice, inclusiv operațiile care pot rasteriza Smart Objects sau afecta o mască existentă, rămân în [referința de compatibilitate](photoshop-mcp-techniques/references/compatibility.md). Atribuirile pentru componentele terțe sunt în [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Pentru verificarea instalatorului, fără Photoshop sau modificarea directoarelor personale:

```bash
python3 -m unittest discover -s tests -v
```
