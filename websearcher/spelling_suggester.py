#!/usr/bin/env python3

from websearcher import spelling_suggester_arg_reader
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

from bs4 import BeautifulSoup

class SpellingSuggester:
    """
    Use browser to search for strings and return suggested spellings
    """

    def __init__(self, argfile):
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = spelling_suggester_arg_reader.SpellingSuggesterArgReader()
        self.args = self.arg_reader.args([argfile])
        self.in_dir = self.args.in_dir
        self.in_file = self.args.in_file
        self.out_dir = self.args.out_dir
        self.out_file = self.args.out_file

    def suggested_spelling(self, search_string):
        """
        Use browser to search for a term and return suggested spelling
        return empty string if browser doesn't suggest a spelling
        """
        browser = webdriver.Firefox()

        # duckduckgo
        # base_url = "https://www.duckduckgo.com"
        # query_prefix = "/?q="

        # google
        base_url = "https://www.google.com"
        query_prefix = "/#q="

        url = base_url + query_prefix + search_string
        browser.get(url)

        try:
            # http://stackoverflow.com/questions/37422832/waiting-for-a-page-to-load-in-selenium-firefox-w-python?lq=1
            # http://stackoverflow.com/questions/5868439/wait-for-page-load-in-selenium
            WebDriverWait(browser, 6).until(lambda d: d.find_element_by_class_name("spell").is_displayed())

            # example google search html
            # <p class="sp_cnt card-section">
            # <span class="spell">Showing results for</span>
            # <a class="spell" href="/search?/search?biw=1280&bih=423&q=tuberculosis&spell=1&sa=X&ved=0ahUKEwjMyeG30oPNAhVMz2MKHRw5D10QvwUIGSgA">
            # <b>
            # <i>tuberculosis</i>
            # </b>
            # </a>

            # use find_element_by_css_selector to match compound class (2 classes)
            # http://stackoverflow.com/questions/17808521/how-to-avoid-compound-class-name-error-in-page-object
            sp_cnt_card_section = browser.find_element_by_css_selector(".sp_cnt.card-section")

            spell_elems = sp_cnt_card_section.find_elements_by_class_name("spell")
            spell_elem = None
            # probably there is a more succint way to do this!
            for elem in spell_elems:
                if elem.tag_name == "a":
                    spell_elem = elem

            # e.g. <b><i>asthma</i></b>
            spell_link_text = spell_elem.get_attribute('innerHTML')

            soup = BeautifulSoup(spell_link_text, 'html.parser')
            # e.g. asthma
            return soup.i.contents[0]

        except:
            #print("Didn't find element")
            return ""

        finally:
            browser.quit()

    def suggested_spellings(self, search_strings):
        """
        Use browser to search for strings and return suggested spellings
        return empty string if browser doesn't suggest a spelling
        """
        results = []
        for search_string in search_strings:
            results.append(self.suggested_spelling(search_string))
        return results

    def suggested_spellings_from_file(self):
        """
        Use browser to search for strings and return suggested spellings
        return empty string if browser doesn't suggest a spelling
        """
        in_file_full_path = os.path.join(self.in_dir, self.in_file)
        input_file = open(in_file_full_path, 'r')
        results = []
        for line in input_file.readlines():
            search_string = line.split(",")[0]
            print("search_string: " + search_string)
            # results.append(self.suggested_spelling(search_string))
        input_file.close()
        return results