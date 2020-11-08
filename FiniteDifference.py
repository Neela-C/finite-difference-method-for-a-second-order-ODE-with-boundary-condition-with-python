# change where there is #### according to your need

import math
import numpy as np
import matplotlib.pyplot as plt


y0= 0      ######
yn= math.exp(-4)    ###### e^-4
x=[]
h= 0.2     ######
start = 0  ######  here I'm solving for 0<x
x.append(start)  
finish = 1  ######  here I'm solving for x<1
fnum=(finish - start)/h   

num=int(fnum)
onevec=np.ones(num+1)   
for i in range (start,num):  
    x.append(start+h)
    start = start +h
x = np.array(x)   

def p(x):  ##### change p(x)
    return 3*onevec 

def q(x):  ###### change q(x)
    return -4*onevec

def r(x): ###### change r(x)
    return (5*math.exp(1)**x)*onevec

a = 2- h*p(x)

b = 2* h**2 * q(x) -4

c = 2 + h*p(x)

d = 2* h**2 * r(x)

# print(a)
# print(b)
# print(c)
# print(d)

my_matrix = np.zeros((num - 1, num - 1))


for i in range(0, num-1): 
    for j in range(0, num-1):
        if i == j :
            my_matrix[i][j] = b[i]
        if i == j+1 :
            my_matrix[i][j] = a[i]
        if i+1 == j :
            my_matrix[i][j] = c[i]


#print (my_matrix)

otherside = np.zeros(num-1)


for i in range (0,num-1): 
    otherside[i] = d[i+1]

otherside[0] = d[1]-a[1]*y0
otherside[num-2] = d[-2]-c[-2]*yn



# print(otherside)

y = np.linalg.solve(my_matrix, otherside.T) #hale moadele

print(y)


x_axis = np.arange(0, 1, 0.01)


def realAnswerFunction(): ###### change the real answer
    return math.exp(-4)**x_axis- math.exp(1)**x_axis + x_axis * math.exp(1)**x_axis


y_axis = realAnswerFunction()



plt.plot(x_axis,y_axis)  


newlist =[]
for i in range(1,num):
    newlist.append(x[i])

plt.plot(newlist, y, 'bo')  

plt.show()
