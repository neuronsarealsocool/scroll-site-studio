#!/usr/bin/env python3
"""Serve an explicit static project on loopback, never the skill/private workspace."""
import sys
sys.dont_write_bytecode = True
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--root',type=Path,required=True); p.add_argument('--port',type=int,default=4500); a=p.parse_args()
    root=a.root.resolve()
    if not (root/'index.html').is_file(): p.error('Root must be the site directory containing index.html.')
    forbidden={'.env','.git','.openai','.herenow','.dev.vars'}
    if any(part.name in forbidden or part.name.startswith(('.env.','.dev.vars.')) or part.is_symlink() for part in root.rglob('*')): p.error('Private state or symlinks found under preview root. Use a sanitized static build directory.')
    server=ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(root)))
    print('Local preview: http://127.0.0.1:'+str(server.server_port),flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
