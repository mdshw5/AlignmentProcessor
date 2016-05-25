'''This program will read through a directory that contains 
    aligned multiple FASTA files and remove the NM identifier 
    (FASTA header) and all the trailing information (end lines)
    for each gene. It will also change all the 
    genome-build-names to common names.


    Copyright 2016 by Shawn Rupp'''

from sys import argv
from glob import glob

def removeHeader(path, commonNames):
    # Open all input files in the directory
    inpath = path + "01_splitFastaFiles/" + "*.fa"   
    files = glob(inpath)   
    for file in files:
        with open(file, "r") as infile:
            filename = file.split("/")[-1]
            # Create output file
            outfile = (path + "02_rmHeader/" + filename.split(".")[0] +
                       "." + filename.split(".")[1] + ".rmHeader")
            with open(outfile, "w") as output:
                for line in infile:
                    if line[0] == ">":
			# Split header to get build name and remove extra info
                        header = line.split(".")
                        # Replace build name with common name
                        if commonNames == True:
                            name = changeNames(header[0])
                        elif commonNames == False:
                            name = header[0][1:]
			# Write common name to file
                        output.write(">" + str(name) + "\n")
                    else:
			# Write sequence to file in all caps
                        output.write(line.upper())

def changeNames(header):
    # Remove leading ">" from header to get the build name
    build = header[1:]
    speciesDict = {}
    with open("bin/02_nameList.txt", "r") as nameList:
        # Create dictionary of species names from file
        for line in nameList:
            try:
                speciesDict[line.split("\t")[0]] = line.split()[1].rstrip()
            except IndexError:
                # Skip lines which are not formatted properly or are empty
                pass
    # Compare the build name against the species dictionary. If it is matched
    # to a key, return the value (the common name).
        if build in speciesDict:
            name = speciesDict[build]
            return name

def main():
    if argv[1] == "-h" or argv[1] == "--help":
        print("Usage: python 02_RemoveHeader.py \
<path to inut and output directories>")
        quit()
    else:
        commonNames = False
        # Set directory names and add a trailing "/" if necessary
        path = argv[1]
        try:
            if argv[2] == "--changeNames":
                commonNames = True
        except IndexError:
            pass
        removeHeader(path, commonNames)

if __name__ == "__main__":
    main()
