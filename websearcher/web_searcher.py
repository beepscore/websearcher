#!/usr/bin/env python3

from websearcher import arg_reader
from websearcher import page_reader
from websearcher import file_writer
import re
import os


class WebSearcher:
    """
    Controller composed of several objects.
    Reads input commands.
    Searches files for expression.
    """

    @staticmethod
    def search_directory(expression, dir_name):
        """
        In directory search every file for expression
        return file names containing expression
        """
        files_containing_expression = []
        for file_name in os.listdir(dir_name):
            file_name_containing_expression = WebSearcher.search_file(expression, dir_name, file_name)
            if file_name_containing_expression is not None:
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
        """
        Initialize the class.

        :param argfile: file with arguments. Don't version control argfile. Put it outside project directory.
        :return: None
        """
        self.arg_reader = arg_reader.ArgReader()
        self.args = self.arg_reader.args([argfile])
        self.page_reader = page_reader.PageReader()

    def request_url_write_to_out_file(self, url, out_file):
        """
        Request url and write response.

        :param url: url to request
        :param out_file: filename to write response to
        :return: None
        """
        response = self.page_reader.response(url)

        writer = file_writer.FileWriter(self.args.out_directory, out_file, response.text)
        writer.create_file(writer.dirname, writer.filename, writer.content)

    def request_url_write_to_file(self, url):
        """
        Request url, write response to file name based on filename_from_url.

        :param url: url to request
        :return: None
        """
        out_file = file_writer.FileWriter.filename_from_url(url)
        self.request_url_write_to_out_file(url, out_file)

    def request_urls_write_to_files(self, urls):
        for url in urls:
            self.request_url_write_to_file(url)

    def request_urls_write_to_files_search_responses(self, urls):
        self.request_urls_write_to_files(urls)
        file_names = WebSearcher.search_directory(self.args.expression, self.args.out_directory)
        return file_names
