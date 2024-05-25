import os
def chec_file(papka_yoli,fayl_nomi):
    x = os.path.join(papka_yoli, fayl_nomi)
    if os.path.exists(x):
        print(f"{x}==>bu yo'lda fayl mavjud")
    else:
        print(f"{x}==>bu yo'lda fayl mavjud emas")
papka_yoli="D:\\new project\\paket"
fayl_nomi="open8.txt"
chec_file(papka_yoli,fayl_nomi)




