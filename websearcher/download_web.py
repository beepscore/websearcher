#!/usr/bin/env python

# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import web_downloader

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Download urls in urls_file to out_directory. Use command line arguments.
    """

    downloader = web_downloader.WebDownloader("@./websearcher_data/inputs/web_downloader_args.txt")

    print("Downloading to " + downloader.args.out_directory)
    downloader.request_urls_write_to_files()

