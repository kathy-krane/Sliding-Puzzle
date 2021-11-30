#




ROWS = 4
COLS = 3

ROW = 0
COL = 1

p = [ [1,2,3],[4,5,0],[7,8,9],[10,11,6]]  #12 square
q =[ [0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,1]]  #16 square
zero = [-1,-1]
touch = [-1,-1]


def moveRowLeft(g,blank,touched):
    r = touch[ROW]
    kk=0
    for kk in range (blank[COL],touch[COL],-1):
        print ("piece [", touch[ROW],kk,"] is ",g[r][kk])
        g[r][kk] = g[r][kk-1]
    g[r][touch[COL]]=0
    print(g)

    
def moveRowRight(g,blank,touch):
    r = touch[ROW]
    for kk in range (blank[COL],touch[COL],1):
        print ("piece [", touch[ROW],kk,"] is ",g[r][kk])
        g[r][kk] = g[r][kk+1]
    g[r][touch[COL]]=0
    print(g)



def moveColUp(g,blank,touch):
    r = blank[ROW]
    c = touch[COL]
    for kk in range (blank[ROW], touch[ROW],-1):
        g[kk][c] = g[kk-1][c]
        print ("Up from col", [r,kk], "to ", touch)
    g[touch[ROW]][c]= 0


def moveColDown(g,blank,touch):
    r = blank[ROW]
    c = touch[COL]
    print ("Down from row ", r)
    for kk in range (blank[ROW], touch[ROW],1):
        g[kk][c] = g[kk+1][c]
        print ("down from col", [r,kk], "to ", touch)
    g[touch[ROW]][c]= 0
   



def findZero(p):
    row = -1
    col = -1
    for ii in range (ROWS):
        currRow = p[ii]
        if 0 in currRow:   
            row = ii
            col = currRow.index(0)
    return ([row,col])



def findTouch(p):
    r = int(input("row: "))
    c = int(input("col: "))
    print("Touched", p[r][c])
    return ([r,c])


print(q)
zero = findZero(q)
touch = findTouch(q)

if True:
    
    if zero[ROW] == touch[ROW]:     #touch is in same row as blank
        if zero[COL] < touch[COL]:       #touch is right of blank
            moveRowRight(q,zero,touch)
            print ("right")
        elif zero[COL] > touch[COL]:     #touch is left of blank
            moveRowLeft(q,zero,touch)
            print ("left")
        else:
            print ("touched blank")
    else:
        print ("Stay row")

    print ("BLANK",zero[COL],"touch",touch[COL])    
    if zero[COL] == touch[COL]:     #touch is in same col as blank
        if zero[ROW] < touch[ROW]:       #touch is below blank
            moveColDown(q,zero,touch)
            print ("below")
        elif zero[ROW] > touch[ROW]:     #touch is above blank
            moveColUp(q,zero,touch)
            print("above")
        else:
                print ("touched blank")
    else:
        print ("Stay col")

print (q)
    





