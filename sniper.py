""" This code is to solve the problem described in nerd_sniping.png
set up an array with the problem near the middle and a spceified number of blank
rows and columns around the basic 1x2 grid.  Solve the problem with a relaxation
method and print the result """

from TwoD import *

def relax(a):
    rn = a.rows
    cn = a.cols
    new = TwoD(rn+2,cn+2,0)
    # copy to middle 
    for r in range(rn):
        for c in range(cn):
            new.arr[c+1][r+1] = a.arr[c][r]
    # relax
    for r in range(rn):
        for c in range(cn):
            a.arr[c][r] = (new.arr[c][r+1] + new.arr[c+2][r+1] +
                           new.arr[c+1][r] + new.arr[c+1][r+2])/4
            
            
    reInit(a)
#    a.display()
    
    
def reInit(a):
    b=int((a.rows-1)/2)
    a.set(b,b+2,1)
    a.set(b+1,b,0)

def resistor(a,b):
    # a.arr[b+2][b] == 1
    if b == 0:
        current = (1-a.arr[1][0]) + (1-a.arr[2][1])
    else:
        current = (1-a.arr[b+1][b]) + (1-a.arr[b+3][b]) +\
        (1-a.arr[b+2][b-1]) + (1-a.arr[b+2][b+1])
    return 1/current
        


#main
b = int(input('blanks around center? '))
arr = TwoD(2*b+2,2*b+3,0)

# top of loop
reInit(arr)

#arr.display()

again = 'y'
while again != 'n':
    relax(arr)
    r = resistor(arr,b)
    print('resistance=',r)
    again = input('again?(y/n)')





