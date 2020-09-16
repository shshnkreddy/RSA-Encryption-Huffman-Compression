import sys
import os
import pickle
from Tree import *
from bstring import binaryList, genBinString, genFile 

if __name__ == '__main__':
    
    if(len(sys.argv) < 2):
        print "Enter file name to be decompressed!"
        sys.exit()
    
    if(os.path.exists(sys.argv[1])):
            with open(sys.argv[1], 'rb') as f1:
                binstrlen = pickle.load(f1)
                convdict = pickle.load(f1)
                restOfInput = f1.read()
    else:
        print "File doesn't exist!"
        sys.exit()
     
    
    #Generating list of numbers from each byte
    blist = binaryList(restOfInput)

    #Generating binary string from list of numbers
    binstr = genBinString(blist, binstrlen)
    

    outfile = genFile(binstr, convdict)

    
    with open(sys.argv[1][:-4], 'w') as f2:
        f2.write(outfile)
        os.remove(sys.argv[1])
