# script-utils
My personalized python scripting helpers and utilities.

Most of this stuff is just a function to wrap a task that comes up a lot in the
course of using python for shell scripting, such as traversing a directory
structure, etc.

Note that I have made this repo public so that others may take code from it,
not because I am offering this code as a library for public use. It's really for
my personal use only. Thus, PRs will most likely not be merged, and I don't
intend to ever upload this to PyPI. If you want a package that does something
similar to this, check out [auxly](https://github.com/jeffrimko/Auxly).

## installation
First, make sure the `setuptools` and `wheel` python packages are installed. Then:

``` sh
git clone https://github.com/dudelson/python-script-utils
cd python-script-utils
python3 setup.py sdist bdist_wheel
pip install .
```

## usage
``` python
import script_utils as su
```
