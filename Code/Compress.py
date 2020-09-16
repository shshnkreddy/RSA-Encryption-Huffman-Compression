import sys
import os
import pickle
from bstring import genBinaryString, genByteArr
from file import *
from Tree import *

if __name__ == '__main__':
    
    if(len(sys.argv) < 2):
        print "Enter file name to be compressed!"
        sys.exit()

    if(os.path.exists(sys.argv[1])):
            with open(sys.argv[1], 'r') as f1:
                try: 
                    l = f1.read()
                except:
                    print "Error in accessing given file!"
                    sys.exit()
    else:
        print "File doesn't exist!"
        sys.exit()

    
    #Generating custom encoding:
    occ = genCount(l)
    tree = Tree.genTree(Tree.genNodes(occ))
    paths = {}
    Tree.Paths(tree,"",paths)

    #Generating a binary string, with custom encoding:
    binaryString = genBinaryString(paths,sys.argv[1])

    #Generating a bytearray, using binary string:
    (binaryArr, binlen) = genByteArr(binaryString)

    #Writing key/value of custom encoding on top of file:
    with open(sys.argv[1] + ".bcn", 'wb') as f2: 
        try:
            pickle.dump(binlen,f2)
            pickle.dump(paths,f2)
            binaryArr.tofile(f2)
            os.remove(sys.argv[1])
        except:
            print "Error creating compressed file!"
            sys.exit()
