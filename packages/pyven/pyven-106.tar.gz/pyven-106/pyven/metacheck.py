from .checks import Container
from .pipify import pipify, setupcommand
from .projectinfo import ProjectInfo
from .util import bgcontainer
from contextlib import contextmanager
from lagoon import diff
from pathlib import Path
from shutil import copy2
from tempfile import TemporaryDirectory
import sys

@contextmanager
def egginfodir(projectdir, version, dockerenabled):
    with TemporaryDirectory() as tempdir:
        copy2(projectdir / 'project.arid', tempdir)
        try:
            copy2(projectdir / 'README.md', tempdir)
        except FileNotFoundError:
            pass
        copyinfo = ProjectInfo.seek(tempdir)
        pipify(copyinfo, version)
        if dockerenabled and {'setuptools', 'wheel'} != set(copyinfo.allbuildrequires):
            with bgcontainer('-v', f"{tempdir}:{Container.workdir}", f"python:{copyinfo.pyversiontags[0]}") as container:
                container = Container(container)
                container.inituser()
                for command in ['apt-get', 'update'], ['apt-get', 'install', '-y', 'sudo']:
                    container.call(command, check = True, root = True)
                container.call(['pip', 'install', '--upgrade', 'setuptools'], check = True, root = True)
                container.call(['pip', 'install', *copyinfo.allbuildrequires], check = True, root = True)
                container.call(['python', 'setup.py', 'egg_info'], check = True)
        else:
            setupcommand(copyinfo, False, 'egg_info')
        d, = Path(tempdir).glob('*.egg-info')
        yield tempdir, d

def metacheck(projectdir, version, dockerenabled):
    with egginfodir(projectdir, version, dockerenabled) as (tempdir, d):
        p = d / 'requires.txt'
        q = projectdir / p.relative_to(tempdir)
        if p.exists():
            diff[print](p, q)
        else:
            assert not q.exists()
        p = d / 'PKG-INFO'
        q = projectdir / p.relative_to(tempdir)
        assert q.exists()
        text = diff(p, q, check = False).stdout
        sys.stdout.write(text)
        assert all(l[0] not in '<>' or l.startswith(('> Requires-Dist: ', '> License-File: ')) for l in text.splitlines())
