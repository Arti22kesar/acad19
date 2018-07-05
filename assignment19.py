#Ques1.

import numpy as np
a = np.random.rand(10,1)
print(a)
print(a.shape)
print(np.mean(a))
print(np.mean(a, axis = 0))
print(np.mean(a, axis = 1))

#Ques2.

import numpy as np
b=np.random.rand(20,1)
print(b)
print(b.shape)
print(np.std(b))
print(np.var(b))

#Ques3.

import numpy as np
c=np.random.rand(10,20)
d=np.random.rand(20,25)
x=np.matmul(c,d)
print(x)
print(x.shape)
print(np.sum(x))

#Ques4.

import numpy as np
from math import *
a=np.full((10,1),2)
print(a)
def f(a):
   return 1 /(1+exp(-a))
f_v=np.vectorize(f)
sc=np.array(a)
n= f_v(sc)
print(n)



