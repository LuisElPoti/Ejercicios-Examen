import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):
    
    #prueba para verificar si la palabra o frase no es palindromo
    def test_no_palindromo(self):
        print(palindromo("Hola mundo"))
        
if __name__ == '__main__':
    unittest.main()