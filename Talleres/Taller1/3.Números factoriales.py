def factorial(n:int):
    factorial=n
    valor=n
    if(n!=0):
        while(valor>1):
            fact_ant=valor-1
            factorial=factorial*fact_ant
            valor=fact_ant
    else:
        factorial=1
    return (n,factorial)

print("Primeros 20 números factoriales.")
prim_fact=[]
for i in range(20):
    prim_fact.append(factorial(i))
print(prim_fact)

def variaciones_sin(n:int , r:int):
    num=factorial(n)[1]
    dem=factorial((n-r))[1]
    return int(num/dem)

print("Permutaciones 6 carros en 3 estacionamientos:")
print(variaciones_sin(6,3))

def combinaciones_sin(n:int , m:int):
    num=factorial(n)[1]
    dem=factorial(m)[1]*factorial((n-m))[1]
    return int(num/dem)

print("Combinaciones equipos 11 jugadores con 22 disponibles:")
print(f"Cualquiera puede ser arquero: {combinaciones_sin(22,11)}.")
print(f"Ya sabemos quien sera el arquero: {combinaciones_sin(21,10)}.")

