import unittest
from ejercicio2 import main

"""
Para esta prueba unitaria debe ingresar los siguientes inputs en este orden

3 10
1 2 3 4 5 6 7 8 9 10
10 1 2 3 4 5 6 7 8 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
0 0

Cada una de estas lineas representa algo especifico:
1. La primera linea contiene dos enteros separados por un espacio: G y P, que indican el número 
   de Grandes Premios y el número de pilotos respectivamente.
   
2. Las siguientes G líneas representan los resultados de cada carrera. Cada línea contiene Q enteros 
   separados por espacios, donde el i-ésimo número indica el orden de llegada del piloto i en esa carrera. 

3. La siguiente línea contiene un solo entero S, indicando el número de sistemas de puntuación.

4. A continuación, cada una de las siguientes S líneas contiene una descripción de un sistema de 
puntuación. Cada descripción comienza con un entero K, seguido de K enteros separados por espacios, 
que indican los puntos asignados para cada posición.

"""

class TestScore(unittest.TestCase):
    def test_score(self):
        main()

if __name__ == '__main__':
    unittest.main()
    