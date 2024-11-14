inferior = int(input("Limite inferior: "))
superior = int(input("Limite superior: "))
primos = []
for num in range(inferior, superior):
    if num > 1:
        for i in range(2, num):
            if num % i ==0:
                break
        else:
            primos.append(num)
print(primos)
#print(f'Os numeros primos entre {inferior} e {superior} sao: {primos}')
print("Na lista temos {} numeros".format(len(primos)))
print("O numero primo na posicao que precisa eh: {}".format(primos[int(input("position: "))]))
mersenne = []
for j in primos:
    mn = 2**j -1
    if mn in primos:
        mersenne.append(mn)
print('Temos {} mersenne numbers'.format(len(mersenne)))

