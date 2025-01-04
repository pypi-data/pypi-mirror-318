from setuptools import setup
versionContext = {}
with open('rtipc/version.py') as f:
    exec(f.read(), versionContext)

import sys

setup(
    name='rtipc',
    description='A Python binding for https://gitlab.com/etherlab.org/rtipc',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    version=versionContext['__version__'],
    url='https://github.com/cielavenir/rtipc',
    license='LGPL',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['rtipc'],
    zip_safe=False,
    # include_package_data=True,
    platforms='any',
    install_requires=[
        'six',
        'aenum~=2.2; python_version < "3"',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
