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