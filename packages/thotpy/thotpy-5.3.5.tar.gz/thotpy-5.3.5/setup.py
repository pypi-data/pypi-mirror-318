from setuptools import find_packages, setup
import re

DESCRIPTION = "The Text enHancement & Optimization for scienTific researcH with PYthon, or just ThothPy, allows you to create, modify and analyze all kinds of text files, with a special focus on (but not limited to) ab-initio calculations."

def get_version(version_path):
    with open(version_path, 'r') as file:
        content = file.read()
        version_match = re.search(r"version\s*=\s*'([^']+)'", content)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version.")

def get_readme():
    with open('README.md', 'r') as f:
        long_description = f.read()
        return long_description

setup(
    name='thotpy', 
    version=get_version('thotpy/core.py'),
    author='Pablo Gila-Herranz',
    author_email='pgila001@ikasle.ehu.eus',
    description=DESCRIPTION,
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    packages=['thotpy'],
    install_requires=['pandas'],
    extras_requires={
        'dev': ['pytest', 'twine']
        },
    python_requires='>=3',
    license='AGPL-3.0',
    keywords=['python', 'thot', 'thotpy', 'thoth', 'thothpy', 'text', 'inputmaker', 'DFT', 'Density Functional Theory', 'MD', 'Molecular Dynamics', 'ab-initio', 'Quantum ESPRESSO', 'Phonopy'],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Other OS",
    ]
)
