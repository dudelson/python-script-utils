import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))
about = {}

with open(os.path.join(here, 'script_utils', '__init__.py'), 'r') as f:
    exec(f.read(), about)

with open(os.path.join(here, 'script_utils', '__version__.py'), 'r') as f:
    exec(f.read(), about)
    
with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
        name=about['name'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__author_email__'],
        description=about['__description__'],
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=about['__url__'],
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
        ],
)
