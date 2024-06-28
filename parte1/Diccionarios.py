agenda = {}  # Creamos un diccionario vacío llamado agenda

# Agregamos entradas al diccionario agenda
agenda["Zosimo"] = "961062795"
agenda["Edwin"] = "987654321"
agenda["Arath"] = "955123456"

nombre_buscar = "Edwin"  # Definimos la cadena 'Edwin' como nombre a buscar

# Verificamos si nombre_buscar está en el diccionario agenda
if nombre_buscar in agenda:
    # Si está presente, imprimimos el teléfono correspondiente
    print(f"Teléfono de {nombre_buscar}: {agenda[nombre_buscar]}")
else:
    # Si no está presente, imprimimos un mensaje de contacto no encontrado
    print("Contacto no encontrado.")