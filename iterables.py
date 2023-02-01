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
