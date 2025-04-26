from urllib import request, parse
import sys

myURL = "https://beejwala.com/cdn/shop/files/GladiolusRedColorFlowerBulb_1024x.jpg"
myFile = "C:\\Users\\User\\Downloads\\myGladiolus.jpg"

try:
      print("Start downloading file from: " + myURL)
      request.urlretrieve(myURL, myFile)

except Exception:
    print("Attention sys info")
    print(sys.exc_info())
    exit

print("File downloaded and saved at: " + myFile )