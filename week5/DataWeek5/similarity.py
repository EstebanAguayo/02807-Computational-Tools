import sys
import os
import mmh3


#################### Utilities ######################
#hashes a list of strings
def listhash(l,seed):
	val = 0
	for e in l:
		val = val ^ mmh3.hash(e, seed)
	return val 



################### Similarity ######################
q = 3 # length of shingle
k = 100 # number of minhashes
docs = {} #dictionary mapping document id to document contents

# read data sets
srcfolder = os.path.dirname(os.path.abspath(__file__))
datafolder = os.path.join(srcfolder, "ats_corpus_small")   # change to ats_corpus for large data set

for file in os.listdir(datafolder):
    filepath = os.path.join(datafolder, file)
    f = open(filepath, 'r')
    docs[file] = f.read()
    print("read document " + file)
    f.close()
