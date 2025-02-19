cars = ['bmw', 'mercedes','porsche', 'audi', 'volkswagen']

for x in cars:
    print(x.upper())


mynumber_list = (list(range(0,10)))
print(mynumber_list)
print("===================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)
print("Max number list:" + str(max(mynumber_list)))
print("Min number list:" + str(min(mynumber_list)))
print("Sum of the list:" + str(sum(mynumber_list)))

my_cars = cars[1:3]
print(my_cars)
my_cars = cars[:3]
print(my_cars)
my_cars = cars[-3:-2]
print(my_cars)