#5-masala
def eng_katta_farqni_topish(a):
    b = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            farq=a[j]-a[i]
            b.append(farq)
    return max(b)
a=[21,19,45,39,42,49]
print(eng_katta_farqni_topish(a))
#-------------------------------------
#2-masala
import random
def matematik_savol(func):
    def tekshirish(*args,**kwargs):
        a=random.randint(1,5)
        b=random.randint(1,5)
        c=random.randint(1,5)
        d=random.choice(["*","-","+"])
        savol=f"{a} {d} {c} {d} {b} {d} {c}"
        javob=int(input(f"javob yozing {savol}="))
        togri_javob=eval(savol)
        if javob==togri_javob:
            x=func(*args,**kwargs)
            return x
        else:
            print("noto'g'ri")
    return tekshirish


@matematik_savol
def top():
    print("ok")
top()
#--------------
#6-masala
def teskari(x):
    a = x[12:17:]
    b = x[6:11:]
    c=x[0:5:]
    teskari_gap=f"{a} {b} {c}"
    return teskari_gap
x="salom senga baxor"
print(teskari(x))

#3-masala
#github link https://github.com/YIGITALI707


