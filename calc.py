#program for creating the calculator

def add(a,b):
    print("the addition of ",a,"and",b,"is",a+b)


def sub(a,b):
    print("the subtraction of",a,"and",b,"is",a-b)

def mul(a,b):
    print("the multiplication of",a,"and",b,"is",a*b)
    
def div(a,b):
    if b==0:
        print("the value should be greater than zero")
    else:
        print("the division of",a,"and",b,"is",a/b)

cchoice='y'
while(cchoice=='y' or cchoice=='Y'):
    print("\n =====simple calculator=====")
    print("1.Addition(+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/)")
    

    choice=input("enter the choice (1-4)")

    if choice not in ['1','2','3','4']:
        print("please select a valid option")
        continue

    try:
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
    except ValueError:
        print("Invalid input! enter the numeric values")
        continue

    if choice=='1':
        add(num1,num2)
    
    elif choice=='2':
        sub(num1,num2)
    
    elif choice=='3':
        mul(num1,num2)

    elif choice=='4':
        div(num1,num2)
    
    cchoice=input("do you want to continue y/Y")
print("Thank you for using the calculator!!")
