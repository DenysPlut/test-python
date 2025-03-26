
filename = "Lessons_List.txt"

try:
    print("Inside TRY")
    myfile = open(filename, mode='r', encoding='Latin-1')
except Exception:
    print("Inside EXCEPT")
    print("Error FOUND!")
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")

    print("============================EOF==============================")

