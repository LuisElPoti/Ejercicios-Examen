# Ejercicio 3

x = 0
t = 0

def min_jumps(x):
    if x == 0:
        return 0
    if x < 0:
        return min_jumps(-x)
    s = 0 # Posicion actual luego de k saltos
    k = 0 # Auxiliar para contar los saltos
    saltos = 0
    # Mientras la posicion actual sea menor que x o la diferencia entre la posicion actual y x sea impar
    while s < x or (s - x) % 2 != 0:
       
        k += 1
        s += k
        
        print("s: ", s, "k: ", k)
        
        if s > x:
            k -= 1
            s -= k
        
        saltos += 1
        
    return saltos

# Pruebas
while t < 1 or t > 1000:
    t = int(input("Ingrese el número de casos de pruebas: "))

while x < 1 or x > 106:
    for i in range(t):
        x = int(input("Ingrese el valor de x: "))
        print(min_jumps(x))
        
        