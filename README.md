# websearcher

# Purpose

## Functionality

### Get suggested spellings
### Get top hits
### Concatenate regexes
### Download web pages
### Unit tests

## Download pages 2 ways

### Download web page containing HTML, then search
Download a list of web pages and store them locally.
Then search them for a regular expression.
Storing pages enables searching multiple times without re-downloading.

### Download web page containing HTML and Javascript
Many web requests return a combination of HTML and Javascript.
Viewing "page source" shows html and javascript, but not the result of running the javascript.

For example, a google search.

        https://www.google.com/#q=pythan

Use selenium webdriver to load the page in a browser.
Have selenium wait until the browser executes the javascript and gets more html.
Then parse and search the page e.g. with Beautiful Soup.

# References

## searcher Python 3
https://github.com/beepscore/searcher

## Download web page containing HTML and Javascript
http://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

http://blog.databigbang.com/web-scraping-ajax-and-javascript-sites/

http://stackoverflow.com/questions/11804497/python-3-web-scraping-and-javascript-oh-my?rq=1

### selenium webdriver
Selenium version 3 needs a driver to launch a browser.

#### Firefox geckodriver
https://www.seleniumeasy.com/selenium-tutorials/launching-firefox-browser-with-geckodriver-selenium-3
https://github.com/mozilla/geckodriver

##### macOS
install via homebrew

    brew install geckodriver

Then in python file
browser = webdriver.Firefox()

2016-10-23 Firefox with current geckodriver works, but logs warning
    'NoneType' object has no attribute 'path'
    
#### Chrome chromedriver

##### macOS
install via homebrew

    brew install chromedriver
    
Then in python file
browser = webdriver.Chrome()

2016-10-23 Chrome with chromedriver, log doesn't show a warning
    
#### Google spell checker api
free use is limited, then pay  
https://code.google.com/archive/p/google-api-spelling-java/

## Beautiful Soup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class

http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup

## Python modules and packages
http://www.dabeaz.com/modulepackage/ModulePackage.pdf

https://www.youtube.com/watch?v=0oTh1CXRaQ0

# Results

## activate the project's virtual environment
For more info about venv see Appendix.

### In terminal shell, cd to project root directory

    cd websearcher

### on macOS
Supply path to websearcher, e.g.

    source ./websearcher/venv/bin/activate

### on Windows
    venv\Scripts\activate

## Get suggested spellings
Don't commit actual input file.
In .gitignore ignored oovwords.csv

    python3 -m get_suggested_spellings -in_dir "data/input" -in_file "oovwords.csv" -out_dir "data/output" -out_file "suggested_spelling_output.csv"

### to use default argument values
    python3 -m get_suggested_spellings

## Get top hits
    python3 -m get_top_hits

## Concatenate regexes
    python3 -m concatenate_regex
    
## Download web pages
    python3 -m download_web

### Search files and write search output to file
Search is similar to Unix/Linux grep command

#### specify argument values
Note: Suggest use different values for download_directory and output file directory.

Otherwise subsequent searches might accidentally search an output file.

    python3 -m search_web -expression "ython" -search_directory "data/downloads" -out_dir "data/output" -out_file "websearcher_output.txt"

#### to use default argument values
    python ./websearcher/search_web.py

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

---

## Appendix Download web page containing HTML and Javascript
Many web requests return a combination of HTML and Javascript.
For example, a google search.

        https://www.google.com/#q=javascwipt

In these cases, we can use a web browser to run the javascript and get more html.

http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class

use class_ not Python keyword class

## oovlist.csv
File from Windows had line endings that show as ^M in vim.
Changed to Unix line endings.
http://stackoverflow.com/questions/811193/how-to-convert-the-m-linebreak-to-normal-linebreak-in-a-file-opened-in-vim
at vim command line type as below, including ^V and ^M

    :%s/<Ctrl-V><Ctrl-M>/\r/g

---

## Appendix virtual environment venv

The project uses a virtual environment.

https://docs.python.org/3/library/venv.html

This can hold a python version and pip installed packages such as "requests".

https://github.com/kennethreitz/requests

### Install virtual environment in directory named "venv"

    $ cd <project root directory>
    python -m venv venv

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

    ➜  websearcher git:(master) source ./venv/bin/activate

### Now active python is in venv and is version 3.5.1

Notice command prompt shows venv is active

    (venv) ➜  websearcher git:(master) which python
    /Users/stevebaker/Documents/projects/pythonProjects/websearcher/venv/bin/python
    (venv) ➜  websearcher git:(master) python --version
    Python 3.5.1


### Deactivate virtual environment
In shell run deactivate
    (venv) ➜  websearcher git:(master) ✗ deactivate

## Appendix upgrade pip
With virtualenv active

    pip install --upgrade pip

    Successfully uninstalled pip-8.1.0
    Successfully installed pip-8.1.2

Installed to project venv

## Appendix pip install dependencies
With virtualenv active

    pip install requests
    pip install beautifulsoup4
    pip install selenium

### update to latest selenium
    pip3 install --upgrade selenium

Then manually edited requirements.txt

## Appendix clone app from github to another machine
After cloning app from github, activating venv did still showed system python.
Fixed as follows:

    delete ./venv
    Re-run pyvenv venv
    pip re-install packages.

## Appendix Use requirements.txt
In requirements.txt list dependencies, update version numbers. Then run

    pip install -r requirements.txt --upgrade

