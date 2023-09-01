# Ejercicio 1
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# Solicitar al usuario un nmero entre 1 y 12
numero = int(input("Ingrese un numero entre 1 y 12: "))

# Verificar si el número está dentro del rango válido
if numero >= 1 and numero <= 12:
    # Mostrar el mes correspondiente
    mes = meses[numero - 1]
    print(f"El mes correspondiente al numero {numero} es {mes}.")
else:
    print("Numero fuera de rango, ingrese del 1 al 12")



#Ejercicio2
cadena = input("Ingrese una cadena de texto: ")
palabras = cadena.split()
cantidad_palabras = len(palabras)

# Mostrar el resultado
print("La cadena tiene", cantidad_palabras, "palabras")


#Ejercicio3
# Inicializar una lista para almacenar las notas
notas = []

# Solicitar al usuario las 5 notas
for i in range(5):
    nota = float(input("Ingrese la nota " + str(i + 1) + " (entre 0 y 10): "))
    # Verificar que la nota esté dentro del rango válido
    if nota < 0 or nota > 10:
        print("Nota fuera de rango. Debe ingresar una nota entre 0 y 10.")
        break
    notas.append(nota)

# Verificar si se han ingresado todas las notas válidas
if len(notas) == 5:
    print("\nNotas ingresadas:")
    for i, nota in enumerate(notas):
        print("Nota", i + 1, ":", nota)

    nota_media = sum(notas) / len(notas)
    print("\nNota media:", nota_media)

    nota_maxima = max(notas)
    nota_minima = min(notas)
    print("Nota mas alta:", nota_maxima)
    print("Nota mas baja:", nota_minima)
