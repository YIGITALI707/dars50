d={
    "users":[
        {"name":"sobir","score":10},
        {"name":"asror","score":56},
        {"name":"aziz","score":45},
        {"name":"asad","score":53}
    ]}

succes=[]
fail=[]

for i in d["users"]:
    if i["score"]>50:
        succes.append(i)
        print("succes=",succes)
    else:
        fail.append(i)
        print("fail=",fail)