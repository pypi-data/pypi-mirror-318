# -*- coding: utf-8 -*-
"""
Created on Thu Jan 2 10:08:22 2025

@author: Maria Marta Zanardi
"""

import DP4plus_solv 
import sys
      
main() 


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")


    DP4plus_solv.main()
    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do. Return values are exit codes.


if __name__ == "__main__":
    sys.exit(main())