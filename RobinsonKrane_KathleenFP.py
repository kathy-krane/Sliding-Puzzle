 #Sliding Puzzle app by Kathy Krane
#v10. 12/14/2021
# two custon widgets are used, aSPbutton and SPframe
# the internal puzzle date is stored in the SPframe.q
# a list of the button widget is stored in SPframe.buttonArray
# handlePuzzle is a fucntion that updates the puzzle array
# labelAllButtons changes the button labels after the puzzle array changes
# findTouch is a method which is associated with every button
# findTouch is activated when any button is pressed


from tkinter import *

ROWS = 4
COLS = 4

ROW = 0
COL = 1

p1 = [ [1,2,3],[4,5,0],[7,8,9],[10,11,6]]  # 12-square
p2 =[ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]  # 16-square
allButtons = []


zero = [-1,-1]
touch = [-1,-1]

class SPbutton(Button):
    def __init__(self,parent):


        ft = lambda : findTouch(self)
        Button.__init__(self,command=ft,width=4, height=3)

        self.row = -1
        self.col = -1
        self.num = -1
        self.frame = parent
        #print ('in s p b', self.row)
        
       
class SPframe(Frame):
    def __init__(self):
        
        window = Tk()
        #window['title'] = 'Puzzle'

        
        Frame.__init__(window)

        self.touchedRow = -1
        self.touchedCol = -1

        self.zeroRow = -1
        self.zeroCol = -1
        self.win = window


        self.buttonArray = []
        self.q = [ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
            
        Frame.pack(window)
        
    
        kk = -1
                
        for row in range (ROWS):
            for col in range (COLS):
                kk += 1
                tt = str(self.q[row][col])

                bb = SPbutton(self)
                
                if self.q[row][col] == 0:
                    bb['fg'] = "black"
                    bb['bg'] = 'black'
                    
                else:
                    bb['fg'] = "yellow"
                    bb['bg'] = 'blue'

                bb.frame = self
                bb.num= kk

                bb.row = row
                bb.col = col
                bb['text'] = str(bb.num)
                bb['width']=6

                self.buttonArray.append(bb)
                bb.grid(row=row,column=col)

                
        zero = findZero(self.q)

        self.zeroRow = zero[ROW]
        self.zeroCol = zero[COL]

        self.touchedRow = zero[ROW]
        self.touchedCol = zero[COL]

        #print ('frame: ',self.zero, end= ' ')
        #print("in spframe button", bb, bb.frame)

        #####


def findTouch(button):

    print ('in  ft ',end=' ')
 

    frame = button.frame

    r = button.row
    c = button.col

    frame.touchedRow = r
    frame.touchedCol = c

    touch[ROW]= r
    touch[COL] = c

    print(r,c)

    handlePuzzle (frame.q, touch)
    labelAllButtons(frame.q,frame.buttonArray)


                   

def moveRowLeft(g,blank,touched):
    r = touch[ROW]
    kk=0
    for kk in range (blank[COL],touch[COL],-1):
        g[r][kk] = g[r][kk-1]
        
    g[r][touch[COL]]=0

    
def moveRowRight(g,blank,touch):
    r = touch[ROW]
    for kk in range (blank[COL],touch[COL],1):
        g[r][kk] = g[r][kk+1]
        
    g[r][touch[COL]]=0



def moveColUp(g,blank,touch):
    r = blank[ROW]
    c = touch[COL]
    for kk in range (blank[ROW], touch[ROW],-1):
        
        g[kk][c] = g[kk-1][c]
    g[touch[ROW]][c]= 0


def moveColDown(g,blank,touch):
    r = blank[ROW]
    c = touch[COL]

    for kk in range (blank[ROW], touch[ROW],1):
        g[kk][c] = g[kk+1][c]

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



def handlePuzzle(q,touch):

    tt = ""
    zero = []
    zero = findZero(q)
    print("in handle", zero)

    
    if zero[ROW] == touch[ROW]:     #touch is in same row as blank
        if zero[COL] < touch[COL]:       #touch is right of blank
            moveRowRight(q,zero,touch)

        elif zero[COL] > touch[COL]:     #touch is left of blank
            moveRowLeft(q,zero,touch)

        else:
            tt ="touched blank"
    else:
        tt = "Stay row"

     
    if zero[COL] == touch[COL]:     #touch is in same col as blank
        if zero[ROW] < touch[ROW]:       #touch is below blank
            moveColDown(q,zero,touch)
            
        elif zero[ROW] > touch[ROW]:     #touch is above blank
            moveColUp(q,zero,touch)

        else:
                tt= "touched blank"
    else:
        tt="Stay col"
    
    

def labelAllButtons(q,buttonArray):
    kk = -1
    #ft = lambda : findTouch(button,frame)
    

    
    for bb in buttonArray:
   
        r=bb.row
        c=bb.col
        
        bb['text'] = str(q[r][c])
        if bb['text'] == '0':
            bb['bg'] = 'black'
            bb['fg'] = 'black'
        else:
            bb['bg'] = 'blue'
            bb['fg'] = 'yellow'




def main():
    """Instantiate and pop up the window."""
    print(' ')



    SPframe().win.mainloop()


main()

            
