#!/usr/bin/env python3
"""Read-only local dependencies; never checks balances or starts paid jobs."""
import sys
sys.dont_write_bytecode = True
import argparse
import json
import platform
import shutil
import sys
from common import binary, run

def report(mode='site'):
    rows = [{'name':'python', 'ok':sys.version_info >= (3,10), 'version':platform.python_version(), 'required':True}]
    for name in ('ffmpeg', 'ffprobe'):
        path = binary(name)
        try:
            out = run([path, '-version']) if path else None
            rows.append({'name':name,'ok':out is not None,'path':path,'required':mode != 'site',
                         'version':out.stdout.splitlines()[0] if out else ''})
        except Exception:
            rows.append({'name':name,'ok':False,'path':path,'required':mode != 'site'})
    ffmpeg = binary('ffmpeg')
    if ffmpeg:
        try:
            filters = run([ffmpeg,'-hide_banner','-filters']).stdout
            encoders = run([ffmpeg,'-hide_banner','-encoders']).stdout
            rows.append({'name':'media-capabilities','ok':all(x in filters for x in ('scale','fps','testsrc2')) and 'libx264' in encoders,'required':mode != 'site'})
        except Exception:
            rows.append({'name':'media-capabilities','ok':False,'required':mode != 'site'})
    node = shutil.which('node')
    try:
        version = run([node, '--version']).stdout.strip() if node else ''
        rows.append({'name':'node (Scroll Craft only)','ok':bool(version) and int(version.lstrip('v').split('.')[0]) >= 18,'version':version,'required':mode == 'scroll-craft'})
    except Exception:
        rows.append({'name':'node (Scroll Craft only)','ok':False,'required':mode == 'scroll-craft'})
    return {'platform':platform.system(),'mode':mode,'checks':rows,'network_used':False,'paid_jobs':0}

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--json',action='store_true'); parser.add_argument('--mode',choices=['site','video','scroll-craft'],default='site'); args=parser.parse_args()
    result=report(args.mode)
    if args.json: print(json.dumps(result,indent=2))
    else:
        for row in result['checks']: print(('OK  ' if row['ok'] else 'MISS')+' '+row['name']+' '+row.get('version',''))
        print('Missing items: run setup.py --plan. No network or generation was used.')
    sys.exit(0 if all(r['ok'] for r in result['checks'] if r['required']) else 1)
