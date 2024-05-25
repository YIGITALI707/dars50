a = [88,44,12,36,95,77,88,44,12,36]
b = [89,45,12,36,99,77,18,449,12,136]
def intersect_list(a,b):
    a1=set(a)
    b1=set(b)
    x=a1.intersection(b1)
    q=list(x)
    return q
print(intersect_list(a,b))