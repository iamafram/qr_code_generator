#!/usr/bin/python

import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=100, border=2)

qr.add_data("https://afram.xyz")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("portfolio_code.png")