import numpy as np
import random
mtx = np.ndarray((5,5))
for i in range(5):
    for j in range(5):
        mtx[i][j] = random.randint(0,100)
print(mtx)

def oszlop_legnagyobb(mtx,a):
    max=-1
    for i in range(0,5):
        if mtx[i][a]>max:
            max=mtx[i][a]
    return max

def sor_legnagyobb(mtx,b):
    max=-1
    for i in range(0,5):
        if mtx[b][i]>max:
            max=mtx[b][i]
    return max

a=int(sor_legnagyobb(mtx,0))
b=int(sor_legnagyobb(mtx,1))
c=int(sor_legnagyobb(mtx,2))
d=int(sor_legnagyobb(mtx,3))
e=int(sor_legnagyobb(mtx,4))

f=int(oszlop_legnagyobb(mtx,0))
g=int(oszlop_legnagyobb(mtx,1))
h=int(oszlop_legnagyobb(mtx,2))
i=int(oszlop_legnagyobb(mtx,3))
j=int(oszlop_legnagyobb(mtx,4))
sum=int(a+b+c+d+e+f+g+h+i+j)
print("sorok maximuma: ",a,b,c,d,e)
print("oszlopok maximuma: ",f,g,h,i,j)
print("osszeguk: ",sum)