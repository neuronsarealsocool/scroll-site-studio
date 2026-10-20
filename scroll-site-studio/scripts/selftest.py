#!/usr/bin/env python3
"""Offline integration tests in a disposable copy; never edits an installed skill/site."""
import sys
sys.dont_write_bytecode = True
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile
from common import ROOT, digest

def main():
    env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
    with tempfile.TemporaryDirectory(prefix='scrollsite-test-') as tmp:
        temp=Path(tmp); skill=temp/'skill'
        shutil.copytree(ROOT,skill,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        def call(script,*args,ok=True):
            result=subprocess.run([sys.executable,str(skill/'scripts'/script),*map(str,args)],capture_output=True,text=True,env=env)
            if (result.returncode==0)!=ok: raise AssertionError(script+' unexpected outcome: '+result.stdout+result.stderr)
            return result
        call('validate.py','--write-hashes')
        for template in ('bounded-walkthrough','editorial-layers'):
            target=temp/template;call('catalog.py','init',template,'--dest',target)
            assert (target/'index.html').is_file()
            call('catalog.py','init',template,'--dest',target,ok=False)
        # A credential-shaped input must not be imported, and no destination is created.
        unsafe=temp/'unsafe';shutil.copytree(temp/'editorial-layers',unsafe);(unsafe/'.env').write_text('SAMPLE=value\n')
        call('catalog.py','add-template','--id','unsafe','--source',unsafe,'--title','Unsafe','--description','Test','--license','MIT',ok=False)
        assert not (skill/'assets/templates/unsafe').exists()
        call('catalog.py','add-template','--id','valid-import','--source',temp/'editorial-layers','--title','Imported editorial','--description','Sanitized template import','--license','MIT')
        call('catalog.py','init','valid-import','--dest',temp/'from-import')
        assert (temp/'from-import/assets/layers.js').is_file()
        call('catalog.py','add-reference','--id','new-source','--url','https://example.com/design','--title','Source','--notes','Link only')
        call('catalog.py','add-reference','--id','bad-source','--url','https://example.com/design?token=private','--title','Bad','--notes','Test',ok=False)
        call('validate.py',ok=False) # Catalog edit invalidates the previous integrity manifest.
        call('validate.py','--write-hashes')
        install=temp/'codex-skills';call('install.py','--agent','codex','--dest',install)
        call('install.py','--agent','codex','--dest',install,ok=False)
        assert (install/'scroll-site-studio/vendor/scroll-craft/engine/scrollcraft.js').is_file()
        claude=temp/'claude-skills';call('install.py','--agent','claude','--dest',claude)
        call('release.py','--out',temp/'release')
        archive=next((temp/'release').glob('*.zip'))
        with zipfile.ZipFile(archive) as z:
            z.extractall(temp/'roundtrip')
        extracted=temp/'roundtrip/scroll-site-studio'
        checks=json.loads((extracted/'SHA256SUMS.json').read_text())
        assert all(digest(extracted/relative)==expected for relative,expected in checks.items())
        # Integrity protection catches a changed runtime after extraction.
        engine=skill/'assets/templates/bounded-walkthrough/assets/flight.js';engine.write_text(engine.read_text()+'\n// tamper test\n')
        call('validate.py',ok=False)
    print('PASS: template copies, no overwrite, private-state rejection, reference import, stale/tampered hash detection, Codex/Claude target installs, release/extract integrity. No network or paid jobs.')

if __name__=='__main__': main()
