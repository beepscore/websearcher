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
