from tkinter import *


def display():

    print(textI.get())



root = Tk()
root.title('assignment')
root.geometry('500x500')


textI = Label(root, text='input which you want to display: ')
textI.grid(row=1, column=1, sticky=E)



textI = Entry(root)
textI.grid(row=1, column=2)

displayB = Button(root, text='DISPLAY VALUES', command=display)

displayB.grid(row=3, columnspan=2, sticky=W)

root.mainloop()
