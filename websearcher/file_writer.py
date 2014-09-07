#!/usr/bin/env python3

import os

class FileWriter():
    '''
    Creates directory if it doesn't exist.
    Writes file to directory.
    '''

    def __init__(self, path, filename, content):
        self.path = path
        self.filename = filename
        self.content = content

    def create_directory(self, path):
        '''
        Creates directory at path if it doesn't exist.
        '''
        # http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise
