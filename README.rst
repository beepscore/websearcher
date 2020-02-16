websearcher
===========

Purpose
=======

Python project to download web pages and search them.

Functionality
-------------

Get suggested spellings
~~~~~~~~~~~~~~~~~~~~~~~

Get top hits
~~~~~~~~~~~~

Concatenate regexes
~~~~~~~~~~~~~~~~~~~

Download web pages
~~~~~~~~~~~~~~~~~~

Unit tests
~~~~~~~~~~

Download pages 2 ways
---------------------

Download web page containing HTML, then search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download a list of web pages and store them locally. Then search them
for a regular expression. Storing pages enables searching multiple times
without re-downloading.

Download web page containing HTML and Javascript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many web requests return a combination of HTML and Javascript. Viewing
“page source” shows html and javascript, but not the result of running
the javascript.

For example, a google search.

::

       https://www.google.com/#q=pythan

Use selenium webdriver to load the page in a browser. Have selenium wait
until the browser executes the javascript and gets more html. Then parse
and search the page e.g. with Beautiful Soup.

References
==========

searcher Python 3
-----------------

https://github.com/beepscore/searcher

.. _download-web-page-containing-html-and-javascript-1:

Download web page containing HTML and Javascript
------------------------------------------------

http://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

http://blog.databigbang.com/web-scraping-ajax-and-javascript-sites/

http://stackoverflow.com/questions/11804497/python-3-web-scraping-and-javascript-oh-my?rq=1

selenium webdriver
~~~~~~~~~~~~~~~~~~

Selenium version 3 needs a driver to launch a browser.

Firefox geckodriver
^^^^^^^^^^^^^^^^^^^

https://www.seleniumeasy.com/selenium-tutorials/launching-firefox-browser-with-geckodriver-selenium-3
https://github.com/mozilla/geckodriver

macOS
'''''

install via homebrew

::

   brew install geckodriver

Then in python file browser = webdriver.Firefox()

2016-10-23 Firefox with current geckodriver works, but logs warning
‘NoneType’ object has no attribute ‘path’

Chrome chromedriver
^^^^^^^^^^^^^^^^^^^

.. _macos-1:

macOS
'''''

install via homebrew

::

   brew install chromedriver

Then in python file browser = webdriver.Chrome()

2016-10-23 Chrome with chromedriver, log doesn’t show a warning

