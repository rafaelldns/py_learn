# my_module.py
def inp_n():
    name = input("Insert a name: ")
    print(f"Hello {name}!")

def cal_id():
    ay = int(input("Insert a current year: "))
    by = int(input("Insert your year of birth: "))
    age = ay - by
    print(f"You are or will be {age} years old this year!")

def cal_su():
    n1 = int(input("Insert first number: "))
    n2 = int(input("Insert a second number: "))
    return n1 + n2
