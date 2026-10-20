#!/usr/bin/env python3
"""Copy this self-contained skill into a Codex or Claude Code skill directory."""
import sys
sys.dont_write_bytecode = True
import argparse
import os
from pathlib import Path
import shutil
from common import NAME, ROOT

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--agent',required=True,choices=['codex','claude'])
    p.add_argument('--project',type=Path)
    p.add_argument('--dest',type=Path,help='Explicit parent skills directory, for a portable/test installation')
    a=p.parse_args()
    if a.dest and a.project: p.error('Choose --dest or --project, not both.')
    if a.dest: base=a.dest.expanduser().resolve()
    elif a.project:
        project=a.project.expanduser().resolve()
        if not project.is_dir(): p.error('Project directory must already exist.')
        base=project/('.agents' if a.agent=='codex' else '.claude')/'skills'
    elif a.agent=='codex': base=Path(os.environ.get('CODEX_HOME', str(Path.home()/'.codex'))).expanduser()/'skills'
    else: base=Path.home()/'.claude'/'skills'
    dest=base/NAME
    if dest.exists(): p.error('Destination already exists; nothing overwritten: '+str(dest))
    if dest.resolve().is_relative_to(ROOT): p.error('Install destination cannot be inside the source skill.')
    from validate import validate
    errors=validate(check_hashes=True)
    if errors: p.error('Package validation failed: '+'; '.join(errors))
    base.mkdir(parents=True,exist_ok=True)
    shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    print('Installed:',dest)
    print('Codex: available next turn. Claude Code: use /scroll-site-studio or read SKILL.md.')
    return 0

if __name__=='__main__': raise SystemExit(main())
