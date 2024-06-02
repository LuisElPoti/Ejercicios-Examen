# Ejercicio 4

def get_valid_input(prompt, expected_type=int):
    while True:
        try:
            value = expected_type(input(prompt))
            return value
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def get_race_results(G, P):
    results = []
    print("\nResultados de las carreras")
    for _ in range(G):
        while True:
            try:
                resultado = list(map(int, input().strip().split()))
                if len(resultado) != P:
                    raise ValueError("Número de pilotos incorrecto.")
                results.append(resultado)
                break
            except ValueError as e:
                print(f"Entrada no válida: {e}")
    return results

def get_scoring_systems(S):
    systems = []
    print("\nSistema de puntaje")
    for _ in range(S):
        while True:
            try:
                sistema = list(map(int, input().strip().split()))[1:]
                systems.append(sistema)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un sistema de puntaje válido.")
    return systems

def calculate_scores(G, P, results, systems):
    ganadoresTodos = []
    for sistema in systems:
        puntajes = [0 for _ in range(P)]
        for resultado in results:
            for piloto, posicion in enumerate(resultado, start=1):
                if posicion <= len(sistema):
                    puntajes[piloto - 1] += sistema[posicion - 1]

        max_puntaje = max(puntajes)
        ganadores = [i + 1 for i, puntaje in enumerate(puntajes) if puntaje == max_puntaje]
        ganadoresTodos.append(ganadores)
    return ganadoresTodos

def print_winners(ganadoresTodos):
    print("\nLos ganadores son: ")
    for ganadores in ganadoresTodos:
        print(" ".join(map(str, ganadores)))

def main():
    while True:
        print("Carreras y pilotos")
        try:
            G, P = map(int, input().split())
        except ValueError:
            print("Entrada no válida. Por favor, ingrese dos números separados por un espacio.")
            continue

        if G == 0 and P == 0:
            break
        
        results = get_race_results(G, P)
        S = get_valid_input("\nNúmero de sistemas de puntajes: ", int)
        systems = get_scoring_systems(S)
        
        ganadoresTodos = calculate_scores(G, P, results, systems)
        print_winners(ganadoresTodos)

if __name__ == "__main__":
    main()

