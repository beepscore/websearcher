# websearcher

# Purpose
Download a list of web pages and store them locally.
Then search them for a regular expression.
Storing pages enables searching multiple times without re-downloading.

# References

## searcher Python 3
https://github.com/beepscore/searcher

# Results

## To use from command line
In terminal shell, go to a directory outside of project directory.

### Activate virtual environment

    source ./websearcher/venv/bin/activate

### cd to project root directory

    cd websearcher

## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.

### Bash script
Runs all test modules.  
Works on OS X. On Windows may work with Cygwin, I don't know.

    $ ./bin/run_tests

### python command
This command lists and tests all modules except web_downloader_arg_reader and web_searcher_arg_reader.

    python -m unittest tests.test_page_reader tests.test_file_writer tests.test_web_downloader tests.test_web_searcher

#### arg_reader tests
Attempting to run test_web_downloader_arg_reader and test_web_searcher_arg_reader has problem with arguments for unittest and for argparse.  
e.g. python -m unittest discover says "unrecognized arguments: discover" and wants the argparse arguments.  
TODO: Consider alternative solutions.  
http://stackoverflow.com/questions/35270177/passing-arguments-for-argparse-with-unittest-discover

## Download files and write to directory

TODO something like

    downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")

    downloader.request_urls_write_to_files()

### Search files and write search results to file
Search is similar to Unix/Linux grep command

Note: Suggest use different values for download_directory and results file directory.

Otherwise subsequent searches might accidentally search a results file.

TODO something like

    web_searcher.WebSearcher.search_directory_write_results("dat*",
    "./websearcher_data/downloads",
    "./websearcher_data/results",
    "websearcher_results.txt")

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
