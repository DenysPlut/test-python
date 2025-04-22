from urllib import request

myUrl = "http://www.astahov.net"

answer = request.urlopen(myUrl)

mytext1 = answer.readlines()
mytext2 = answer.read()

print(answer)
print(mytext2)

for line in mytext1:
    print(line)