import re

input_filename = "reg-emails.txt.txt"
result_filename = "results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_filename,mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(lookfor, mytext)

for item in result:
    print(item)
    resultfile.write(item)



print("Total: " + str(len(result)))