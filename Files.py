from os import write

inputfile = "names.txt"
outputfile ="mynames.txt"

word_lookfor = "Fergusson"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, x in enumerate(myfile1, 1):
    if word_lookfor in x:
        print("Line N: " + str(num) + " : " + x.strip())
        myfile2.write("Name found " + x)

myfile1.close()
myfile2.close()



