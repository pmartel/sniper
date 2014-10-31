""" This code is to solve the problem described in nerd_sniping.png
set up an array with the problem near the middle and a spceified number of blank
rows and columns around the basic 1x2 grid.  Solve the problem with a relaxation
method and print the result """

from TwoD import *

class Center:
    """set up a variable center array (store the info)"""
    def __init__( self, rSize, cSize, r1,c1,r0,c0):
        self.rSize = rSize
        self.cSize = cSize
        self.r1 = r1
        self.c1 = c1
        self.r0 = r0
        self.c0 = c0
        
def relax(a):
    """run relaxation on the array a.  Each point becomes the average of
       the 4 adjacent points """
    rn = a.rows
    cn = a.cols
    new = TwoD(rn,cn)

    for r in range(rn):
        for c in range(cn):
            new.arr[c][r] = a.arr[c][r]
    # this takes care of edges, but is messy
    for r in range(rn):
        if r == 0:
            for c in range(cn):
                if c == 0:
                    a.arr[c][r] = ( new.arr[c][r+1] +
                                    new.arr[c+1][r])/2
                elif c == cn-1:
                    a.arr[c][r] = ( new.arr[c][r+1] +
                                   new.arr[c-1][r])/2
                else:
                    a.arr[c][r] = ( new.arr[c][r+1] +
                                   new.arr[c-1][r] + new.arr[c+1][r])/3
        elif r == rn-1:
            for c in range(cn):
                if c ==0:
                    a.arr[c][r] = (new.arr[c][r-1] +
                                    new.arr[c+1][r])/2
                elif c == cn-1:
                    a.arr[c][r] = (new.arr[c][r-1] +
                                   new.arr[c-1][r])/2
                else:
                    a.arr[c][r] = (new.arr[c][r-1] + 
                                   new.arr[c-1][r] + new.arr[c+1][r])/3
        else:
            for c in range(cn):
                if c ==0:
                    a.arr[c][r] = (new.arr[c][r-1] + new.arr[c][r+1] +
                                    new.arr[c+1][r])/3
                elif c == cn-1:
                    a.arr[c][r] = (new.arr[c][r-1] + new.arr[c][r+1] +
                                   new.arr[c-1][r])/3
                else:
                    a.arr[c][r] = (new.arr[c][r-1] + new.arr[c][r+1] +
                                   new.arr[c-1][r] + new.arr[c+1][r])/4
            
    
    
def reInit(a,center):
    b=int((a.rows-center.rSize)/2)
    a.set(b+center.r1,b+center.c1,1)
    a.set(b+center.r0,b+center.c0,0)

def resistor(a,center):
    b=int((a.rows-center.rSize)/2)
    if b == 0:
        current = (1-a.arr[1][0]) + (1-a.arr[2][1])
    else:
        current = (1-a.arr[b+1][b]) + (1-a.arr[b+3][b]) +\
        (1-a.arr[b+2][b-1]) + (1-a.arr[b+2][b+1])
    return 1/current
        


#main
center = Center(2, 3, 0, 2, 1,0)
#center = Center(2, 2, 0, 1, 1,0)
b = int(input('blanks around center? '))
arr = TwoD(2*b+center.rSize,2*b+center.cSize,0)

# top of loop
reInit(arr,center)

#arr.display()

again = 'y'
while again != 'n':
    # it takes 2 relaxation steps to change the resistance
    relax(arr)
    reInit(arr,center)
    relax(arr)
    reInit(arr,center)
    #arr.display()
    r = resistor(arr,center)
    print('resistance=',round(r,6))
    again = input('again?(y/n)')
arr.display()






