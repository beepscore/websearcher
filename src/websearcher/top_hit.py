#!/usr/bin/env python3

from bs4 import BeautifulSoup
from websearcher import browser_driver


def top_hit(search_string):
    """
    Use browser to search for a term and return top hit
    return empty string if browser doesn't suggest a spelling
    """
    html = browser_driver.st_html(search_string)

    parsed = parsed_text(html)
    return parsed


def parsed_text(html):
    """
    return html text, stripped of tags and ellipses '...'
    """
    soup = BeautifulSoup(html, 'html.parser')
    # strip tags like <em>
    text = soup.get_text()
    text_no_ellipsis = text.replace('...', '')
    return text_no_ellipsis
