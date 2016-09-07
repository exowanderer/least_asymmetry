# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from distutils.core import setup, Extension

### Start Creating Direcotry in site-packages ###
from os         import path, mkdir, getcwd
from subprocess import Popen
from site       import getsitepackages

CurrentDir  = getcwd() + '/'
PackageDir  = getsitepackages()[0]
dirExists   = path.exists(PackageDir)

if not dirExists:
    print PackageDir + ' DOES NOT EXIST'

InstallDir  = PackageDir + '/least_asymmetry/'
dirExists   = path.exists(InstallDir)

print''
print InstallDir
print''

try:
    if not dirExists:
        print '\n\n Directory DOES NOT Exist. Creating NOW \n\n'
        mkdir(InstallDir)
    elif len(argv) > 1 and argv[1] == 'overwrite':
        print '\n\n Directory Exists Deleting before Over Writing Symbolic Links \n\n'
        Popen(["/bin/bash", "-c", "rm -rf " + InstallDir])
        print "rm -rf " + InstallDir
        print '\n\n Re-Creating Directory NOW \n' + InstallDir + '\n\n'
        mkdir(InstallDir)
    else:
        print '\n\n Directory Exists.  If you want to overwrite all files, type "python install.py overwrite"\n\n'
except:
    raise Exception, "\n\nSomething went wrong: you probably don't have permissions to make \n" + InstallDir + '\n\n'

### End Creating Direcotry in site-packages ###


cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

ext_modules = [
    Extension(
        'make_asym',
        ['make_asym.cc'],
        include_dirs=['include'],
        language='c++',
        extra_compile_args=cpp_args,
    ),
]

setup(
    name='make_asym',
    version='0.1',
    author='Nate Lust',
    author_email='nlust@astro.princeton.edu',
    description='A module for calculating centers though least asymmetry',
    ext_modules=ext_modules,
)

### Start moving asym.py to site-packages ###
Popen(['/bin/cp', CurrentDir + 'asym.py'    , InstallDir])
Popen(['/bin/cp', CurrentDir + '__init__.py', InstallDir])
### End moving asym.py to site-packages ###
