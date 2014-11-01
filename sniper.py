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
    if not( center.r0 == None): # handle not having a ground point
        a.set(b+center.r0,b+center.c0,0)

def resistor(a,center):
    """ For the 1 Volt point, the resistance is 1/(sum of currents in
        adjacent resistors).  The current in one of those resistors is
        1-(voltage at adjacent node)"""
    b=int((a.rows-center.rSize)/2)
    # row and column of "1" point
    r = b + center.r1
    c = b + center.c1
    current = 0
    # current in resistor north of "1" point
    if r > 0:
        current += 1 - a.arr[r-1][c]
    #south
    if r < a.rows-1:
        current += 1 - a.arr[r+1][c]
    #east
    if c < a.cols-1:
        current += 1 - a.arr[r][c+1]
    #west
    if c > 0:
        current += 1 - a.arr[r][c-1]

    return 1/current

def CheckEdges(a):
    """ check that all edge cells of the array are 0.  if not say "at limit" """
    lim = False
    for r in range(a.rows):
        if a.arr[r][0] != 0:
            lim = True
            break
        if a.arr[r][a.cols-1] != 0:
            lim = True
            break
    if not( lim ):
        for c in range(a.cols):
            if a.arr[0][c] != 0:
                lim = True
                break
            if a.arr[a.rows-1][c] != 0:
                lim = True
                break
    if lim:
        print( "at limit")

        
#main
center = Center(2, 3, 0, 2, 1,0) #"sniping" grid
#center = Center(2, 2, 0, 1, 1,0)
#center = Center(1, 1, 0, 0, None,None)

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
    CheckEdges(arr)
    again = input('again?(y/n)')
arr.display()






