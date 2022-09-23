from gettext import npgettext
import numpy as np
from scipy import interpolate

if __name__ == "__main__":
    list = np.loadtxt("data2.txt")
    print(list)
    #x = list[:,0]
    #y = list[:,1]

    #pol = interpolate.interp1d(x,y)
    #print(pol)