#!/usr/bin/env python3

import requests
from selenium import webdriver
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

    def class_name_from_html(self, html_doc, class_name):
        """
        Parse html for class_name
        """
        soup = BeautifulSoup(html_doc, 'html.parser')

        result = soup.prettify()

        # http://stackoverflow.com/questions/17154427/how-to-getelementsbyclassname-by-using-python-xml-dom-minidom
        # Use class_ not Python keyword class
        # result = soup.find_all("a", class_=class_name)
        # result = soup.find_all(class_=class_name)
        # result = soup.find('a', attrs={'class' : 'spell'})

        # for duckduckgo
        # need to look in javascript "data", "Heading" to find astma changed to Asthma
        #result = soup.find_all("a", class_=class_name)

        print(result)
        return result

    def spell_from_url(self, url):
        """
        Request web page at url, return links whose class matches "spell"
        """
        #response = self.response(url)
        # html_doc = response.text
        # return self.class_name_from_html(html_doc, "spell")

        browser = webdriver.Firefox()
        browser.get(url)
        try:
            elem = browser.find_element_by_class_name("spell")
            print('Found <%s> element with that class name' % (elem.tag_name))
        except:
            print("Didn't find element")

