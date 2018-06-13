from tkinter import *

root = Tk()

root.title('hello world')

root.geometry('500x500')

root.configure(background='#EEEEEE')

hwL = Label(root, text='Hello World!!', bg='red', font='Arial 15 bold')

hwL.pack()

exitB = Button(root, text='EXIT', bg='blue', font='Times 15 bold', command=root.destroy)

exitB.pack(fill=X, side=BOTTOM)

root.mainloop()
