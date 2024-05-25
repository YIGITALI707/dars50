import eel
eel.init('paket/web/web')
@eel.expose
def add_user(name,surname,phone):
    print(name,surname,phone)
    f=open("datas.txt","a")
    f.write(name + " " + surname + " " + phone + "\n")
    f.close()
    return "User qo'shildi"



eel.start('index.html')