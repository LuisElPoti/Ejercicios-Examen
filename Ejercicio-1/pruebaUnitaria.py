#Pruebas unitarias
import unittest
from ejercicio1 import palindromo

class TestPalindromo(unittest.TestCase):
    
    #Prueba para verificar si la palabra es palindromo
    def test_palindromo_palabra(self):
        self.assertEqual(palindromo("ana"), "La palabra es palindromo")

    #Prueba para verificar si la frase es palindromo
    def test_palindromo_frase(self):
        self.assertEqual(palindromo("Anita lava la tina"), "La palabra es palindromo")
    
    #prueba para verificar si la palabra o frase no es palindromo
    def test_no_palindromo(self):
        self.assertEqual(palindromo("Hola mundo"), "La palabra o frase no es palindromo")

if __name__ == '__main__':
    unittest.main()