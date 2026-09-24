#function that adds two numbers
def add(x,y):
    print(x+y)
#function that subtracts two numbers
def subtract(x,y):
    print(x-y)
#function that multiplies two numbers
def multiply(x,y):
    print(x*y)
#function that divideds two numbers
def divide(x,y):
    print(x/y)
x = int(input("Enter the First Number: "))
y = int(input("Enter the Second Number: "))
add(x,y)
subtract(x,y)
multiply(x,y)
divide(x,y)
#Start of the Program
print("Welcome to calc")
print("What do you want to do")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")
calc_choice = input(": ")
print(calc_choice)
x = int(input("Enter the First Number: "))
y = int(input("Enter the Second Number: "))
while(1): 
    if calc_choice == 'a':
        add(x,y)
    elif calc_choice == 's':
        subtract(x,y)
    elif calc_choice == 'm':
        multiply(x,y)
    elif calc_choice == 'd': 
        divide(x,y)
    elif calc_choice == 'q':
        print("Bye!")
        break
    else:
        print("Invalid input")
        
        


