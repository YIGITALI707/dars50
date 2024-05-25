import tkinter as tk
import json
window=tk.Tk()
window.title("SAVE")
window.geometry("600x600+700+100")


def saqlash():
    xujjat={"ism": name.get(),
        "familiya": name1.get(),
        "adres": name2.get(),
        "telefon": name3.get(),
        "yosh": name4.get()
        }
    x=open("malumot.txt","a")
    json.dump(xujjat,x)
    x.write("\n")
    name.delete(0, tk.END)
    name1.delete(0, tk.END)
    name2.delete(0, tk.END)
    name3.delete(0, tk.END)
    name4.delete(0, tk.END)

# entry=Entry(window,width=15,font=(" ",15))
# entry.place(x=150,y=50)
tk.Label(text="Ism",bg="green",fg="white",font=("Times new roman",13,"bold")).grid(row=0,column=0,stic="w")
name=tk.Entry(window)
tk.Label(text="Familiya",bg="green",fg="white",font=("Times new roman",13,"bold")).grid(row=1,column=0,stic="w")
name1=tk.Entry(window)

tk.Label(text="Adres",bg="green",fg="white",font=("Times new roman",13,"bold")).grid(row=2,column=0,stic="w")
name2=tk.Entry(window)

tk.Label(text="Telefon",bg="green",fg="white",font=("Times new roman",13,"bold")).grid(row=3,column=0,stic="w")
name3=tk.Entry(window)

tk.Label(text="Yosh",bg="green",fg="white",font=("Times new roman",13,"bold")).grid(row=4,column=0,stic="w")
name4=tk.Entry(window)

name.grid(row=0,column=1)
name1.grid(row=1,column=1)
name2.grid(row=2,column=1)
name3.grid(row=3,column=1)
name4.grid(row=4,column=1)

save_button = tk.Button(window, text="Saqlash",command=saqlash)
save_button.grid(row=5, column=0, columnspan=2)

window.grid_columnconfigure(0,minsize=100)
window.grid_columnconfigure(1,minsize=100)


window.mainloop()
