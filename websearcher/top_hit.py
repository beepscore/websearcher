#!/usr/bin/env python3

from websearcher import top_hit_arg_reader
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

from bs4 import BeautifulSoup


class TopHit:
    """
    Use browser to search for strings and return top hit
    """
    def __init__(self, argfile):
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = top_hit_arg_reader.TopHitArgReader()
        self.args = self.arg_reader.args([argfile])
        self.in_dir = self.args.in_dir
        self.in_file = self.args.in_file
        self.out_dir = self.args.out_dir
        self.out_file = self.args.out_file

    def top_hit(self, search_string):
        """
        Use browser to search for a term and return top hit
        return empty string if browser doesn't suggest a spelling
        """
        st_html = self.st_html(search_string)

        st_soup = BeautifulSoup(st_html, 'html.parser')

        top_hit_for = self.top_hit_for(st_soup)
        if top_hit_for is not None:
            return top_hit_for

        return ""

    def st_html(self, search_string):
        """
        Use browser to search for a term
        wait for javascript to run and return html for id taw
        return empty string if browser doesn't suggest a spelling
        """
        browser = webdriver.Firefox()

        # google
        base_url = "https://www.google.com"
        query_prefix = "/#q="

        url = base_url + query_prefix + search_string
        browser.get(url)

        try:
            # http://stackoverflow.com/questions/37422832/waiting-for-a-page-to-load-in-selenium-firefox-w-python?lq=1
            # http://stackoverflow.com/questions/5868439/wait-for-page-load-in-selenium
            WebDriverWait(browser, 6).until(lambda d: d.find_element_by_class_name("st").is_displayed())
            st = browser.find_element_by_class_name("st")
            st_html = st.get_attribute('outerHTML')
            return st_html

        except:
            print("Didn't find element")
            return ""

        finally:
            browser.quit()

    def top_hit_for(self, st_soup):
        """
        Parse google search look for class "st"

        Example: search benaz

        parameter st_soup is beautiful soup object
        return string if found, else return None
        """

        if len(st_soup) == 0:
            return None
        else:
            return str(st_soup)

    def top_hits_from_file(self):
        """
        Use browser to search for strings and return suggested spellings
        return empty string if browser doesn't suggest a spelling
        """
        in_file_full_path = os.path.join(self.in_dir, self.in_file)
        out_file_full_path = os.path.join(self.out_dir, self.out_file)

        # Use "with" to attempt to avoid ResourceWarning about unclosed file.
        # "with" automatically closes file at end of block, even if exception was raised
        # http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python#6159912
        # https://www.python.org/dev/peps/pep-0343/
        # Unfortunately warning is still present. May be coming from somewhere else.

        with open(in_file_full_path, 'r') as input_file, open(out_file_full_path, 'w') as output_file:
            line_number = 1
            for line in input_file.readlines():
                print('input line ' + str(line_number) + ' ' + line)
                search_string = line.split(",")[0]

                count = ""
                if line is not None and len(line.split(",")) > 1:
                    count = line.split(",")[1]

                print("searching " + search_string)
                search_result = self.top_hit(search_string)
                search_result_line = search_string + "," + count + "," + search_result
                print("output line " + search_result_line)
                output_file.write(search_result_line + '\n')
                line_number += 1

