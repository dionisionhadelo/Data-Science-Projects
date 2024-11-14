import random
import numpy as np
import matplotlib.pyplot as plt

horiz = np.array(range(200))/200.0# linhas do quadrado
yy = np.ones(200)
plt.plot(horiz , yy, 'b')
vert = np.array(range(200))/200.0
xx = np.ones(200)
plt.plot(xx , vert, 'b')


inside = 0
i=1
n=int(input("Intriduza o numero de pontos: "))
while (i<=n):  
    x = random.random()  
    y = random.random()  
    if ((x**2)+(y**2))<=1:    
        inside+=1    
        plt.plot(x , y , 'go') 
    else:    
        plt.plot(x , y , 'ro')  
    i+=1
pi=(4*inside)/n
print ("O valor de pi vale:", end = '')
print(pi)
plt.show()