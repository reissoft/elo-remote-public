"""Public distribution automation. No private app code or signing key needed."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = Path(__file__).resolve().parents[1]
NAMES = {'EloRemote-windows-x86_64.exe', 'EloRemote-linux-x86_64', 'EloRemote-Windows.zip',
         'EloRemote-Linux-x86_64.tar.gz', 'libjuice-LICENSE.txt', 'libjuice-source.tar.gz'}
ALL = NAMES | {'update.json', 'update.json.sig', 'SHA256SUMS.txt'}


def gh(*args, **kwargs):
    return subprocess.run(['gh', *args], check=True, **kwargs)


def verify(folder, tag, repository, public_key):
    raw = (folder / 'update.json').read_bytes()
    if len(raw) > 32768: raise ValueError('Manifest too large')
    public_key.verify(base64.b64decode((folder / 'update.json.sig').read_bytes().strip(), validate=True), raw)
    manifest = json.loads(raw)
    if manifest.get('schema') != 1 or manifest.get('repository') != repository or manifest.get('channel') != 'stable' or 'v' + manifest.get('version', '') != tag:
        raise ValueError('Release does not match signed manifest')
    if set(manifest.get('downloads', {})) != NAMES or {p.name for p in folder.iterdir()} != ALL:
        raise ValueError('Unexpected or missing release files')
    for name, info in manifest['downloads'].items():
        path = folder / name
        if path.is_symlink() or path.stat().st_size != info['size']: raise ValueError('Wrong asset size')
        result = hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024*1024), b''): result.update(chunk)
        if result.hexdigest() != info['sha256']: raise ValueError('Wrong asset digest')
    for platform, name in [('windows-x86_64','EloRemote-windows-x86_64.exe'), ('linux-x86_64','EloRemote-linux-x86_64')]:
        asset = manifest['assets'][platform]
        if asset['name'] != name or {k:asset[k] for k in ('sha256','size')} != manifest['downloads'][name]:
            raise ValueError('Updater payload does not match release')
    return manifest


def main():
    tag, repository = os.environ['RELEASE_TAG'], os.environ['RELEASE_REPOSITORY']
    if not re.fullmatch(r'v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', tag): raise ValueError('Stable tags only')
    config = json.loads((ROOT / 'update-public-key.json').read_text(encoding='utf-8'))
    if repository != config['repository']: raise ValueError('Wrong repository')
    public_key = Ed25519PublicKey.from_public_bytes(base64.b64decode(config['public_key'], validate=True))
    meta = json.loads(gh('release','view',tag,'--repo',repository,'--json','isDraft,isPrerelease',capture_output=True,text=True).stdout)
    if meta['isDraft'] or meta['isPrerelease']: raise ValueError('Only published stable releases can be promoted')
    with tempfile.TemporaryDirectory() as work:
        folder=Path(work)/'release';folder.mkdir()
        gh('release','download',tag,'--repo',repository,'--dir',str(folder))
        manifest=verify(folder,tag,repository,public_key)
        exists=subprocess.run(['gh','release','view','last','--repo',repository],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
        if exists:
            previous=Path(work)/'previous';previous.mkdir()
            gh('release','download','last','--repo',repository,'--dir',str(previous),'--pattern','update.json','--pattern','update.json.sig')
            raw=(previous/'update.json').read_bytes()
            public_key.verify(base64.b64decode((previous/'update.json.sig').read_bytes().strip(),validate=True),raw)
            old=json.loads(raw)
            if tuple(map(int,old['version'].split('.'))) > tuple(map(int,manifest['version'].split('.'))):
                raise ValueError('Refusing to downgrade last')
        else:
            gh('release','create','last','--repo',repository,'--title','Elo Remote — última versão estável',
               '--notes','Links permanentes de download. Consulte o histórico para versões anteriores.','--latest=false')
        ordered=sorted(ALL-{'update.json.sig'})+['update.json.sig']
        gh('release','upload','last','--repo',repository,'--clobber',*[str(folder/name) for name in ordered])
        gh('release','edit','last','--repo',repository,'--notes','Última versão estável: '+manifest['version']+'. Links permanentes de download.')


if __name__=='__main__': main()
