#!/usr/bin/env python3

import unittest
import os

# tried putting tests in a "test" directory at same level as websearcher
# relative import didn't work
from websearcher import file_writer


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        pass


    def test_filename_from_url_root(self):
        actual = file_writer.FileWriter.filename_from_url("http://www.beepscore.com")
        expected = "httpwww.beepscore.com"
        self.assertEqual(expected, actual)

    def test_filename_from_url(self):
        actual = file_writer.FileWriter.filename_from_url("http://beepscore.com/hubcape/")
        expected = "httpbeepscore.comhubcape"
        self.assertEqual(expected, actual)

    # This test is not ideal because it depends upon developer machine
    def test_absolute_dir_path(self):
        test_dirname = "../junk"
        actual = file_writer.FileWriter.absolute_dir_path(test_dirname)
        self.assertEqual('/Users/stevebaker/Documents/projects/pythonProjects/junk',
                         actual, '')

    # This test is not ideal because it depends upon developer machine
    def test_absolute_file_path(self):
        test_dirname = "../junk"
        test_filename = "foo.html"
        actual = file_writer.FileWriter.absolute_file_path(test_dirname, test_filename)
        self.assertEqual('/Users/stevebaker/Documents/projects/pythonProjects/junk/foo.html',
                         actual, '')

    def test_create_directory(self):
        test_dirname = "../junk"
        file_writer.FileWriter.create_directory(test_dirname)
        self.assertTrue(os.path.isdir(test_dirname), '')

    def test_init(self):
        test_dirname = "../junk"
        test_filename = "foo.html"
        test_content = "junk_text"
        writer = file_writer.FileWriter(test_dirname, test_filename, test_content)
        self.assertEqual(test_dirname, writer.dirname, '')
        self.assertEqual(test_filename, writer.filename, '')
        self.assertEqual(test_content, writer.content, '')

    def test_create_file(self):
        test_dirname = "../junk"
        test_filename = "foo.html"
        test_content = "junk_text"
        writer = file_writer.FileWriter(test_dirname, test_filename, test_content)

        writer.create_file(writer.dirname, writer.filename, writer.content)

        actual = file_writer.FileWriter.absolute_file_path(test_dirname, test_filename)
        self.assertTrue(os.path.isfile(actual), '')

if __name__ == "__main__":
    unittest.main()
