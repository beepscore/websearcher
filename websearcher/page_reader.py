#!/usr/bin/env python3

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

class PageReader:
    """
    Requests a url and returns the response or response properties.
    """

    def __init__(self):
        pass

    def response(self, url):
        """
        Request web page at url, return response
        Then caller can read response.status_code, response.text
        """
        # http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
        response = requests.get(url)
        # response = requests.post(url=url, data=body, headers={'Connection':'close'})
        # http://stackoverflow.com/questions/10115126/python-requests-close-http-connection?rq=1
        response.connection.close()

        return response

    def suggested_spelling(self, search_string):
        """
        Use browser to search for a term and return suggested spelling
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

        # http://stackoverflow.com/questions/37422832/waiting-for-a-page-to-load-in-selenium-firefox-w-python?lq=1
        # http://stackoverflow.com/questions/5868439/wait-for-page-load-in-selenium
        WebDriverWait(browser, 10).until(lambda d: d.find_element_by_class_name("spell").is_displayed())

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
        browser.quit()

        soup = BeautifulSoup(spell_link_text, 'html.parser')
        # e.g. asthma
        return soup.i.contents[0]

"""
        try:
            # taw_elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "taw")))
            # spell_elems = browser.find_elements_by_class_name("spell")
            # print("len(spell_elems) == {0}".format(len(spell_elems)))

            try:
                #spell_elem = browser.find_element_by_class_name("spell")
                print("Found element with class name spell, tag_name {0}".format(spell_elem.tag_name))
                print("spell_elem.tag_name == {0}".format(spell_elem.tag_name))
            except:
                #print("Didn't find element")
                pass

        finally:
            browser.quit()
            spell_elem = spell_elems[1]
            return spell_elem
"""

