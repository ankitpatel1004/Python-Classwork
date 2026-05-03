import qrcode
img = qrcode.make('https://google.com')
img.save("my_qr_code.png")

