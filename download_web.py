#!/usr/bin/env python3

from websearcher import web_downloader

"""
Download urls in urls_file to out_directory. Use command line arguments.
"""

downloader = web_downloader.WebDownloader("@./data/input/web_downloader_args.txt")

print("Downloading to " + downloader.args.out_directory)
downloader.request_urls_write_to_files()
