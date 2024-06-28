# Definición de la función que multiplica cada elemento de la lista por 2
def lista_cambiada(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2  # Multiplica cada elemento por 2

# Función principal que prueba la función lista_cambiada
def main():
    lista = [1, 2, 3, 4, 5]  # Definición de una lista inicial
    print("antes de la mutación:", lista)  # Imprime la lista original
    lista_cambiada(lista)  # Llama a la función lista_cambiada para modificar la lista
    print("después de la mutación:", lista)  # Imprime la lista modificada

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta como programa principal