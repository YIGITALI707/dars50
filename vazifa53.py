import qrcode
import random

def qr_kod_yaratish():
    link = ''
    for _ in range(10):
        link += random.choice('abcdefghijklmnopqrstuvwxyz')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)

    yield link, qr

generator = qr_kod_yaratish()
link, qr = next(generator)
print(f"natijani chiqar {link}")
