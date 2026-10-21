#!/usr/bin/env python3
"""Check the portable package, catalog, provenance and release file hashes."""
import sys
sys.dont_write_bytecode = True
import argparse
import re
from common import ROOT, digest, file_list, identifier, inside, read_json, scan, write_json

def hashes():
    return {p.relative_to(ROOT).as_posix():digest(p) for p in file_list() if p.name!='SHA256SUMS.json'}

def validate(check_hashes=True):
    errors=scan(ROOT)
    for name in ('SKILL.md','README.md','LICENSE','THIRD_PARTY.md','catalog.json','vendor-manifest.json','package.json'):
        if not (ROOT/name).is_file(): errors.append('Missing '+name)
    try:
        package=read_json(ROOT/'package.json'); catalog=read_json(ROOT/'catalog.json')
        text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        if not text.startswith('---\n') or 'name: scroll-site-studio\n' not in text: errors.append('Invalid primary frontmatter.')
        if 'version: '+package['version'] not in text: errors.append('Skill/package versions disagree.')
        seen=set()
        for t in catalog['templates']:
            identifier(t['id'])
            if t['id'] in seen: errors.append('Duplicate catalog id '+t['id'])
            seen.add(t['id']); folder=inside(ROOT,t['path'])
            for name in ('index.html','TEMPLATE.md'):
                if not (folder/name).is_file(): errors.append('Missing template file: '+t['id']+'/'+name)
        for ref in catalog['references']:
            identifier(ref['id'])
            if ref['id'] in seen: errors.append('Duplicate catalog id '+ref['id'])
            seen.add(ref['id'])
            if not ref['url'].startswith('https://'): errors.append('Reference must be HTTPS: '+ref['id'])
        for pack in catalog.get('reference_packs',[]):
            identifier(pack['id'])
            if pack['id'] in seen: errors.append('Duplicate catalog id '+pack['id'])
            seen.add(pack['id'])
            if not inside(ROOT,pack['index']).is_file(): errors.append('Missing source pack index: '+pack['id'])
            if not pack['sources'] or any(not source['url'].startswith('https://') for source in pack['sources']): errors.append('Invalid source pack links: '+pack['id'])
        for vendor in read_json(ROOT/'vendor-manifest.json')['components']:
            path=inside(ROOT,vendor['path'])
            if not (path/'SKILL.md').is_file() or not (path/'LICENSE').is_file(): errors.append('Incomplete vendor '+vendor['id'])
            if vendor.get('files'):
                actual={p.relative_to(path).as_posix():digest(p) for p in file_list(path)}
                if actual!=vendor['files']: errors.append('Vendor files differ from pinned snapshot: '+vendor['id'])
        for name in re.findall(r'`((?:references|vendor)/[^`]+\.md)`',text):
            if not inside(ROOT,name).is_file(): errors.append('Broken entrypoint reference: '+name)
        if check_hashes:
            stored=ROOT/'SHA256SUMS.json'
            if not stored.is_file(): errors.append('Missing SHA256SUMS.json; review then use --write-hashes.')
            elif read_json(stored)!=hashes(): errors.append('Release hashes are stale or files changed.')
    except (ValueError,KeyError,OSError) as e: errors.append('Manifest validation: '+str(e))
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--write-hashes',action='store_true'); a=p.parse_args()
    errors=validate(check_hashes=not a.write_hashes)
    if errors:
        print('\n'.join('FAIL: '+e for e in errors)); return 1
    if a.write_hashes: write_json(ROOT/'SHA256SUMS.json',hashes())
    print('PASS: package, catalogs, licenses, vendor snapshots, private-state scan and release hashes.'); return 0

if __name__=='__main__': raise SystemExit(main())
