#!/usr/bin/env python3
"""Read-only upstream HEAD comparison; does not alter installed skills or Git refs."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / 'skills-lock.json').read_text())
for name, item in lock['skills'].items():
    try:
        result = subprocess.run(['git', 'ls-remote', item['repository'] + '.git', 'HEAD'], capture_output=True, text=True, timeout=30, check=True)
        sha = result.stdout.split()[0]
        print(f'{name}: installed={item["commit"]} upstream={sha} ' + ('same' if sha == item['commit'] else 'different; review before upgrading'))
    except (subprocess.SubprocessError, OSError, IndexError) as error:
        print(f'{name}: upstream check unavailable ({type(error).__name__}); keep installed version')
