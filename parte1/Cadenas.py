# Definición de la función 'invertir' que recibe una cadena y devuelve su inverso
def invertir(cadena):
    return cadena[::-1]  # Retorna la cadena invertida usando slicing

cadena = input("Ingresa una cadena: ")  # Solicita al usuario ingresar una cadena y la guarda en 'cadena'
M = invertir(cadena)  # Llama a la función 'invertir' con 'cadena' y guarda el resultado en 'M'
print("La cadena invertida es:", M)  # Imprime la cadena original y su versión invertida, almacenada en 'M'