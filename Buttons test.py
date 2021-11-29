import tkinter as tk

window = tk.Tk()

"""butA = tk.Button(text='A',bg='yellow',fg='blue')
butA.pack()

butB = tk.Button(text='B',bg='yellow',fg='blue')
butB.pack() """

but = []
kk = -1
for ii in range (3):
    for jj in range (3):
        kk += 1
        tt = str(kk)
        if kk == 0:
            bb = tk.Button(text=tt,bg='black',fg='black')
        else:
            bb = tk.Button(text=tt,bg='yellow',fg='blue')
        
        but.append(bb)
        bb.grid(row=ii,column=jj)
        





