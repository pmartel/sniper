# developing code for working with a 2-D array
class TwoD:
##    arr = [] # don't need to set these up explicitly
##    cols =0
##    rows=0

    def __init__(self, rows, cols, val = 0,digits =4):
        self.rows = rows
        self.cols = cols
        self.arr = []
        self.digits = digits
        rObj =[]
        for r in range(rows):
            rObj.append(val)
        for c in range(cols):
            # just having append(rObj) points to one copy
            self.arr.append(rObj.copy())

    def copy(self, m):
        """copy the contents of TwoD m to self  if reasonable. return true if copied"""
        if type(self) != type(m):
            return False
        if self.rows != m.rows:
            return False
        if self.cols != m.cols:
            return False
        for r in range(self.rows):
            for c in range(self.cols):
                self.arr[c][r] = m.arr[c][r]
        return True
                
        
    def display(self, left= 0,right=None,top=0,bot=None):
        """ print the 2D array with row and column stuff on the outside"""
        t = '\t|' # marker
        if right == None :
            right = self.cols
        if bot == None :
            bot = self.rows
        
        print('___',end='')
        for c in range(left,right): # column stuff
            print( t,c, end='')
        print()
        for r in range(top,bot):
            print(r, end='') # row stuff
            for c in range(left,right):
                v = self.arr[c][r]
                #print('debug',r,c,v)
                print( t,round(v,self.digits), end='')
            print()
        print()

    def fill(self, val):
        """ load with a single value """
        for r in range(self.rows):
            for c in range(self.cols):
                self.arr[c][r] = val

    def get(self, row, col ):
        """ get a value.  return None if outside of range """
        if row < 0 or row >= self.rows :
            return None
        if col < 0 or col >= self.cols :
            return None
        ret = self.arr[col][row]
        if ret == []:  # for the peg puzzle, a [] is out of bounds, so None
            return None
        else:
            return ret
        
    def seqFill(self):
        """ debug code """
        n = 0
        for r in range(self.rows):
            for c in range(self.cols):
                self.arr[c][r] = n
                n +=1

    def set(self, row, col, val ):
        """ get a value.  return None if outside of range """
        if row < 0 or row >= self.rows :
            return False
        if col < 0 or col >= self.cols :
            return False
        self.arr[col][row] = val
        return True

# this runs if TwoD.py is run stand-alone.
# it serves as debug code
if __name__ == '__main__':
    a = TwoD(4,3)
    b = TwoD(3,5)
    c = TwoD(4,3)
    a.seqFill()
    print('Class TwoD demo')
    print('a')
    a.display()
    print()
    print(a.get(1,2))
    print(a.get(-1,2))
    print(a.get(2,3))
    print(a.set(2,2,-1))
    print()
    print('modified a')
    a.display()
    b.seqFill()
    print('b')
    b.display()
    c.copy(a)
    print('c')
    print(c.arr)
        

    
