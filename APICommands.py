from urllib import request

myUrl = "https://ukr.net"

answer = request.urlopen(myUrl)

mytext1 = answer.readlines()
mytext2 = answer.read()

print(answer)
print(mytext2)

for line in mytext1:
    print(line)