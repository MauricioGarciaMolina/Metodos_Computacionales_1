#Librerias usadas
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

def esPrimo(n:int):
    i=int(np.sqrt(n))
    noPrimo=False
    while(i>1 and noPrimo==False):
        cociente=n%i
        if(cociente==0):
            noPrimo=True
        i=i-1
    if(noPrimo==False):
        return n
            
lista_primos=[]
n=2
while(len(lista_primos)<1000):
    rta=esPrimo(n)
    if(rta==n):
        lista_primos.append(rta)
    n+=1

array_primos=np.array(lista_primos[0:10])
print(array_primos)
x=range(len(lista_primos))
y=np.array(lista_primos)
plt.plot(x,y)