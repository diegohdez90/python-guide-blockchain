list_names = ["John", "Louis", "Marian", "Joseph", "Daniel", "Nelson"]

for name in list_names:
    print(name + " has length of: " + str(len(name)))
    if len(name) > 5:
        print(name)
    if 'n' in name or 'N' in name:
        print(name + " includes N or n")

while len(list_names) > 0:
    list_names.pop()
