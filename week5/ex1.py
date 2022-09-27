import numpy as np

def shingle(q,string):
    shingles=[]
    for i in range(len(string)):
        stored = False
        if i+q > len(string):
            print("Length issue or Finalized")
            break
        else:
            for element in np.in1d(string[i:q+i],shingles):
                if element == True:
                    stored = True
            if stored == False:
                shingles.append(string[i:q+i]) #also check for already existing shingles
    return shingles


if __name__ == "__main__":
    print(shingle(2,"abcdeab"))