Windows 10
''''''''''

In Anaconda navigator searched for chromedriver, found one at
clinicalgraphics.

In terminal program “anaconda prompt” Activate desired conda environment
e.g.

::

   C:\Users\KLittle\AppData\Local\Continuum\anaconda3\Scripts\activate LingProg

Then to install

::

   conda install -c clinicalgraphics selenium-chromedriver

Google spell checker api
^^^^^^^^^^^^^^^^^^^^^^^^

| free use is limited, then pay
| https://code.google.com/archive/p/google-api-spelling-java/

Beautiful Soup
--------------

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class

http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup

Python modules and packages
---------------------------

http://www.dabeaz.com/modulepackage/ModulePackage.pdf

https://www.youtube.com/watch?v=0oTh1CXRaQ0

Results
=======

activate the project’s virtual environment
------------------------------------------

For more info about venv see Appendix.

In terminal shell, cd to project root directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   cd websearcher

on macOS
~~~~~~~~

Supply path to websearcher, e.g.

::

   source ./websearcher/venv/bin/activate

on Windows
~~~~~~~~~~

::

   venv\Scripts\activate

.. _get-suggested-spellings-1:

Get suggested spellings
-----------------------

Don’t commit actual input file. In .gitignore ignored oovwords.csv

::

   python3 -m get_suggested_spellings -in_dir "data/input" -in_file "oovwords.csv" -out_dir "data/output" -out_file "suggested_spelling_output.csv"

to use default argument values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   python3 -m get_suggested_spellings

.. _get-top-hits-1:

Get top hits
------------

::

   python3 -m get_top_hits

.. _concatenate-regexes-1:

Concatenate regexes
-------------------

::

   python3 -m concatenate_regex

.. _download-web-pages-1:

Download web pages
------------------

::

   python3 -m download_web

Search files and write search output to file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search is similar to Unix/Linux grep command

specify argument values
^^^^^^^^^^^^^^^^^^^^^^^

Note: Suggest use different values for download_directory and output
file directory.

Otherwise subsequent searches might accidentally search an output file.

::

   python3 -m search_web -expression "ython" -search_directory "data/downloads" -out_dir "data/output" -out_file "websearcher_output.txt"

.. _to-use-default-argument-values-1:

to use default argument values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   python ./websearcher/search_web.py

.. _unit-tests-1:

Unit tests
----------

| To run tests, open terminal shell.
| cd to project directory. Run tests via python command or bash script.

Bash script
~~~~~~~~~~~

| Runs all test modules.
| Works on OS X. On Windows may work with Cygwin, I don’t know.

::

   $ ./bin/run_tests

python command
~~~~~~~~~~~~~~

This command lists and tests all modules

::

   python3 -m unittest discover -s tests/

| Alternatively, can supply test module names as args.
| This command lists and tests all modules except
  web_downloader_arg_reader and web_searcher_arg_reader.

::

   python -m unittest tests.test_page_reader tests.test_file_writer tests.test_web_downloader tests.test_web_searcher

arg_reader tests
^^^^^^^^^^^^^^^^

| Attempting to run test_web_downloader_arg_reader and
  test_web_searcher_arg_reader has problem with arguments for unittest
  and for argparse.
| e.g. python -m unittest discover says “unrecognized arguments:
  discover” and wants the argparse arguments.
| TODO: Consider alternative solutions.
| http://stackoverflow.com/questions/35270177/passing-arguments-for-argparse-with-unittest-discover

--------------

Appendix Download web page containing HTML and Javascript
---------------------------------------------------------

Many web requests return a combination of HTML and Javascript. For
example, a google search.

::

       https://www.google.com/#q=javascwipt

In these cases, we can use a web browser to run the javascript and get
more html.

http://stackoverflow.com/questions/11331071/get-class-name-and-contents-using-beautiful-soup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class

use class\_ not Python keyword class

oovlist.csv
-----------

File from Windows had line endings that show as ^M in vim. Changed to
Unix line endings.
http://stackoverflow.com/questions/811193/how-to-convert-the-m-linebreak-to-normal-linebreak-in-a-file-opened-in-vim
at vim command line type as below, including ^V and ^M

::

   :%s/<Ctrl-V><Ctrl-M>/\r/g

PyCharm test configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.idea files aren’t in source control, so describe configuration setup
here. Add from Defaults/Python tests/unittests

Target / Path
^^^^^^^^^^^^^

::

   tests/

pattern
^^^^^^^

can leave this blank

Python interpreter
^^^^^^^^^^^^^^^^^^

Python 3.6.1 (~/anaconda/envs/beepscore/bin/python)

select add content roots to python path select add source roots to
python path

Working directory
^^^^^^^^^^^^^^^^^

can leave this blank

Appendix Anaconda
-----------------

The project uses an Anaconda environment.

Activate anaconda environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _macos-2:

macos
^^^^^

::

   beepscore02:websearcher stevebaker$ conda activate beepscore

windows
^^^^^^^

::

   C:\Users\KLittle\AppData\Local\Continuum\anaconda3\Scripts\activate LingProg

Notice command prompt shows anaconda environment is active

::

   (beepscore) beepscore02:websearcher stevebaker$

   (beepscore) beepscore02:websearcher stevebaker$ which python
   /Users/stevebaker/anaconda/envs/beepscore/bin/python

   (beepscore) beepscore02:websearcher stevebaker$ python --version
   Python 3.6.2 :: Continuum Analytics, Inc.

Deactivate conda environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In shell run conda deactivate

::

   (beepscore) beepscore02:websearcher stevebaker$ conda deactivate
