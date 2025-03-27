import sys
import os

print("Hello")

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this program is allowed ")

    print("Argument: " + str(sys.argv[1:]))
else:
    print("Argument is not provided")

os.system("dir > test.txt")
sys.exit(2)