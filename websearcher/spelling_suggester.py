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
        taw_html = self.taw_html(search_string)

        taw_soup = BeautifulSoup(taw_html, 'html.parser')

        spelling_showing_results_for = self.spelling_from_taw_showing_results_for(taw_soup)
        if spelling_showing_results_for != None:
            return spelling_showing_results_for

        else:
            return ""

    def taw_html(self, search_string):
        """
        Use browser to search for a term
        wait for javascript to run and return html for id taw
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
            WebDriverWait(browser, 6).until(lambda d: d.find_element_by_id("taw").is_displayed())
            taw = browser.find_element_by_id("taw")
            taw_html = taw.get_attribute('outerHTML')
            return taw_html

        except:
            #print("Didn't find element")
            return ""

        finally:
            browser.quit()


    def spelling_from_taw_showing_results_for(self, taw_soup):
        """
        Parse google search look for section "Showing results for"
        Example: search tuburculosis
        <p class="sp_cnt card-section">
        <span class="spell">Showing results for</span>
        <a class="spell" href="/search?/search?biw=1280&bih=423&q=tuberculosis&spell=1&sa=X&ved=0ahUKEwjMyeG30oPNAhVMz2MKHRw5D10QvwUIGSgA">
        <b>
        <i>tuberculosis</i>
        </b>
        </a>

        parameter taw_soup is beautiful soup object
        return string if found, else return None
        """

        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
        sp_cnt_card_section_list = taw_soup.select("p.sp_cnt.card-section")

        if len(sp_cnt_card_section_list) == 0:
            return None
        else:
            sp_cnt_card_section = sp_cnt_card_section_list[0]
            # print(sp_cnt_card_section.prettify())

            # e.g. <b><i>tuberculosis</i></b>
            spell_elem = sp_cnt_card_section.select("a.spell")[0]

            # e.g. tuberculosis
            return spell_elem.i.contents[0]

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
                if line != None and len(line.split(",")) > 1:
                    count = line.split(",")[1]

                print("searching " + search_string)
                search_result = self.suggested_spelling(search_string)
                search_result_line = search_string + "," + count + "," + search_result
                print("output line " + search_result_line)
                output_file.write(search_result_line + '\n')
                line_number += 1
