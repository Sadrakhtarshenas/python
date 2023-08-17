# # import qrcode 
# # # qrcode.create(content, error='H', version=None, mode=None, encoding=None)
# # import pyqrcode 
# # from pyqrcode import QRCode 
  
  
# # # String which represent the QR code 
# # s = "www.geeksforgeeks.org"
  
# # # Generate QR code 
# # url = pyqrcode.create(s) 
  
# # # Create and save the png file naming "myqr.png" 
# # url.svg("myqr.svg", scale = 8) 
# import qrcode
# text = "MrPython.blog.ir"
# qr = qrcode.make(text)
# qr.save("my_qrcode.png")

# import decode
# from PIL import Image
# picture = Image.open("my_qrcode.png")
# qr = decode(picture)
# text = qr[0].data.decode()
# print("Text : {}".format(text))

import pyqrcode
from pyqrcode import QRCode
qr = 'akhtarshenassadra319@gmail.com'
new_qr = pyqrcode.create(qr)
new_qr.svg('sadra_python.svg')
