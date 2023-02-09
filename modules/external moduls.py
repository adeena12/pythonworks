import pyqrcode
from pyqrcode import QRCode

s="hello world"

url=pyqrcode.create(s)
url.svg("testqrcode.svg",scale=8)