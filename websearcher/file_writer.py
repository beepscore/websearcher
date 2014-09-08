#!/usr/bin/env python3

import os


class FileWriter():
    '''
    Writes file to path.
    Path includes directory name and file name.
    Creates directory if it doesn't exist.
    '''

    @staticmethod
    def absolute_dir_path(dirname):
        # Note Python does not expand ~ in path as on OS X
        # http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        # current_dir is absolute path
        # current_dir = os.path.dirname(__file__)
        absolute_path = os.path.abspath(dirname)
        return absolute_path

    @staticmethod
    def absolute_file_path(dirname, filename):
        absolute_dir_path = FileWriter.absolute_dir_path(dirname)
        absolute_file_path = os.path.join(absolute_dir_path, filename)
        return absolute_file_path

    @staticmethod
    def create_directory(dirname):
        '''
        Creates directory at dirname if it doesn't exist.
        '''
        abs_dir_path = FileWriter.absolute_dir_path(dirname)
        # http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary
        try:
            os.makedirs(abs_dir_path)
        except OSError:
            if not os.path.isdir(abs_dir_path):
                raise

    def __init__(self, dirname, filename, content):
        self.filename = filename
        self.dirname = dirname
        self.content = content

    def create_file(self, dirname, filename, content):
        '''
        Creates file at path and writes content
        '''
        abs_file_path = FileWriter.absolute_file_path(dirname, filename)
        self.create_directory(dirname)
        # https://docs.python.org/3.3/tutorial/inputoutput.html
        f = open(abs_file_path, 'w')
        f.write(content)
        f.close()
