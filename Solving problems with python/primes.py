lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
primos = [] 
mersennes = []
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0: 
               break  
       else:  
           #print(num) 
           primos.append(num) 
print("The prime numbers are: ", end = " ")
print(primos)
print()
for j in primos:
    sp = 2 ** j - 1
    if sp in primos:
        mersennes.append(sp)
print("The mersenne numbers are: ", end = ' ')
print(mersennes)