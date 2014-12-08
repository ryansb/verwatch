#!/usr/bin/env python

import setuptools

VERSION = "0.6"

setuptools.setup(
    name='verwatch',
    version=VERSION,
    description='Package version watch utility',
    author='Jakub Ruzicka',
    author_email='jruzicka@redhat.com',
    url='http://github.com/yac/verwatch',
    packages=['verwatch','verwatch.fetchers'],
    entry_points={
        "console_scripts": ["verw = verwatch.shell:main"]
    },
    install_requires=[
        "blessings",
    ],
    )
