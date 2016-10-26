#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def taw_html(search_string):
    """
    Use browser to search for a term
    wait for javascript to run and return html for id taw
    return empty string if browser doesn't suggest a spelling
    """
    # browser = webdriver.Chrome()
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
        outer_html = taw.get_attribute('outerHTML')
        return outer_html

    except TimeoutException:
        print("TimeoutException, returning empty string")
        return ""

    except AttributeError:
        # http://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occured#9824050
        print("AttributeError, returning empty string")
        return ""

    finally:
        browser.quit()
