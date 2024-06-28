#Crear una función que calcule el factorial de un número

def factorial(n):  # Define una función llamada factorial que calcula el factorial de n
    if n == 0:  # Verifica si n es igual a 0
        return 1  # Retorna 1 si n es igual a 0 (condición base del factorial)
    return n * factorial(n - 1)  # Retorna n multiplicado por factorial(n - 1)

number = int(input("Ingrese un número: "))  # Solicita al usuario ingresar un número y lo convierte a entero
print(f"El factorial de {number} es {factorial(number)}")  # Imprime el resultado del factorial del número ingresado