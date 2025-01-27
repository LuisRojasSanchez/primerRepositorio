nombre_archivo="archivo_ejemplo.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("Este es un archivo de ejempli creado con Python.\n")
    archivo.write("Rojas Sanchez Luis Francisco.\n Tics\n TECNM CAMPUS TLALPAN \n")
    
print(f"El archivo {nombre_archivo} ha sido creado y guardado")