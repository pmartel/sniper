""" This code is to solve the problem described in nerd_sniping.png
set up an square array  of a specified size with the problem gridnear the middle
  Solve the problem with a relaxation method and print the result """

from TwoD import *
# for timing 
from time import *

def Current(m):
    r = int(m.rows/2) 
    c = int(m.cols/2)
    #the location of the 1 volt node
    r1 = r-1
    c1 = c+1
    
    cur = (1-m.get(r1,c1-1)) #voltage difference through 1 Ohm
    cur += (1-m.get(r1,c1+1))
    cur += (1-m.get(r1-1,c1))
    cur += (1-m.get(r1+1,c1))
    return cur

def InitCondition(m): # set 1 volt and gnd nodes in the middle of array m
    r = int(m.rows/2) 
    c = int(m.cols/2)
    m.set(r,c-1,0)
    m.set(r-1,c+1,1)
###PrintCenter to see what's going on
def Relax(m,aux): # do a relaxation on TwoD m using TwoD aux as an auxiliary
    for r in range(m.rows):
        for c in range( m.cols):
            me = m.get(r,c)
            sum = me
            sum += RelaxGet(m,r-1,c,me)
            sum += RelaxGet(m,r+1,c,me)
            sum += RelaxGet(m,r,c-1,me)
            sum += RelaxGet(m,r,c+1,me)
            sum /= 5.
            aux.set(r,c,sum)
    m.copy(aux)
            
def RelaxGet(m,r,c,default):
    ret = m.get(r,c)
    if ret == None :
        ret = default
    return ret


#main
#get matrix size
s = int(input('matrix size? '))

# set up matrices
m1 = TwoD( s, s, 0.5)  #0.5 is close to the voltage on most nodes of a large grid
m2 = TwoD( s, s )

#run the loop s/2 times the effect of relaxation should hit the 'walls' then
for i in range(int(m1.cols/2)):
    InitCondition(m1)
    c = Current(m1)
    print(i+1,1/c)
    #15m1.display()
    Relax(m1,m2)

#m1.display()