from tkinter import *
def click(event):
    global scvalue
    text= event.widget.cget("text") # event.widget gives button which is run and .cget gives the text of button
    print(text)
    
    if text == "=":
         if scvalue.get().isdigit():
             value = int(scvalue.get())
         else:
            try:
             value = eval(screen.get())


            except Exception as e:
                value = "ERROR"
            
            

         scvalue.set(value)
         screen.update
             
    
    
    elif text== "c":
        scvalue.set("")
        screen.update()
    
    
    else:
        

        scvalue.set(scvalue.get() + text)
        screen.update()



root=Tk()
root.geometry("644x900")
root.title("calculator by vaibhav zinjurke ")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8,padx=10,pady=10)


frame1= Frame(root, bg="black")
b = Button( frame1, text="9",padx=20 ,pady=5, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="8",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="7",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)


frame1= Frame(root, bg="black")
b = Button( frame1, text="6",padx=20, pady=5, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="5",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="4",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)


frame1= Frame(root, bg="black")
b = Button( frame1, text="3",padx=20, pady=15, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="2",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="1",padx=20, pady=5, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)



frame1= Frame(root, bg="black")
b = Button( frame1, text="0",padx=22, pady=5, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="-",padx=22, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="*",padx=22, pady=5, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)

frame1= Frame(root, bg="black")
b = Button( frame1, text="/",padx=18, pady=5, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="%",padx=18, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="=",padx=18, pady=5, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)

frame1= Frame(root, bg="black")
b = Button( frame1, text="c",padx=20, pady=15, font="lucida 35 bold")
frame1.pack()
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="8",padx=20, pady=15, font="lucida 35 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
b = Button( frame1, text="7",padx=20, pady=15, font="lucida 35 bold")
b.pack(side=LEFT , padx=15, pady=5)
b.bind("<Button-1>", click)



root.mainloop()