#!/usr/bin/env python3

#from websearcher import spelling_suggester_arg_reader
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

from bs4 import BeautifulSoup

class TopHit:
    """
    Use browser to search for strings and return top hit
    """

    def __init__(self):
        """
        Initialize the class.

        :return: None
        """
        self.out_dir = 'websearcher_data/results'
        self.out_file = 'oovinforesults.txt'

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

        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
        #sp_cnt_card_section_list = taw_soup.select("p.sp_cnt.card-section")

        if len(st_soup) == 0:
            return None
        else:
            print(st_soup.prettify())

