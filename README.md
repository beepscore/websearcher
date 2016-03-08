# web_searcher

# Purpose
Download a sequence of web pages and store them locally.
Then search them for a regular expression.
Storing pages enables searching multiple times without re-downloading.

# Results
To run tests, use script run_tests. For more info see script.

    $ ./run_tests

## virtual environment venv

The project uses a virtual environment.  
https://docs.python.org/3/library/venv.html
This can hold a python version and pip installed packages such as "requests".
https://github.com/kennethreitz/requests

### Install virtual environment in directory named "venv"

    $ pyvenv venv

### Before activating virtual environment
On my machine, active python is 2.7.11

    ➜  websearcher git:(master) ✗ which python
    /usr/local/bin/python
    ➜  websearcher git:(master) python --version
    Python 2.7.11

On my machine, to use python3 must specify python3

    ➜  websearcher git:(master) which python3
    /usr/local/bin/python3

### Activate virtual environment
    ➜  websearcher git:(master) source venv/bin/activate

### Now active python is in venv and is version 3.5.1
Notice command prompt shows venv is active

    (venv) ➜  websearcher git:(master) which python
    /Users/stevebaker/Documents/projects/pythonProjects/websearcher/venv/bin/python
    (venv) ➜  websearcher git:(master) python --version
    Python 3.5.1
