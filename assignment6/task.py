from tkinter import *

try :
    # Defining main Window
    window = Tk()
    window.geometry('500x500')

    # Entry Element
    entry = Entry(window, width=56, borderwidth=5)
    entry.place(x=0, y=0)

    # Buttons
    def click(num):
        """
        This function is used to display number on entry box
        :return: void
        """
        result = entry.get() # value inside entry box
        entry.delete(0,END)
        entry.insert(0,str(result) + str(num))


    b = Button(window, text="1", width=12, command=lambda : click(1))
    b.place(x=10,y=60)

    b = Button(window, text="2", width=12, command=lambda : click(2))
    b.place(x=80,y=60)

    b = Button(window, text="3", width=12, command=lambda : click(3))
    b.place(x=170,y=60)

    b = Button(window, text="4", width=12, command=lambda : click(4))
    b.place(x=10,y=120)

    b = Button(window, text="5", width=12, command=lambda : click(5))
    b.place(x=80,y=120)

    b = Button(window, text="6", width=12, command=lambda : click(6))
    b.place(x=170,y=120)

    b = Button(window, text="7", width=12, command=lambda : click(7))
    b.place(x=10,y=180)

    b = Button(window, text="8", width=12, command=lambda : click(8))
    b.place(x=80,y=180)

    b = Button(window, text="9", width=12, command=lambda : click(9))
    b.place(x=170,y=180)

    b = Button(window, text="0", width=12, command=lambda : click(0))
    b.place(x=10,y=240)

    # Add Operators
    def add() : 
        """
        This function is used to addition of numbers on entry box
        :return: void
        """
        n = entry.get()
        global math
        math = 'addition'
        global i
        i = int(n)
        entry.delete(0, END)


    b = Button(window, text="+", width=12, command=add)
    b.place(x=80,y=240)

    # Subtract Operators
    def sub() : 
        """
        This function is used to subtraction of numbers on entry box
        :return: void
        """
        n = entry.get()
        global math
        math = 'subtraction'
        global i
        i = int(n)
        entry.delete(0, END)

    b = Button(window, text="-", width=12, command=sub)
    b.place(x=170,y=240)

    # Multiply Operators
    def multiply() : 
        """
        This function is used to multiplication of numbers on entry box
        :return: void
        """
        n = entry.get()
        global math
        math = 'multiplication'
        global i
        i = int(n)
        entry.delete(0, END)

    b = Button(window, text="*", width=12, command=multiply)
    b.place(x=10,y=300)

    # Divide Operators
    def divide() : 
        """
        This function is used to devision of numbers on entry box
        :return: void
        """
        n = entry.get()
        global math
        math = 'division'
        global i
        i = int(n)
        entry.delete(0, END)

    b = Button(window, text="/", width=12, command=divide)
    b.place(x=80,y=300)

    # Equal Operators
    def equal() : 
        n2 = entry.get()
        entry.delete(0, END)

        if math == 'addition' : 
            entry.insert(0, i + int(n2))
        elif math == 'subtraction' :
            entry.insert(0, i - int(n2))
        elif math == 'multiplication' :
            entry.insert(0, i * int(n2))
        elif math == 'division':
            entry.insert(0, i / int(n2))         

    b = Button(window, text="=", width=12, command=equal)
    b.place(x=170,y=300)

    # Clear Operators
    def clear() :
        entry.delete(0,END)

    b = Button(window, text="clear", width=12)
    b.place(x=10,y=350)

    # MainLoop
    window.mainloop()    
except Exception as e:   
    print(f'\nError: {e}')
finally : 
    print(f'\nClosing window..............')
    window.destroy()    