import json
import pickle

menu_open = True
list_names_pickle = {
    "list": []
}
list_names_json = {
    "list": []
}


def select_option():
    return input("Select an option: ")


def input_name():
    return input("Type your name: ")


# 3. Save data
def save_as_json():
    with open('list_json.txt', mode="w") as f:
        f.write(json.dumps(list_names_pickle))


def save_as_pickle():
    with open("list_pickle.p", mode="wb") as f:
        f.write(pickle.dumps(list_names_pickle))


# 4. load data
def load_as_json():
    with open("list_json.txt", mode="r") as f:
        file_content = f.readlines()
        global list_names_json
        data = json.loads(file_content[0])
        list_ = data
        update_list = []
        for item in list_['list']:
            update_list.append(item)
        list_names_json['list'] = update_list


def load_as_pickle():
    with open("list_pickle.p", mode="rb") as f:
        global list_names_pickle
        file_content = None
        try:
            file_content = pickle.loads(f.read())
            data = file_content['list']
            list_ = []
            for item in data:
                list_.append(item)
            list_names_pickle['list'] = list_
        except EOFError as e:
            print(e)


load_as_json()
load_as_pickle()

# 1. Infinite loop to retrieve input data
while menu_open:
    print("1. Add name")
    print("2. Print names")
    print("q. Quit")
    option = select_option()
    if option == "1":
        input_name_value = input_name()
        print('input value ', input_name_value)
        list_names_json['list'].append(input_name_value)
        list_names_pickle['list'].append(input_name_value)
        save_as_json()
        save_as_pickle()
    # 2. Print values
    elif option == "2":
        print("List names from json")
        print(list_names_json['list'])
        print("List names from pickle")
        print(list_names_pickle['list'])
    elif option == "q":
        menu_open = False
    else:
        print("Invalid choice")

else:
    print("User left!")
print("Done!")
