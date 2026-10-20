#!/usr/bin/env python3
"""Produce a local ZIP and checksum from a validated self-contained skill."""
import sys
sys.dont_write_bytecode = True
import argparse
from pathlib import Path
import zipfile
from common import NAME, ROOT, digest, file_list, read_json, write_json
from validate import validate, hashes

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--out',required=True,type=Path); a=p.parse_args()
    out=a.out.resolve()
    if out.is_relative_to(ROOT): p.error('Release directory must be outside the skill.')
    errors=validate(check_hashes=False)
    if errors: p.error('; '.join(errors))
    write_json(ROOT/'SHA256SUMS.json',hashes())
    errors=validate()
    if errors: p.error('; '.join(errors))
    version=read_json(ROOT/'package.json')['version']; out.mkdir(parents=True,exist_ok=True)
    archive=out/(NAME+'-'+version+'.zip')
    if archive.exists(): p.error('Release exists; bump version or choose a new output directory.')
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for item in file_list(): z.write(item,NAME+'/'+item.relative_to(ROOT).as_posix())
    checksum=digest(archive)
    archive.with_suffix('.zip.sha256').write_text(checksum+'  '+archive.name+'\n',encoding='utf-8')
    print(archive); print('SHA256 '+checksum); return 0

if __name__=='__main__': raise SystemExit(main())
