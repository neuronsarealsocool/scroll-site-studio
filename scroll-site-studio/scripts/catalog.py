#!/usr/bin/env python3
"""List, instantiate and extend the maintained template/reference catalog."""
import sys
sys.dont_write_bytecode = True
import argparse
from pathlib import Path
import shutil
from urllib.parse import urlparse
from common import ROOT, identifier, inside, read_json, write_json, scan

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('list')
    init=sub.add_parser('init'); init.add_argument('id'); init.add_argument('--dest',required=True,type=Path)
    add=sub.add_parser('add-template'); add.add_argument('--id',required=True); add.add_argument('--source',required=True,type=Path); add.add_argument('--title',required=True); add.add_argument('--description',required=True); add.add_argument('--license',required=True)
    ref=sub.add_parser('add-reference'); ref.add_argument('--id',required=True); ref.add_argument('--url',required=True); ref.add_argument('--title',required=True); ref.add_argument('--notes',required=True)
    a=p.parse_args(); data=read_json(ROOT/'catalog.json')
    if a.command=='list':
        for item in data['templates']: print(item['id']+' — '+item['description'])
        print('Design/source references:',len(data['references'])); return 0
    if a.command=='init':
        match=next((t for t in data['templates'] if t['id']==a.id),None)
        if not match: p.error('Unknown template id.')
        dest=a.dest.expanduser().resolve()
        if dest.exists(): p.error('Destination exists; nothing overwritten.')
        if dest.is_relative_to(ROOT): p.error('Create site projects outside the skill.')
        shutil.copytree(inside(ROOT,match['path']),dest)
        print('Created:',dest); return 0
    identifier(a.id)
    if any(x['id']==a.id for x in data['templates']+data['references']): p.error('Catalog id already exists.')
    if a.command=='add-reference':
        parsed=urlparse(a.url)
        if parsed.scheme!='https' or not parsed.hostname or parsed.username or parsed.password or parsed.query: p.error('Use a public HTTPS reference without credentials, tokens or query parameters.')
        data['references'].append({'id':a.id,'url':a.url,'title':a.title,'notes':a.notes,'redistribution':'link-only'})
    else:
        source=a.source.resolve()
        if not source.is_dir() or not (source/'index.html').is_file() or not (source/'TEMPLATE.md').is_file(): p.error('Template needs index.html and TEMPLATE.md.')
        errors=scan(source)
        if errors: p.error('; '.join(errors))
        destination=ROOT/'assets/templates'/a.id
        if destination.exists(): p.error('Template folder already exists.')
        if source==ROOT or ROOT.is_relative_to(source) or source.is_relative_to(destination): p.error('Source cannot contain this skill or destination.')
        shutil.copytree(source,destination)
        data['templates'].append({'id':a.id,'title':a.title,'description':a.description,'path':'assets/templates/'+a.id,'license':a.license,'status':'imported-needs-validation'})
    write_json(ROOT/'catalog.json',data)
    print('Added:',a.id,'— review, validate, then release to refresh checksums.')
    return 0

if __name__=='__main__':
    try: raise SystemExit(main())
    except ValueError as e: raise SystemExit(str(e))
