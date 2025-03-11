def create_record(name, telephone, address):
    record = {
        'name': name,
        'telephone': telephone,
        'address': address
    }
    return record
user1 =create_record('Rohan', '10420420944222', 'Kaufberg')
user2 =create_record('Benatal','14010909090900', 'Tormanz')

print(user1)
print(user2)

def give_award(medal, *persons):
    for person in persons:
        print('Volunteer ' + person.title() + ' applied for ' + medal)

give_award('100 gold', 'Benatal' ,'Rohan')
give_award('200 gold','Rohan', 'Gustav','Ulrich')