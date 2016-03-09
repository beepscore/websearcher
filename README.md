# web_searcher

# Purpose
Download a list of web pages and store them locally.
Then search them for a regular expression.
Storing pages enables searching multiple times without re-downloading.

# Results

## Command line
In terminal shell, go to a directory outside of project directory.
Then

    source ./websearcher/venv/bin/activate

TODO something like

    ./download_files -filenames filenames.txt -out_directory download_directory

This part is similar to Unix/Linux grep command
Note: Suggest use different values for download_directory and results_directory.
Otherwise subsequent searches might accidentally search results file.

    ./search_files -expression expression -file_path download_directory -results_directory results_directory

## Unit tests
To run tests, open terminal shell and use run_tests. For more info see script.

    $ ./run_tests

---

## Appendix virtual environment venv

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

### Deactivate virtual environment
In shell run deactivate
    (venv) ➜  websearcher git:(master) ✗ deactivate
