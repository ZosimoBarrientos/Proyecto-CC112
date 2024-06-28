with open('datos.txt', 'w') as archivo_salida:  # Abre el archivo 'datos.txt' en modo de escritura ('w') y lo asigna a archivo_salida
    archivo_salida.write('Hola grupo!\n')  # Escribe la cadena 'Hola grupo!' seguida de un salto de línea en el archivo
    archivo_salida.write('No quiero ser bika :c\n')  # Escribe la cadena 'No quiero ser bika :c' seguida de un salto de línea en el archivo

with open('datos.txt', 'r') as archivo_entrada:  # Abre el archivo 'datos.txt' en modo de lectura ('r') y lo asigna a archivo_entrada
    for linea in archivo_entrada:  # Itera sobre cada línea del archivo
        print(f'Línea leída: {linea.rstrip()}')  # Imprime cada línea del archivo eliminando los espacios en blanco al final (rstrip())