

#1-masala
txt_fayl_joylashuvi="D:\new project\vazifa50.txt"
def txt_fayl_ochuvchi(txt_fayl_joylashuvi,):
    try:
        x=open(r"D:\\new project\\vazifa50.txt","r")
        a=x.read()
        return a
    except FileNotFoundError:
        print(f"Fayl {txt_fayl_joylashuvi} yo'q ekan.")
txt_fayl_joylashuvi=r"D:\\new project\\vazifa50.txt"
print(txt_fayl_ochuvchi(txt_fayl_joylashuvi)) # txt fayl o'qiy oladigan fayl tuzdim lekin txt fayl ichidagi
# sozlarni qanday qilib sanashni bilmadim???????????

#2-masala
def txt_fayl_ochuvchi(txt_fayl_joylashuvi):
    try:
        x=open(r"D:\\new project\\vazifa50.txt","r")
        u=x.read()
        b = eval(u)
        c=max(b,key=len)
        return u,c
    except FileNotFoundError:
        print(f"Fayl {txt_fayl_joylashuvi} yo'q ekan.")

txt_fayl_joylashuvi=r"D:\\new project\\vazifa50.txt"
print(txt_fayl_ochuvchi(txt_fayl_joylashuvi))

#3-masala
l=[1,2,3,4,5,6,7,17,9,10]
for i in range(len(l)-1):
    if l[i]+1!=l[i+1]:
        print(f"noto'g'ri raqamlar {l[i]}")


