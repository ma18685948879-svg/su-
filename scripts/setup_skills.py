#!/usr/bin/env python3
"""Restore isolated dependencies in a fresh Codex checkout; never install globally."""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('folio', 'guizang-ppt-skill', 'industrial-design-portfolio')


def run(command, cwd):
    print('+', ' '.join(map(str, command)), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill', choices=NAMES, action='append')
    parser.add_argument('--skip-browser', action='store_true')
    parser.add_argument('--industrial-tests', action='store_true', help='Install optional upstream test dependencies into a local venv')
    args = parser.parse_args()
    names = args.skill or list(NAMES)
    for name in names:
        folder = ROOT / '.agents' / 'skills' / name
        if name == 'industrial-design-portfolio' and not args.industrial_tests:
            print(f'{name}: core validators use Python standard library; no package installation required.')
            continue
        npm = shutil.which('npm')
        if not npm:
            raise RuntimeError('npm is required. Use Node.js 20+ in the Codex environment.')
        run([npm, 'ci', '--ignore-scripts', '--no-audit', '--no-fund'], folder)
        if not args.skip_browser:
            cli = folder / 'node_modules' / ('@playwright/test/cli.js' if name == 'industrial-design-portfolio' else 'playwright/cli.js')
            run([shutil.which('node') or 'node', str(cli), 'install', 'chromium'], folder)
        if name == 'industrial-design-portfolio':
            venv = folder / '.venv'
            run([sys.executable, '-m', 'venv', str(venv)], folder)
            python = venv / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
            run([str(python), '-m', 'pip', 'install', '-r', str(folder / 'requirements-test.txt')], folder)
    run([sys.executable, str(ROOT / 'scripts/verify_skills.py'), '--runtime'], ROOT)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f'Setup failed: {error}', file=sys.stderr)
        sys.exit(1)
