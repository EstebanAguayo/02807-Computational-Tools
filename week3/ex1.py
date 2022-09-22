import numpy as np

file_path = "data.txt"

if __name__ == "__main__":
   #X = 1,2,3,4
   #Y = 6,9,12,7
   #Z = 2,0,9,10

   #X = int(X)
   #Y = int(Y)
   #Z = int(Z)

   #np.savetxt("data.txt",(X,Y,Z))
    
   #file_path="C:/Users/Esteban/Documents/DTU/3rd_Semester/02807_Comp_Tools/Exercises/Week2/data.txt"
    
    Mat = np.loadtxt("data.txt") 
    Mat.reshape((3,4))
    A = Mat[:,:3]
    b = Mat[:,3].T
    
    x = np.linalg.solve(A,b)

    print(x)
