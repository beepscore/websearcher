#!/usr/bin/env python3

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
    def search_directory_write_results(expression, search_dir, out_dir, out_file):
        files_containing_expression = WebSearcher.search_directory(expression, search_dir)
        # convert list to string with line separator
        files_string = (os.linesep).join(files_containing_expression)
        file_writer.FileWriter.create_file(out_dir, out_file, files_string)

    @staticmethod
    def search_directory(expression, search_dir):
        """
        In directory search every file for expression
        return file names containing expression
        """
        files_containing_expression = []
        for file_name in os.listdir(search_dir):
            file_name_containing_expression = WebSearcher.search_file(expression, search_dir, file_name)
            if file_name_containing_expression is not None:
                files_containing_expression.append(file_name_containing_expression)
        return files_containing_expression

    @staticmethod
    def search_file(expression, search_dir, file_name):
        if file_name == ".DS_Store":
            # avoid read error
            return None
        else:
            file_path = file_writer.FileWriter.absolute_file_path(search_dir, file_name)
            textfile = open(file_path, 'r')
            text = textfile.read()
            textfile.close()
            matches = re.findall(expression, text)
            if matches == []:
                return None
            else:
                return file_name

