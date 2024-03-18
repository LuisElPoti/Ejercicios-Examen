def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    return "La palabra es palindromo" if palabra == palabra[::-1] else "La palabra o frase no es palindromo"

