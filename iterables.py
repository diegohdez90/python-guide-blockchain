# 1 user list
users_dict = [{
    'name': 'Diego',
    'age': 32,
    'hobbies': ['coding', 'watching movies', 'walk']
}, {
    'name': 'John',
    'age': 23,
    'hobbies': ['snowboarding', 'swimming'],
}, {
    'name': 'Sarah',
    'age': 19,
    'hobbies': ['writing', 'painting']
}, {
    'name': 'Max',
    'age': 30,
    'hobbies': ['teaching']
}, {
    'name': 'Ana',
    'age': 20,
    'hobbies': ['studying', 'read novels']
}, {
    'name': 'Diana',
    'age': 15,
    'hobbies': ['playing video games']
}, {
    'name': 'Daniel',
    'age': 17,
    'hobbies': ['sci-fi topics']
}]

# 2 List of names
name_list = [user.get('name') for user in users_dict]

print(name_list)

# 3 List of user older than 20
older_than_twenty_list = [user.get('name')
                          for user in users_dict if user.get('age') > 20]

print(older_than_twenty_list)


# 4 Copy list and update first user name
comprehensive_list = users_dict[:]
for (index, user) in enumerate(comprehensive_list):
    if index != 0:
        continue
    copy_user = user.copy()
    copy_user.update((k, 'Arturo')
                     for k, v in copy_user.items() if k == 'name')
    comprehensive_list[index] = copy_user

print(comprehensive_list[0])
print(users_dict[0])

# 5 Unpack the dicts attributes
for user in users_dict:
    name, age, hobbies = user.values()
    print('Name: ' + name)
    print('Age: ' + str(age))
    print('Hobbies: ' + str(hobbies))


print("-" * 20)

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

persons = [{ 'name' : 'ABC', 'age': 22, 'hobbies' : ['listning Music', 'dancing'] } ,
          { 'name' : 'PQR', 'age': 23, 'hobbies' : ['reading', 'dancing'] }, 
          { 'name' : 'XYZ', 'age': 24, 'hobbies' : ['painting', 'dancing', 'travelling']} ]

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

person_names = [names['name'] for names in persons]
print (person_names)

# 3) Use a list comprehension to check whether all persons are older than 20.

person_age = all([names['age']>20 for names in persons])
print(person_age)

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

#duplicat_persons_list = [person for person in persons]
#duplicat_persons_list[0]['name'] = 'XXX'
#print(duplicat_persons_list)
#print(persons)

duplicat_persons_list = []
for person in persons:
    duplicat_persons_list.append(person.copy())
duplicat_persons_list[0]['name'] = 'XXX'
print("*"*50)
print(duplicat_persons_list)
print("*"*50)
print(persons)
print("*"*50)

# 5) Unpack the persons of the original list into different variables and output these variables.

person_a, person_b, person_c = persons
print(person_a)
print(person_b)
print(person_c)