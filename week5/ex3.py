from queue import Empty
import mmh3
import numpy as np
from DataWeek5
from week5.DataWeek5.similarity import listhash



#3.1 
def minhash(lst, seed=0):
    minhash = 99999999999999999999999999
    if seed == 0:
        print("No seed provided, default execution")
        for shingle in lst:
            hash = mmh3.hash(shingle)
            if minhash < hash:
                minhash = hash
    else:
        for shingle in lst:
            hash = mmh3.hash(shingle, seed)
            if minhash < hash:
                minhash = hash
    return min


#3.2
def extendedminhash(lst, seedlist):
    minhashlist = []
    for seed in seedlist:
        minhashlist.append(minhash(lst, seed))
return minhashlist