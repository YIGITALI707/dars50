import random
w = "Lorem elit ipsum dolor sit amet consectetur, sit adipisicing elit. Exercitationem, dolorum elit".split()
a=[]
for i in w:
    q=random.choices(w)
    a.append(q)
print(a)