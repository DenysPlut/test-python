import sys

filename = "Lessons_List.txt"

while True:

   try:
       print("Inside TRY")
       myfile = open(filename, mode='r', encoding='Latin-1')
   except Exception:
       print("Inside EXCEPT")
       print("Error FOUND!")
       filename = input("Enter correct filename! : ")
   else:
       print("Inside ELSE")
       print(myfile.read())
       sys.exit()
   finally:
       print("Inside FINALLY")

       print("============================EOF==============================")

