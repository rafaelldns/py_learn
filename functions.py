# Functions encapsulates tasks and executes them when requested

print("Defining and calling functions")

def func():
    print("First function")

func()

print("\nParameters and Arguments")

def pa(nome):
    print(f"Hello, {nome}!")

pa("Tulio")

print("\nReturn Values")

def su(a, b) :
    return a + b

result = su(23,27)
print(result)

print("\nAnonymous Functions")

pw = lambda x: x**2
print(pw(4))

print("\nScope of variables")

def fun():
    local_variable = 100
    #local acess, cant call "print(local_variable)"
    print(local_variable)

global_variable = 200

def fun2():
    print(global_variable)

fun()
fun2()

print(global_variable)

print("\nUser-defined Functions")

def media_calc(*num):
    suma = sum(num)
    lena = len(num)
    media = suma/lena
    return media

print("Media is: ", media_calc(3, 6, 9, 12))

def ex(x):
    return x + 10
#example replacing def ex with exf lambda
exf = lambda x: x + 10
print(exf(5))


print("\nDocStrings")

def triangle_area(base, height):
    """
    Calculate the area of the triangle 
    Args:
        base(float)triangle base + height(float)triangle height
    Returns:
        float: triangle area
    """
    return (base*height)/2

print(triangle_area(6, 4))

print("\nVariable Args")

def variable_sum(*numbers):
    suma = 0
    for x in numbers:
        suma += x
    return suma

print(variable_sum(2, 4, 6))
print(variable_sum(1, 3, 5, 7, 9))
