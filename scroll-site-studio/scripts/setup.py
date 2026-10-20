#!/usr/bin/env python3
"""Plan or explicitly install dependencies via an existing OS package manager."""
import sys
sys.dont_write_bytecode = True
import argparse
import platform
import shutil
import subprocess

def command(dependency):
    system=platform.system()
    if system=='Windows' and shutil.which('winget'):
        return ['winget','install','--exact','--id',{'ffmpeg':'Gyan.FFmpeg','node':'OpenJS.NodeJS.LTS'}[dependency]]
    if system=='Darwin' and shutil.which('brew'):
        return ['brew','install', 'ffmpeg' if dependency=='ffmpeg' else 'node']
    if system=='Linux':
        for manager,action,package in [('apt-get','install',dependency if dependency=='ffmpeg' else 'nodejs'),('dnf','install',dependency if dependency=='ffmpeg' else 'nodejs'),('pacman','-S',dependency if dependency=='ffmpeg' else 'nodejs')]:
            if shutil.which(manager): return ['sudo',manager,action,package]
    return None

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--plan',action='store_true'); p.add_argument('--install',choices=['ffmpeg','node']); a=p.parse_args()
    if a.install:
        cmd=command(a.install)
        if not cmd: p.error('No supported package manager found. Install from https://ffmpeg.org/download.html or https://nodejs.org/ then rerun doctor.py.')
        print('Running package manager:',subprocess.list2cmdline(cmd),flush=True)
        return subprocess.call(cmd)
    for name in ('ffmpeg','node'):
        cmd=command(name)
        print(name+': '+(subprocess.list2cmdline(cmd) if cmd else 'Use the official project download for this OS.'))
    print('FFmpeg package includes ffprobe. Python 3.10+ is the bootstrap prerequisite.')
    print('Optional Scroll Craft harness: Chrome + npm install --save-dev playwright-core in the site project, when the host permits it.')
    print('No dependencies were installed; no license prompts were accepted; no model was called.')
    return 0

if __name__=='__main__': raise SystemExit(main())
