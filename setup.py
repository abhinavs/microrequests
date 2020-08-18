from setuptools import setup
import re
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

def readme():
      with open(os.path.join(here, 'README.rst')) as f:
            return f.read()


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(name='microrequests',
    version=find_version('microrequests', '__init__.py'),
    description='microrequests is a wrapper over requests module - makes it more efficient to consume microservices in Python',
    long_description=readme(),
    url='http://www.abhinav.co/microrequests.html',
    author='Abhinav Saxena',
    author_email='abhinav061@gmail.com',
    packages=['microrequests'],
    install_requires=[
        'requests'
    ],
    test_suite='pytest',
    tests_require=['pytest'],
    zip_safe=False)
