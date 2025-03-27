import json

filename = "users.txt"
myfile = open(filename, mode='w', encoding='Latin_1')

player1 = {
    'Name': "Bob Schumacher",
    'Score': 345,
    'Awards': ["Mazda", "Honda", "BMW", "Audi"]

}

player2 = {
    'Name': 'Garry Fischer',
    'Score': 234,
    'Awards': ["Renault", "Peugeout", "Skoda", "VW"]

}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#------------------------SAVE with JSON-----------------------

json.dump(myplayers, myfile)
myfile.close()

#------------------------LOAD with JSON-----------------------

myfile = open(filename, mode='r', encoding='Latin_1')
json_data = json.load(myfile)

for user in json_data:
    print("Player name is:  " + str(user['Name']))
    print("Player score is:  " + str(user['Score']))
    print("Player award #1 is  " + str(user['Awards'] [0]))
    print("Player award #1 is  " + str(user['Awards'][1]))
    print("Player award #1 is  " + str(user['Awards'][2]))
    print("------------------------------------------\n\n")