import secrets # Para generar contraseñas criptográficamente seguras
import string # Para obtener conjuntos de caracteres (letras, dígitos, puntuación)
import hashlib # Para generar hashes SHA-1 (necesario para la API de Have I Been Pwned)
import requests # Para hacer peticiones HTTP a la API de Have I Been Pwned

contraseñasAlmacenadas = {}

def generarContraseñas(longitud,usarSimbolos,usarNumeros):
    caracteres = string.ascii_letters  # Letras mayúsculas y minúsculas
    if usarNumeros:
        caracteres+= string.digits
    if usarSimbolos:
        caracteres += string.punctuation.replace("'", "").replace('"', '').replace('\\', '')
    if longitud < 8:
        print("Advertencia: La longitud mínima recomendada es 8 caracteres.")
        longitud = 8 