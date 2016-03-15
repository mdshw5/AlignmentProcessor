'''convertHeader.py will convert headers from alignment files downloaded from
UCSC into headers which are compliant with AlignmentProcessor.


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

def convertHeader(infile):
    # determine path to output file
    path = infile.split("/")[:-1]
    outpath = ""
    for i in path:
        outpath += i + "/"
    outfilename = outpath + "newHeader." + infile.split("/")[-1]
    with open(infile, "r") as fasta:
        with open(outfilename, "w") as output:
            for line in fasta:
                if line[0] == ">":
                    # Extract relevant data from original header
                    gene = ""
                    genebuild = line[1:].split()[0]
                    build = str(genebuild.split("_")[-1])
                    # Loop through gene ID incase it contains a "_"
                    for i in genebuild.split("_")[:-1]:
                        gene += i
                    # Write new header
                    output.write(">" + build + "." + gene + "\n")
                else:
                    output.write(line)          
            
def main():
    if argv[1] == "-h" or argv[1] == "--help":
        print("usage: convertHeader.py <path to input file>")
    else:
        infile = argv[1]
        convertHeader(infile)

if __name__ == "__main__":
    main()