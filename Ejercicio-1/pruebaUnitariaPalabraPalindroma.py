import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):
    
    #Prueba para verificar si la palabra es palindromo
    def test_palindromo_palabra(self):
        print(palindromo("ana"))
        
if __name__ == '__main__':
    unittest.main()