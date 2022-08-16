#Fibonacci
import numpy as np
from matplotlib import pyplot as plt 
#Punto 1
#Recibe como input el número de valores de la serie a calcular.
def  fibonacci(v_0:int, v_1:int):
    valor_0=v_0
    valor_1=v_1
    valor_nuevo=valor_0+valor_1
    return valor_nuevo
def arr_fibonacci(n:int):
    lista_fibonacci=[]
    valor_ant=0
    valor_prev=0
    for i in range(n):
        if(i<=1):
            v_n=fibonacci(valor_ant,valor_prev)
            lista_fibonacci.append([i,v_n])
            valor_prev=1
        else:
            v_n=fibonacci(valor_ant,valor_prev)
            lista_fibonacci.append([i,v_n])
            valor_ant=valor_prev
            valor_prev=v_n
    array_fib=np.array(lista_fibonacci)
    return array_fib

print(arr_fibonacci(20))
#Punto 2
#Recibe por parámetro el número de pasos dentro de la sucesión de Fibonacci para la gráfica.
for theta in np.linspace(0,np.pi,100):
        r = ((theta)**2)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
plt.plot(x,y)
#Punto 3
#Recibe por parámetro el número de pasos dentro de la sucesión de Fibonacci para calcular el número aureo.
def numero_aureo(n:int):
    valor_ant=0
    valor_prev=0
    for i in range(n):
        if(i<=1):
            v_n=fibonacci(valor_ant,valor_prev)
            valor_prev=1
        else:
            v_n=fibonacci(valor_ant,valor_prev)
            valor_ant=valor_prev
            valor_prev=v_n
    aureo=(valor_prev/valor_ant)
    return aureo

aureo_cte=(1+(5**(1/2)))/2
aureo_calc=numero_aureo(1000)

print(aureo_calc,aureo_calc-aureo_cte)