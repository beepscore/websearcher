# Purpose
Python project to download web pages and search them.

## Example usage

### Get suggested spellings

Don't commit actual input file. In .gitignore ignored oovwords.csv

    python3 -m get_suggested_spellings -in_dir "data/input" -in_file "oovwords.csv" -out_dir "data/output" -out_file "suggested_spelling_output.csv"

### to use default argument values

    python3 -m get_suggested_spellings

### Get top hits

    python3 -m get_top_hits

### Concatenate regexes

    python3 -m concatenate_regex

### Download web pages

    python3 -m download_web

#### Download pages 2 ways

#### Download web page containing HTML, then search

#### Download web page, store locally, then search
Storing pages enables searching multiple times without re-downloading.

### Search files and write search output to file

Search is similar to Unix/Linux grep command

#### specify argument values

Note: Suggest use different values for download\_directory and output
file directory.

Otherwise subsequent searches might accidentally search an output file.

    python3 -m search_web -expression "ython" -search_directory "data/downloads" -out_dir "data/output" -out_file "websearcher_output.txt"

#### to use default argument values

    python ./websearcher/search_web.py


# References

## Download web page containing HTML and Javascript

<http://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python>

<http://blog.databigbang.com/web-scraping-ajax-and-javascript-sites/>

<http://stackoverflow.com/questions/11804497/python-3-web-scraping-and-javascript-oh-my?rq=1>

## Google spell checker api

| free use is limited, then pay
| <https://code.google.com/archive/p/google-api-spelling-java/>

## Beautiful Soup

<https://www.crummy.com/software/BeautifulSoup/bs4/doc/>

<https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class>

<http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup>

## searcher
Python 3 project to search local file directories

<https://github.com/beepscore/searcher>

## Appendix Why use selenium?
Many web requests return a combination of HTML and Javascript.
In these cases, we can use a web browser to run the javascript and get more html.

Use selenium webdriver to load the page in a browser.
Have selenium wait until the browser executes the javascript and gets more html.
Then parse and search the page e.g. with Beautiful Soup.

<http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup>
<https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class>

## Appendix activate the project's virtual environment

Can use Anaconda or virtualenv.

### In terminal shell, cd to project root directory

    cd websearcher

### on macOS

Supply path to websearcher, e.g.

    source ./websearcher/venv/bin/activate

### on Windows

    venv\Scripts\activate


## Unit tests

| To run tests, open terminal shell.
| cd to project directory. Run tests via python command or bash script.

### Bash script

| Runs all test modules.
| Works on OS X. On Windows may work with Cygwin, I don't know.

    $ ./bin/run_tests

### python command

This command lists and tests all modules

    python3 -m unittest discover -s tests/

| Alternatively, can supply test module names as args.
| This command lists and tests all modules except
  web\_downloader\_arg\_reader and web\_searcher\_arg\_reader.

    python -m unittest tests.test_page_reader tests.test_file_writer tests.test_web_downloader tests.test_web_searcher

#### arg\_reader tests

| Attempting to run test\_web\_downloader\_arg\_reader and
  test\_web\_searcher\_arg\_reader has problem with arguments for
  unittest and for argparse.
| e.g. python -m unittest discover says "unrecognized arguments:
  discover" and wants the argparse arguments.
| TODO: Consider alternative solutions.
| <http://stackoverflow.com/questions/35270177/passing-arguments-for-argparse-with-unittest-discover>



use class\_ not Python keyword class

oovlist.csv

-----------

File from Windows had line endings that show as \^M in vim. Changed to
Unix line endings.
<http://stackoverflow.com/questions/811193/how-to-convert-the-m-linebreak-to-normal-linebreak-in-a-file-opened-in-vim>
at vim command line type as below, including \^V and \^M

    :%s/<Ctrl-V><Ctrl-M>/\r/g

### PyCharm

#### Python interpreter

#### Anaconda
Select within desired anaconda environment, e.g.

    > Python 3.6.1 (\~/anaconda/envs/beepscore/bin/python)

NOTE: On Windows, may need to click "eye" icon to show hidden files e.g.

    C:\Users\KLittle\AppData\Local\Continuum\anaconda3\envs
    
#### Poetry
If using Poetry, select within desired virtual environment, e.g.

    > ~/Library/Caches/pypoetry/virtualenvs/websearcher-NBsQj66t-py3.7/bin

select add content roots to python path select add source roots to python path

#### Working directory
can leave this blank

## Appendix Anaconda

### Activate anaconda environment

#### macOS {#macos-2}

    beepscore02:websearcher stevebaker$ conda activate beepscore

#### Windows

    C:\Users\KLittle\AppData\Local\Continuum\anaconda3\Scripts\activate my_env_name

Notice command prompt shows anaconda environment is active

    (beepscore) beepscore02:websearcher stevebaker$

    (beepscore) beepscore02:websearcher stevebaker$ which python
    /Users/stevebaker/anaconda/envs/beepscore/bin/python

    (beepscore) beepscore02:websearcher stevebaker$ python --version
    Python 3.6.2 :: Continuum Analytics, Inc.

### Deactivate conda environment

In shell run conda deactivate

    (beepscore) beepscore02:websearcher stevebaker$ conda deactivate

Appendix Poetry
---------------

<https://python-poetry.org/docs/basic-usage/>

### activate virtualenv

cd to virtual environment e.g.

> cd
> /Users/stevebaker/Library/Caches/pypoetry/virtualenvs/websearcher-NBsQj66t-py3.7/bin
> source activate

Notice command prompt shows virtual environment is active

> (websearcher-NBsQj66t-py3.7)

Appendix install selenium webdriver, geckodriver, chromedriver
--------------------------------------------------------------

### selenium webdriver

Selenium version 3 needs a driver to launch a browser.

#### Firefox geckodriver

<https://www.seleniumeasy.com/selenium-tutorials/launching-firefox-browser-with-geckodriver-selenium-3>
<https://github.com/mozilla/geckodriver>

##### macOS

install via homebrew

    brew install geckodriver

Then in python file browser = webdriver.Firefox()

2016-10-23 Firefox with current geckodriver works, but logs warning
'NoneType' object has no attribute 'path'

#### Chrome chromedriver

##### macOS {#macos-1}

install via homebrew

    brew install chromedriver

Then in python file browser = webdriver.Chrome()

2016-10-23 Chrome with chromedriver, log doesn't show a warning

##### Windows 10
https://stackoverflow.com/questions/38876281/anaconda-selenium-and-chrome

In terminal program "anaconda prompt" Activate desired conda environment
e.g.

    C:\Users\KLittle\AppData\Local\Continuum\anaconda3\Scripts\activate my_env_name

Then to install

    conda install -n my_env_name -c conda-forge python-chromedriver-binary
