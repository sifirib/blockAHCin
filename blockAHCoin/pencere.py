from tkinter import *

def openwindow(window):
    abc = Label(window,text = "ABC")
    abcgiris = Entry(window)
    
    abc.grid()
    abcgiris.grid()
    window = mainloop()
    
pencere = Tk()
wallet = Button(pencere, text = "wallettt" , command = lambda:openwindow(pencere))


wallet.grid(row = 0, column = 0)

pencere = mainloop()

