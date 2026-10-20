#!/usr/bin/env python3
"""Local media preparation, with no uploads or generation API calls."""
import sys
sys.dont_write_bytecode = True
import argparse
import json
from pathlib import Path
import tempfile
from common import binary, run, write_json

def tool(name):
    path=binary(name)
    if not path: raise ValueError(name+' missing. Run setup.py --plan.')
    return path

def probe(path):
    return json.loads(run([tool('ffprobe'),'-v','error','-show_streams','-show_format','-of','json',path]).stdout)

def encode(source,target,mobile=False):
    target=Path(target)
    if target.exists(): raise ValueError('Refusing to overwrite '+str(target))
    target.parent.mkdir(parents=True,exist_ok=True)
    run([tool('ffmpeg'),'-v','error','-i',source,'-map','0:v:0','-an','-c:v','libx264','-preset','slow','-crf','23' if mobile else '20','-pix_fmt','yuv420p','-g','4' if mobile else '8','-keyint_min','4' if mobile else '8','-sc_threshold','0','-movflags','+faststart','-n',target],timeout=300)

def frames(source,directory,stem=None):
    directory=Path(directory); directory.mkdir(parents=True,exist_ok=True)
    name=stem or Path(source).stem
    first=directory/(name+'-first.jpg'); last=directory/(name+'-last.jpg')
    if first.exists() or last.exists(): raise ValueError('Boundary files already exist; nothing overwritten.')
    run([tool('ffmpeg'),'-v','error','-i',source,'-frames:v','1','-q:v','2','-n',first])
    run([tool('ffmpeg'),'-v','error','-i',source,'-map','0:v:0','-fps_mode','passthrough','-update','1','-q:v','2','-n',last],timeout=300)
    return first,last

def synthetic(target,width,height,mobile=False,duration=2):
    run([tool('ffmpeg'),'-v','error','-f','lavfi','-i',f'testsrc2=size={width}x{height}:rate=24','-t',str(duration),'-an','-c:v','libx264','-preset','ultrafast','-crf','28','-pix_fmt','yuv420p','-g','4' if mobile else '8','-keyint_min','4' if mobile else '8','-sc_threshold','0','-movflags','+faststart','-n',target],timeout=180)

def smoke():
    with tempfile.TemporaryDirectory(prefix='scrollsite-media-') as temp:
        root=Path(temp); source=root/'source.mp4'; target=root/'encoded.mp4'
        synthetic(source,320,180,duration=1)
        encode(source,target)
        first,last=frames(target,root)
        result=probe(target); stream=next(s for s in result['streams'] if s['codec_type']=='video')
        assert (stream['width'],stream['height'])==(320,180)
        assert stream['codec_name']=='h264' and stream['pix_fmt']=='yuv420p'
        assert not any(s['codec_type']=='audio' for s in result['streams'])
        assert first.stat().st_size>100 and last.stat().st_size>100
        assert first.read_bytes()!=last.read_bytes(), 'Motion/boundary extraction did not advance.'
        print('PASS: encode, native dimensions, silent H.264, first/last decoded frames. No paid jobs.')

def demo(site):
    site=Path(site).resolve(); index=site/'index.html'
    if not (site/'TEMPLATE.md').is_file() or not index.is_file(): raise ValueError('Use a copy of the bounded-walkthrough template.')
    html=index.read_text(encoding='utf-8')
    if 'data-template="bounded-walkthrough"' not in html: raise ValueError('Not the bounded-walkthrough starter.')
    folder=site/'assets/film'
    if folder.exists(): raise ValueError('Film directory already exists; no assets overwritten.')
    folder.mkdir(parents=True)
    for name in ('arrival','threshold'):
        for mobile,width,height in [(False,1280,720),(True,720,1280)]:
            stem=('mobile-' if mobile else '')+name
            target=folder/(stem+'.mp4'); synthetic(target,width,height,mobile)
            frames(target,folder,stem)
    html=html.replace('data-media-ready="false"','data-media-ready="true"').replace('Static starter · Add your footage','Technical demo · Synthetic test footage')
    index.write_text(html,encoding='utf-8')
    write_json(folder/'manifest.json',{'kind':'synthetic-offline-technical-demo','paid_jobs':0,'clips':4,'formats':['1280x720','720x1280'],'duration_per_clip_seconds':2,'warning':'Test patterns, not generated architecture or approved production media.'})
    print('Offline synthetic demo created:',site)

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='command',required=True)
    s=sub.add_parser('probe'); s.add_argument('input',type=Path)
    s=sub.add_parser('encode'); s.add_argument('input',type=Path); s.add_argument('output',type=Path); s.add_argument('--mobile',action='store_true')
    s=sub.add_parser('frames'); s.add_argument('input',type=Path); s.add_argument('--out',required=True,type=Path)
    s=sub.add_parser('demo'); s.add_argument('site',type=Path)
    sub.add_parser('smoke'); a=p.parse_args()
    if a.command=='probe': print(json.dumps(probe(a.input),indent=2))
    elif a.command=='encode': encode(a.input,a.output,a.mobile)
    elif a.command=='frames': print(*frames(a.input,a.out),sep='\n')
    elif a.command=='demo': demo(a.site)
    else: smoke()

if __name__=='__main__':
    try: main()
    except (ValueError,AssertionError) as e: raise SystemExit(str(e))
