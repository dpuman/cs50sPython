people = [
    {'name': 'Dipu', 'house': 'Gryffendor'},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]


# def function(person):
#     return person['name']


# people.sort(key=function)


people.sort(key=lambda person: person['name'])

print(people)
