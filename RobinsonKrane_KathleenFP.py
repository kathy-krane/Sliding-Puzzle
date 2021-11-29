#




ROWS = 4
COLS = 3
p = [ [1,2,3],[4,5,0],[7,8,9],[10,11,6]]
q =[ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
touch = [1,0]

def moveRowLeft(g,cc):
    print ("Left",cc)
    for kk in range (cc,0,-1):
        print (g[kk][cc])
    
def moveRowRight(g,r,blank, touched):
    print ("Right from ",r,",",blank, "to ", r,',',touched)
    for kk in range (blank,touched-1,-1):
        print ("piece [", r,kk,"] is ",g[r][kk])
        g[r][kk] = g[r][kk-1]
    g[r][kk]=0
    print(g)

def moveRow(rr):
    currRow = p[rr]
    if 0 in currRow:
        index = currRow.index(0)
        print("Found zero", rr, index)
        if index < touch[1]:
            moveRowLeft(p,index)
        elif index > touch[1]:
            moveRowRight(p,rr,index, touch[1])
        else:
            print ("Stay")
    else:
            print ("No blank space in row ",rr)
        

print(p,touch)
print("touched", p[touch[0]][touch[1]])
for ii in range (ROWS):
    moveRow(ii)
