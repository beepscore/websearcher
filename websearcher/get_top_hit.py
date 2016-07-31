#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import top_hit

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Search words in input file. Use command line arguments.
    """

    top_hit = top_hit.TopHit("@./websearcher_data/inputs/top_hit_args.txt")

    actual = top_hit.top_hits_from_file()
    print("results")
    print('\n'.join(actual))

