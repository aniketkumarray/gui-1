from tkinter import *

def change():

   hwL.config( text='Assignment q3', bg='red', font='Times 15 bold ')

   hwL.pack()

root = Tk()

root.title('My App')

root.geometry('300x300')

root.configure(background='#EEEEEE')

frame=Frame(root,bg='black')

frame.pack()

hwL = Label(frame, text='GuI', bg='green', font='Times 15 bold ')

hwL.pack(fill=X, side=TOP)

exitB = Button(frame, text='EXIT', command=root.destroy, bg='blue', font='Times 15 bold ')

exitB.pack(fill=X)

changeB = Button(frame, text= 'CHANGE THE TEXT', command=change, bg='yellow', font='Times 15 bold ')

changeB.pack(side=BOTTOM)

frame.mainloop()

root.mainloop()
