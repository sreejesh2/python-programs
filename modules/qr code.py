import pyqrcode

s = 'sreejesh vs'

url = pyqrcode.create(s)
url.svg("testqr.svg",scale=8)