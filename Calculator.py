# Menu for showing operation list
def menu():
    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")
    print("5. % ")

#Calculating Operations
def calculate(choice,num1,num2):
    if choice==1:
        return num1+num2 
    elif choice==2:
        return num1-num2
    elif choice==3:
        return num1*num2
    elif choice==4:
        return num1/num2
    elif choice==5:
        return num1%num2
    else:
        return "Enter valid Choice"


menu()
choice=int(input("Enter Ur Choice = "))
num1=eval(input("Enter num 1 ="))
num2=eval(input("Enter num 2 ="))

print(calculate(choice,num1,num2))

