#DICCIONARIOS

Familiares= {18594799: "Monica", 46032044: "Angeles", 36598245: "Natalia", 40325544: "Camila"}

print(Familiares[46032044])

Familiares[3265879] = "Rosa"
Familiares[34897562] = "Santiago"
Familiares[32411233] = "Carla"

print(Familiares)

import random

nombres = ["Ramiro", "Martin", "Lautaro", "Sofia"]
telefonos = {}

for nombre in nombres:
    numero_telefono = "".join([str(random.randint(0, 9))for _ in range(9)])
    telefonos[nombre] = numero_telefono 
    
print("Diccionario de Teléfonos:")
for nombre, telefonos in telefonos.items():
    print(f"Nombre: {nombre} - Teléfono: {telefonos}")
    