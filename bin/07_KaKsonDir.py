'''This program will run KaKs_Calculator on a directory. Must be in the 
AlignmentProcessor directory to run.


    AlignmentProcessor0.6 Copyright 2016 by Shawn Rupp

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License (GPL3.txt) for more details.'''

from sys import argv
from subprocess import Popen
from shlex import split
from glob import glob
import os

def calculateKaKs(path):
    '''Calculates substition rates.'''
    print("Calculating Ka/Ks values...")
    inpath = path + "06_axtFiles/" + "*.axt"
    files = glob(inpath)
    for file in files:
        with open(file, "r") as infile:
            filename = file.split("/")[-1]
            # Create output file
            outfile = (path + "KaKsOutput/" + filename.split(".")[0]
                       + ".kaks")
            ck = Popen(split("bin/KaKs_Calculator -i " + file + " -o " +
                             outfile + " -m NG"))
            ck.wait()

def main():
    if argv[1] == "-h" or argv[1] == "--help":
        print("Usage: python 07_KaKsonDirectory.py \
<path to inut and output directories> <name of refernce species>")
        quit()
    else:
        path = argv[1]
        calculateKaKs(path)

if __name__ == "__main__":
    main()