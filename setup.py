#!/usr/bin/env python3

from setuptools import find_packages, setup

requirements = [
    'pulp-2to3-migrate',
    'pulp-file',
]

setup(
    name='pulp-2to3-migrate-iso',
    version='0.0.1a1.dev1',
    description='ISO extension for Pulp 2 to Pulp 3 migration tool',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    url='http://www.pulpproject.org',
    python_requires='>=3.6',
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=(
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
    entry_points={
        'pulp_2to3_migrate.plugin': [
            'iso = pulp_2to3_migrate_iso.handle:handle',
        ]
    }
)
