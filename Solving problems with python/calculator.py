print("Hello User!")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("""
[1]: To Add
[2]: To Sub
[3]: To Mult
[4]: To Div
[5]: To Quit Calculator
""") 
option = 0
while option != 5:
    option = int(input("Which option do you want? "))


    if option == 1:
        print(f'The answer is {n1 + n2}')

    elif option == 2:
        print(f'The answer is {n1 - n2}')

    elif option == 3:
        print(f'The answer is {n1 * n2}')

    elif option == 4:
        try:
            sum = n1 / n2 
        except ZeroDivisionError:
            print("STOP!. You can't Divide a number by Zero!!!")
    elif option == 5:
        print(f'End of the Calculator Program!')
    else: 
        print("invalid choice")
print(f'GOODBYE!')

            

    