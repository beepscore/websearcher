#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup


class TopHit:
    """
    Use browser to search for strings and return top hit
    """

    @staticmethod
    def top_hit(search_string):
        """
        Use browser to search for a term and return top hit
        return empty string if browser doesn't suggest a spelling
        """
        st_html = TopHit.st_html(search_string)

        st_parsed = TopHit.st_parsed(st_html)
        return st_parsed

    @staticmethod
    def st_html(search_string):
        """
        Use browser to search for a term
        wait for javascript to run and return html for class "st"
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
            st_html = st.get_attribute('innerHTML')
            return st_html

        except:
            print("Didn't find element")
            return ""

        finally:
            browser.quit()

    @staticmethod
    def st_parsed(st_html):
        """
        strip tags from st_html and return a string
        """
        st_soup = BeautifulSoup(st_html, 'html.parser')
        # strip tags like <em>
        text = st_soup.get_text()
        text_no_ellipsis = text.replace('...', '')
        return text_no_ellipsis
