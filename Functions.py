from http.client import responses


def print_congrats(name):
    print("Congrats" " " + name + " " "Wish you all the best!")
    print("Hello")

def factorial(x):
    response = 1
    for i in range(1, x+1):
        response = response * i
    return response


print_congrats("Denys")
print_congrats("Max")

for i in range(1, 100):
    print(str(i) + "!\t = " + str(factorial(i)))
print(factorial(1))
print(factorial(7))



