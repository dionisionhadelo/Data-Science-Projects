inferior = int(input("Digite o limite inferior: "))
superior = int(input("Digite o limite superior: "))
for i in range(inferior, superior):
    if i % 2 == 0:
        print(f'{i} is a even number')
    else:
        print(f'{i} is a odd number')