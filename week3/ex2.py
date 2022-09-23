from gettext import npgettext
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #x=[1,2,3,4]
    #np.savetxt("data3.txt",x)
    list = np.loadtxt("week3/data2.txt")
    print(list)
    x = list[:,0]
    y = list[:,1]

    f = interpolate.interp1d(x,y, kind='cubic')

    y1=f(x)

    #plt.figure(1)
    plt.plot(x,y,'r')
    plt.plot(x,y1,'x')
    plt.legend(["real", "interpolated"])
    plt.show()

    