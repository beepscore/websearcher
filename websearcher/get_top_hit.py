#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'websearcher')))

from websearcher import top_hit

# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':

    """
    Search word
    """

    top_hit = top_hit.TopHit()
    actual = top_hit.top_hit('semitendinosus')
    print("results")
    print(actual)
    print('\n'.join(actual))
