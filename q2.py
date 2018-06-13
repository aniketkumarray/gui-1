from tkinter import *


def display():

    txt = Label(root, text='Assignment of Gui Q2', bg='red', font='Arial 15 bold ')
    txt.pack()



root = Tk()

root.title('assignment')

root.geometry('500x500')

root.configure(background='#EEEEEE')

hwL = Label(root, text='Hello World!!', bg='green', font='Times 15 bold ')

hwL.pack(fill=X, side=TOP)

dispB = Button(root, text='PLEASE CLICK IT', bg='yellow', font='Times 15 bold ', command=display)


exitB = Button(root, text='EXIT', bg='blue', font='Times 15 bold', command=root.destroy)

exitB.pack(fill=X, side=BOTTOM)
dispB.pack(side=BOTTOM)


root.mainloop()
