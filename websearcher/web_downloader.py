#!/usr/bin/env python3

from websearcher import arg_reader
from websearcher import page_reader
from websearcher import file_writer


class WebDownloader:
    """
    Controller composed of several objects.
    Reads input commands.
    Requests a list of web pages and writes each one to a file.
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    """

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
