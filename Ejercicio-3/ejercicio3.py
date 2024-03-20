# Ejercicio 3

x = 0
t = 0

def min_jumps(x):
    if x == 0:
        return 0
    if x < 0:
        return min_jumps(-x)
    
    saltos = 0
    while (saltos * (saltos + 1) < 2 * x):
        saltos +=1
    
    if (saltos * (saltos + 1) / 2 == x + 1):
        saltos +=1
    
    
        
    return saltos

# Pruebas
while t < 1 or t > 1000:
    t = int(input("Ingrese el número de casos de pruebas: "))

while x < 1 or x > 106:
    for i in range(t):
        x = int(input("Ingrese el valor de x: "))
        print(min_jumps(x))
        
        