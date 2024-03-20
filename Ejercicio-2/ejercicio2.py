# Problema Formula 1

def score():
    G, Q = map(int, input().split())
    if G == 0:
        return 0
    
    g = [[0] * 105 for i in range(105)]
    
    for i in range(G):
        row = list(map(int, input().strip().split()))
        for j, x in enumerate(row):
            g[i][x - 1] = j + 1
            
    S = int(input().strip())
    for i in range(S):
        score = [0] * 105
        K = int(input().strip())
        for j in range(K):
            row = list(map(int, input().strip().split()))
            for p in range(G):
                score[g[p][row[p] - 1]] += row[p]
                
        mx = max(score)
        first = True
        for i in range(1, Q + 1):
            if score[i] == mx:
                if first:
                    print(i, end="")
                    first = False
                else:
                    print(" ", i, end="")
        print()

score()