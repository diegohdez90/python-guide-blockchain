name = input("Enter your name: ")
age = input("Enter your age: ")

def concat(name, age):
    print('My name is '+ name +' and I\'m ' + age)

def any_concat(age, name = "John Doe"):
    print('My name is '+ name +' and I\'m ' + age)

def decades_lived(age):
    return int(int(age)//10)

concat(name, age)
any_concat(age="33")
decades= decades_lived(age)

print('I live '+ str(decades) + "decades")
