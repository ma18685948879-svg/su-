#!/usr/bin/env python3
"""Check vendored source integrity, discoverable entries, resources, and runtime."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--runtime', action='store_true')
args = parser.parse_args()
lock = json.loads((ROOT / 'skills-lock.json').read_text())
errors = []
for name, item in lock['skills'].items():
    folder = ROOT / item['path']
    for rel in ('SKILL.md', 'SKILL.upstream.md', 'LICENSE', 'UPSTREAM.json', 'agents/openai.yaml', 'references', 'scripts', 'assets'):
        if not (folder / rel).exists():
            errors.append(f'{name}: missing {rel}')
    if (folder / '.git').exists():
        errors.append(f'{name}: nested Git repository must not be committed')
    front = (folder / 'SKILL.md').read_text().split('---', 2)
    if len(front) != 3 or not re.search(r'^name: ' + re.escape(name) + r'$', front[1], re.M) or not re.search(r'^description: .+', front[1], re.M):
        errors.append(f'{name}: invalid Skill metadata')
    if len(front) == 3 and set(re.findall(r'^([\w-]+):', front[1], re.M)) != {'name', 'description'}:
        errors.append(f'{name}: unexpected metadata keys')
    info = json.loads((folder / 'UPSTREAM.json').read_text())
    if info['commit'] != item['commit']:
        errors.append(f'{name}: version index differs from provenance')
    for rel, expected in info['copied_files_sha256'].items():
        file = folder / rel
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            errors.append(f'{name}: upstream source changed or missing: {rel}')
    print(f'{name}: verified {len(info["copied_files_sha256"])} upstream files at {info["commit"][:12]}')
    if args.runtime and name != 'industrial-design-portfolio':
        code = "import {readFileSync} from 'node:fs';const pkg=JSON.parse(readFileSync('package.json'));for(const p of Object.keys(pkg.dependencies||{}))await import(p);console.log('Node dependencies imported');"
        result = subprocess.run(['node', '--input-type=module', '-e', code], cwd=folder, capture_output=True, text=True)
        if result.returncode:
            errors.append(f'{name}: runtime dependencies unavailable; run scripts/setup_skills.py')
        else:
            print(f'{name}: {result.stdout.strip()}')
if args.runtime:
    folder = ROOT / '.agents/skills/industrial-design-portfolio'
    result = subprocess.run([sys.executable, str(folder / 'scripts/validate_layout_library.py')], capture_output=True, text=True)
    print(result.stdout.strip())
    if result.returncode:
        errors.append('industrial-design-portfolio: upstream layout library validation failed')
for error in errors:
    print('ERROR:', error, file=sys.stderr)
print(f'Installation check: {len(errors)} error(s). Browser launch and application rendering require separate checks.')
sys.exit(bool(errors))
