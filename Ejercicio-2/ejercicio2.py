# Problema Formula 1

def score():
    G, P = 1, 1
    ganadoresTodos = []
    while True:
        print("Carreras y pilotos")
        G, P = map(int, input().split())
        
        if(G == 0 and P == 0):
            break
        
        results = []
        print("\nResultados de las carreras")
        for i in range(G):
            resultado = list(map(int, input().strip().split()))
            results.append(resultado)
        
        print("\nNúmero de sistemas de puntajes")
        S = int(input().strip())
        
        print("\nSistema de puntaje")
        for i in range(S):
            
            
            sistema = list(map(int, input().split()))[1:]
            puntajes = [0 for _ in range(P)]
            
            for resultado in results:
                for piloto, posicion in enumerate(resultado, start=1):
                    if posicion <= len(sistema):
                        puntajes[piloto - 1] += sistema[posicion - 1]
            
            max_puntaje = max(puntajes)
            
            ganadores = []
            
            for score, puntaje in enumerate(puntajes):
                if puntaje == max_puntaje:
                    ganadores.append(score + 1)
            
            ganadoresTodos.append(ganadores)
    
    print("\nLos ganadores son: ")
    for ganadores in ganadoresTodos:
        print(" ".join(map(str, ganadores)))
        
score()

