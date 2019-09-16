#!/usr/bin/env python3
"""
A script to split csv files into a printable txt file
"""

import sys, os

def get_info(file, out):
    """
    A method to split and write the contents of file to out
    """
    in_file = open(file, 'r+', encoding='iso8859')
    res_file = open(out, 'a+')

    for line in in_file:
        splits = line.split(',')
        res_file.write('\tlabomep.sesamath.net\n')
        res_file.write(f"{splits[0]} {splits[1]}, {splits[2]}\n")
        res_file.write(f"Identifiant : {splits[4]}\t Mot de passe : {splits[5]}\n")

    in_file.close()
    res_file.close()

def main():
    """
    The main function that calls get_info() on every command line argument
    """
    outfile = 'result.txt'

    if os.path.exists(outfile):
        os.remove(outfile)

    for arg in sys.argv[1:]:
        get_info(arg, outfile)

if __name__ == "__main__":
    main()
