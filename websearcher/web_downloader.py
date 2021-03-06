#!/usr/bin/env python3

from websearcher import web_downloader_arg_reader
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
        self.arg_reader = web_downloader_arg_reader.WebDownloaderArgReader()
        self.args = self.arg_reader.args([argfile])
        self.urls_file = self.args.urls_file

    def urls_from_urls_file(self, urls_file):
        # http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array#3277516
        textfile = open(urls_file, 'r')
        # remove newline at end of line
        urls_list = [line.rstrip('\n') for line in textfile]
        textfile.close()
        return urls_list

    def request_url_write_to_out_file(self, url, out_file):
        """
        Request url and write response.

        :param url: url to request
        :param out_file: filename to write response to
        :return: None
        """
        response = page_reader.response(url)

        file_writer.create_file(self.args.out_directory, out_file, response.text)

    def request_url_write_to_file(self, url):
        """
        Request url, write response to file name based on filename_from_url.

        :param url: url to request
        :return: None
        """
        out_file = file_writer.filename_from_url(url)
        self.request_url_write_to_out_file(url, out_file)

    def request_urls_write_to_files(self):
        urls = self.urls_from_urls_file(self.urls_file)
        for url in urls:
            self.request_url_write_to_file(url)
