'''compileKaKs will concatenate the output files of KaKs_Calculator into
a single tsv file.


    Copyright 2016 by Shawn Rupp'''

from sys import argv
from glob import glob

def compileKsKs(path):
    '''Prints Ka/Ks output as a single tsv file.'''
    # Set counter so the header is only printed once
    count =  0
    inpath = path + "07_KaKsOutput/" + "*.kaks"
    files = glob(inpath)
    outfile = path + "KaKs.tsv"
    # Open input and output files
    with open(outfile, "w") as output:
        for file in files:
            with open(file, "r") as infile:
                filename = file.split("/")[-1]
                for line in infile:
                    if count == 0:
                        #Print header from first file
                        output.write("GeneID\t" + line)
                        count += 1
                    else:
                        # Print data from remaining files
                        if line.split("\t")[0] == "Sequence":
                            pass
                        else:
                            output.write(filename.split(".")[0] + "\t" + line)
                    
def main():
    if argv[1] == "-h" or argv[1] == "--help":
        print("Usage: python 08_compileKaKs.py \
<path to inut and output directories>")
        quit()
    else:
        path = argv[1]
        compileKsKs(path)

if __name__ == "__main__":
    main()
