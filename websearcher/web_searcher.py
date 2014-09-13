#!/usr/bin/env python3

from websearcher import arg_reader
from websearcher import page_reader
from websearcher import file_writer
import re
import os


class WebSearcher():
    '''
    Controller composed of several objects.
    Reads input commands.
    Requests a series of web pages.
    Writes response to a file.
    Searches file for expression.
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    '''

    @staticmethod
    def url_for_page_number(filename_start, page_number, filename_end):
        if page_number <= 0:
            return "{0}{1}".format(filename_start, filename_end)
        else:
            return "{0}{1}{2}".format(filename_start, 25 * (page_number - 1), filename_end)

    @staticmethod
    def file_name_for_page_number(filename_start, page_number, filename_end):
        if page_number <= 0:
            return "{0}{1}".format(filename_start, filename_end)
        else:
            return "{0}{1}{2}".format(filename_start, page_number, filename_end)

    @staticmethod
    def search_directory(expression, dir_name):
        files_containing_expression = []
        for file_name in os.listdir(dir_name):
            file_name_containing_expression = WebSearcher.search_file(expression, dir_name, file_name)
            if file_name_containing_expression != None:
                files_containing_expression.append(file_name_containing_expression)
        return files_containing_expression

    @staticmethod
    def search_file(expression, dir_name, file_name):
        if file_name == ".DS_Store":
            # avoid read error
            return None
        else:
            file_path = file_writer.FileWriter.absolute_file_path(dir_name, file_name)
            textfile = open(file_path, 'r')
            text = textfile.read()
            textfile.close()
            matches = re.findall(expression, text)
            if matches == []:
                return None
            else:
                return file_name

    def __init__(self, argfile):
        '''
        Don't version control argfile
        Put it outside project directory
        '''
        self.arg_reader = arg_reader.ArgReader()
        self.args = self.arg_reader.args([argfile])
        self.page_reader = page_reader.PageReader()

    def request_page_write_response(self, url, out_file):
        response = self.page_reader.response(url)

        writer = file_writer.FileWriter(self.args.out_directory, out_file, response.text)
        writer.create_file(writer.dirname, writer.filename, writer.content)

    def request_pages_write_responses(self):
        # range function excludes end, so add 1

        page_range = range(int(self.args.item_start), int(self.args.item_end) + 1)
        for page_number in page_range:
            url = WebSearcher.url_for_page_number(self.args.url_start, page_number, self.args.url_end)
            out_file = WebSearcher.file_name_for_page_number("junk", page_number, ".html")
            self.request_page_write_response(url, out_file)

