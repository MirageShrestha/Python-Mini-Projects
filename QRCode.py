import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data=("https://www.facebook.com/mirage.sth.1/")
qr.make(fit=True)
image=qr.make_image(fill_color="blue",back_color="white")
image.save("MirageSth_Facebook.png")