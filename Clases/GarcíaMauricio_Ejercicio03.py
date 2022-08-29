import numpy as np
import matplotlib.pyplot as plt

def funcion(x,c):
    f_x = 1- np.exp(-c*x) -x
    return f_x
def derivada_central(f,x,h,c):
    d_f= (f(x+h,c)-f(x-h,c))/(2*h)
    return d_f
def NewtonRapson(f,x_0,h,c):
    precision=h
    x_p=x_0
    error=1
    it=0
    itmax=int(1/h)
    while(error>precision and it<itmax):
        try:
            x_n = x_p - (f(x_p,c)/derivada_central(f,x_p,h,c))
            error=np.abs(f(x_n,c))/np.abs(derivada_central(f,x_n,h,c))
        except ZeroDivisionError:
            print("División por cero.")
        x_p=x_n
        it+=1
    if(it==itmax):
        return False
    else:
        return x_n
c=2
solution_a=NewtonRapson(funcion,1,1e-6,c)
c_values= np.linspace(0,3,300)
f_nr=np.zeros(300)
for i in range(len(c_values)):
    f_i=NewtonRapson(funcion,1,1e-6,c_values[i])
    f_nr[i]=f_i
print(f"La solución de la ecuacion para c = {c} es {solution_a}")
plt.plot(c_values,f_nr)
plt.title("Raíz de $x=1-e^{-cx}$ encontradas en función de c")
plt.xlabel("c")
plt.ylabel("Raíz encontrada para $x=1-e^{-cx}$")
plt.savefig("GarcíaMauricio_Ejercicio3")