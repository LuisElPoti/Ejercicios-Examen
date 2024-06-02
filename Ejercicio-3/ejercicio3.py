# Ejercicio 3

def validar_numero(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if num < min_val or num > max_val:
                raise ValueError(f"El número debe estar entre {min_val} y {max_val}.")
            return num
        except ValueError as e:
            print(f"Entrada no válida: {e}")

def min_jumps(x):
    if x == 0:
        return 0
    if x < 0:
        return min_jumps(-x)
    
    saltos = 0
    while (saltos * (saltos + 1) < 2 * x):
        saltos += 1
    
    if (saltos * (saltos + 1) / 2 == x + 1):
        saltos += 1
    
    return saltos

def main():
    t = validar_numero("Ingrese el número de casos de pruebas (1-1000): ", 1, 1000)
    
    for _ in range(t):
        x = validar_numero("Ingrese el valor de x (1-106): ", 1, 106)
        print(min_jumps(x))

if __name__ == "__main__":
    main()