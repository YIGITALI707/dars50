from tkinter import *

window=Tk()
window.title("Kalkulyator")
window.geometry("600x600+700+100")

entry=Entry(window,width=15,font=(" ",20))
entry.place(x=100,y=50)
knopka1=Button(window,bg="black",fg="white",text="1")
knopka1.place(x=100,y=100,width=25,height=25 )

knopka2=Button(window,bg="black",fg="white",text="2")
knopka2.place(x=125,y=100,width=25,height=25 )

knopka3=Button(window,bg="black",fg="white",text="3")
knopka3.place(x=150,y=100,width=25,height=25 )

knopka4=Button(window,bg="black",fg="white",text="4")
knopka4.place(x=175,y=100,width=25,height=25 )

knopka5=Button(window,bg="black",fg="white",text="5")
knopka5.place(x=100,y=125,width=25,height=25 )

knopka6=Button(window,bg="black",fg="white",text="6")
knopka6.place(x=125,y=125,width=25,height=25 )

knopka7=Button(window,bg="black",fg="white",text="7")
knopka7.place(x=150,y=125,width=25,height=25 )

knopka8=Button(window,bg="black",fg="white",text="8")
knopka8.place(x=175,y=125,width=25,height=25 )

knopka9=Button(window,bg="black",fg="white",text="9")
knopka9.place(x=100,y=150,width=25,height=25 )

knopka0=Button(window,bg="black",fg="white",text="0")
knopka0.place(x=125,y=150,width=25,height=25 )

knopka=Button(window,bg="black",fg="white",text="=")
knopka.place(x=150,y=150,width=25,height=25 )

knopka11=Button(window,bg="black",fg="white",text="*")
knopka11.place(x=200,y=100,width=25,height=25 )

knopka12=Button(window,bg="black",fg="white",text="/")
knopka12.place(x=225,y=100,width=25,height=25 )

knopka13=Button(window,bg="black",fg="white",text="-")
knopka13.place(x=200,y=125,width=25,height=25 )

knopka14=Button(window,bg="black",fg="white",text="+")
knopka14.place(x=225,y=125,width=25,height=25 )
window.mainloop()
