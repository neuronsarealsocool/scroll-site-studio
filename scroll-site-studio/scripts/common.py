"""Small standard-library helpers. No network calls or global configuration."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
NAME = 'scroll-site-studio'
FORBIDDEN = {'.git', '.env', '.herenow', '.openai', '.sites-runtime', '.wrangler',
             'node_modules', '__pycache__', '.dev.vars', '.next', '.venv',
             'credentials', 'credentials.json', 'settings.local.json'}

def inside(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Path escapes the expected directory: ' + str(relative))
    return path

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def file_list(root=ROOT):
    return sorted(p for p in Path(root).rglob('*') if p.is_file() and
                  '__pycache__' not in p.parts and p.suffix != '.pyc')

def run(args, timeout=60):
    return subprocess.run([str(a) for a in args], capture_output=True, text=True,
                          timeout=timeout, check=True)

def binary(name):
    env = os.environ.get('SCROLLSITE_' + name.upper())
    if env:
        if not Path(env).is_file():
            raise ValueError('Configured executable does not exist: SCROLLSITE_' + name.upper())
        return env
    found = shutil.which(name)
    if found:
        return found
    if name == 'ffprobe' and os.environ.get('SCROLLSITE_FFMPEG'):
        adjacent = Path(os.environ['SCROLLSITE_FFMPEG']).with_name('ffprobe.exe' if os.name == 'nt' else 'ffprobe')
        if adjacent.is_file():
            return str(adjacent)
    candidates = []
    if os.name == 'nt':
        base = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / 'AppData/Local'))) / 'Microsoft/WinGet/Packages'
        candidates.extend(base.glob('Gyan.FFmpeg*/*/bin/' + name + '.exe'))
    candidates.extend(Path(p) / name for p in ('/opt/homebrew/bin', '/usr/local/bin', '/usr/bin'))
    return str(next((p for p in candidates if p.is_file()), ''))

def identifier(value):
    if not re.fullmatch(r'[a-z][a-z0-9-]{0,62}', value):
        raise ValueError('Use a lowercase hyphenated identifier, at most 63 characters.')
    return value

def scan(root):
    """Reject known private state and credential shapes; not a proof of asset rights."""
    errors = []
    root = Path(root)
    for p in root.rglob('*'):
        rel = p.relative_to(root)
        if p.is_symlink():
            errors.append('Symlink not distributable: ' + rel.as_posix())
            continue
        if any(part in FORBIDDEN or part.startswith(('.env.', '.dev.vars.')) for part in rel.parts):
            errors.append('Private/runtime path: ' + rel.as_posix())
        if p.is_file() and p.suffix.lower() in {'.md', '.json', '.js', '.mjs', '.py', '.html', '.css', '.yaml', '.yml', '.txt'}:
            data = p.read_text(encoding='utf-8-sig', errors='replace')
            # Do not echo the actual match in diagnostics.
            patterns = [r'\b(?:r8_|sk_live_|sk-proj-|hnk_|ghp_|github_pat_)[A-Za-z0-9_-]{16,}',
                        r'(?i)Bearer\s+[A-Za-z0-9_.-]{28,}',
                        r'[A-Za-z]:[\\/]+Users[\\/]+(?:matt|Matt)[\\/]']
            if any(re.search(pattern, data) for pattern in patterns):
                errors.append('Possible credential/personal path in: ' + rel.as_posix())
    return sorted(set(errors))
