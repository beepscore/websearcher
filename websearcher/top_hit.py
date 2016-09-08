#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup


def top_hit(search_string):
    """
    Use browser to search for a term and return top hit
    return empty string if browser doesn't suggest a spelling
    """
    html = st_html(search_string)

    parsed = parsed_text(html)
    return parsed


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
        inner_html = st.get_attribute('innerHTML')
        return inner_html

    except:
        print("Didn't find element")
        return ""

    finally:
        browser.quit()


def parsed_text(html):
    """
    return html text, stripped of tags and ellipses '...'
    """
    soup = BeautifulSoup(html, 'html.parser')
    # strip tags like <em>
    text = soup.get_text()
    text_no_ellipsis = text.replace('...', '')
    return text_no_ellipsis
