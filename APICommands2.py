from urllib import request, parse
import sys
from urllib.parse import urlencode

myUrl = "https://www.google.com/search?"
value = {'q': "ANDESA soft"}

#User agent has to be added from the browser.
#myheader = {}
#myheader["User-Agent"] = ""


try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    output = request.urlopen(req)
    output = output.readlines()
    for line in output:
        print(line)
except Exception:
    print("Error occured during web request!")
    print(sys.exc_info()[1])