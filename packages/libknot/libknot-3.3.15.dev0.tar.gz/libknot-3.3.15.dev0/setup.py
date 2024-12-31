import pathlib
import setuptools

p = pathlib.Path("README.md")
if p.exists():
    long_description = p.read_text()

setuptools.setup(
    name='libknot',
    version='3.3.15dev',
    description='Python bindings for libknot',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='CZ.NIC, z.s.p.o.',
    author_email='knot-dns@labs.nic.cz',
    url='https://gitlab.nic.cz/knot/knot-dns/-/tree/master/python/libknot',
    license='GPL-3.0',
    packages=['libknot'],
    classifiers=[ # See https://pypi.org/classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
    ],
    python_requires='>=3.5',
)
