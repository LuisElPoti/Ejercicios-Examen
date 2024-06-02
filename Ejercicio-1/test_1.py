import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):
    
    #Prueba para verificar si la frase es palindromo
    def test_palindromo_frase(self):
        print(palindromo("Anita lava la tina"))
        
if __name__ == '__main__':
    unittest.main()