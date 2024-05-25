import tkinter
Window=tkinter.Tk()
counter=0
ayiruv=0

def plus():
    global counter
    counter+=1
    count.config(text=counter)
def ayir():
    global counter
    counter-=1
    count.config(text=counter)


Window.geometry("300x300")
label=tkinter.Label(text=" Counter ",font=("bolt",24))
count=tkinter.Label(text=" 0 ",font=("bolt",24))

knopka=tkinter.Button(text="add",command=plus,font=("bolt",24),foreground="#fff",bg="#333")
knopka1=tkinter.Button(text="minus",command=ayir,font=("bolt",24),foreground="#fff",bg="#333")
knopka1.pack()
label.pack()
count.pack()
knopka.pack()
Window.mainloop()
