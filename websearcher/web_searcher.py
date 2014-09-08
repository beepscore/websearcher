#!/usr/bin/env python3

from websearcher import arg_reader
from websearcher import page_reader
from websearcher import file_writer


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

    def __init__(self, argfile):
        '''
        Don't version control argfile
        Put it outside project directory
        '''
        self.arg_reader = arg_reader.ArgReader()
        self.args = self.arg_reader.args([argfile])
        self.page_reader = page_reader.PageReader()

    def request_page_write_response(self):
        response = self.page_reader.response(self.args.url_start)

        writer = file_writer.FileWriter(self.args.out_directory, self.args.out_file, response.text)
        writer.create_file(writer.dirname, writer.filename, writer.content)
