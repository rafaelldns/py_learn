condition1 = False
#if condition is False, nothing happens

def fun():
    if condition1:
        raise Exception("Condition is True")
    else :
        print("Condition is false, nothing happens")
    
try:
    fun()
except Exception as e:
    print(f"Error: {str(e)}")

condition2 = True
#if condition is True, the function throws an error with raise
#'try' block catch this error
#'except' print "Error: Condition is True"

def fun1():
    if condition2:
        raise Exception("Condition is True")
    else :
        print("Condition is False")
    
try:
    fun1()
except Exception as c:
    print(f"ERROR: {str(c)}")


print("\nReal Example")

balance = 1200.00
print("Your balance is", balance)
value = float(input("How much do you want to draw? "))

def withdraw(balance, value):
    if value > balance:
        raise Exception("Insufficient Balance!")
    else :
        print("Successful Withdrawal")
        draw = balance - value
        print("Your current balance is:", draw)
        
try:
    withdraw(balance, value)
except Exception as v:
    print(f"ERROR: {str(v)}")
