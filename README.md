# Python Challenge


## Overview

Some programming exercises


## Installation

### Manual installation

#### Virtualenv
Recommended that you create a virtualenv to install this code and it's dependencies into.

See [virtualenv docs](https://pypi.python.org/pypi/virtualenv)

#### Run the install
You can install the code simply by running

`python setup.py test` 

If the tests pass proceed with the intsall. Execute

`python setup.py install` 

from the project's root directory.

## Usage

After installation the following will be available on your path 

`nth-prime.py n`

You can run it without arguments to get a help message or specify an integer of reasonable size to see what the nth prime is.

`palindrome-product.py`


## Testing
You can run the automated tests with

`python setup.py test`

If the package is already installed there might be some conflicts. You can usually clean these up by deleting the build directory

`rm -rf build/`

from the project's root directory.

The run tests from setup.py or by `py.test`

## Information

Source: https://github.com/lakeslc/pychallenge

Authors: [Jonathan Randall](https://github.com/lakeslc/)
