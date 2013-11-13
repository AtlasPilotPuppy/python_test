from setuptools import setup, find_packages
from distutils.core import Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

requires = [
    'py==1.4.18',
    'pytest==2.4.2',
    'wsgiref==0.1.2',
]


setup(
    name="pychallenge",
    version="1.0.0",
    packages=find_packages(),
    package_data={
        'pychallenge': [
            '*.*',
        ]
    },
    cmdclass={'test': PyTest},
    scripts=["bin/nth-prime.py", "bin/palindrome-product.py"],
    install_requires=requires,
    long_description="Python Coding Challenge"
)
