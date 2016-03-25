'''This program will run CodeML on a directory of single gene alignments.


    Copyright 2016 by Shawn Rupp'''

from sys import argv
from glob import glob
from subprocess import Popen
from shlex import split
import os

def runCodeML(ctl, path):
    # Open all input files in the directory
    inpath = path + "06_phylipFiles/" + "*.phylip"   
    files = glob(inpath)   
    for file in files:
        filename = file.split("/")[-1]
        outfile = path + "07_codeml/" + filename.split(".")[0]
        tempctl = path + "07_codeml/tmp.ctl"
        with open(ctl, "r") as control:
            with open(tempctl, "w") as temp:
                for line in control:
                    if "seqfile" in line:
                        temp.write("\tseqfile = " + file + "\n")
                    elif "outfile" in line:
                        temp.write("\toutfile = " + outfile + ".mlc\n")
                    else:
                        temp.write(line)
        cm = Popen(split("./bin/paml/bin/codeml " + tempctl))
        cm.wait()
        os.remove(tempctl)

def main():
    if argv[1] == "-h" or argv[1] == "--help":
        print("Usage: python 07_CodeMLonDir.py <path to codeml control file> \
<path to input and output directories>")
        quit()
    else:
        ctl = argv[1]
        path = argv[2]
        # Set directory names and add a trailing "/" if necessary
        if path[-1] != "/":
            path += "/"
        runCodeML(ctl,path)

if __name__ == "__main__":
    main()
