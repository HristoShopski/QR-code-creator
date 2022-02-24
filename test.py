import pyqrcode
import png
from pyqrcode import QRCode

address = input('Paste your url here >>>')

url = pyqrcode.create(address)
url.png('qrcode.png', scale=8)

print(pyqrcode)
