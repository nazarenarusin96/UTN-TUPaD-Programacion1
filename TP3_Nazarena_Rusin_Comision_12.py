#!/usr/bin/env python3

"""
TP3 - Estructuras condicionales
Alumna: Nazarena Rusin 
Comisión: 12
"""

import random
from statistics import mode, median, mean

def ejercicio_1():
    edad = input("Ejercicio 1 - Ingrese su edad: ")
    try:
        edad = int(edad)
        if edad > 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad (no tiene más de 18 años)")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

def ejercicio_2():
    nota = input("Ejercicio 2 - Ingrese su nota (numérica): ")
    try:
        nota = float(nota)
        if nota >= 6:
            print("Aprobado")
        else:
            print("Desaprobado")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")

def ejercicio_3():
    valor = input("Ejercicio 3 - Ingrese un número (se aceptan pares únicamente): ")
    try:
        n = int(valor)
        if n % 2 == 0:
            print("Ha ingresado un número par")
        else:
            print("Por favor, ingrese un número par")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

def ejercicio_4():
    edad = input("Ejercicio 4 - Ingrese su edad: ")
    try:
        edad = int(edad)
        if edad < 12:
            categoria = "Niño/a"
        elif 12 <= edad < 18:
            categoria = "Adolescente"
        elif 18 <= edad < 30:
            categoria = "Adulto/a joven"
        else:
            categoria = "Adulto/a"
        print(f"Categoría: {categoria}")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

def ejercicio_5():
    pwd = input("Ejercicio 5 - Ingrese una contraseña (8-14 caracteres inclusive): ")
    longitud = len(pwd)
    if 8 <= longitud <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    try:
        mda = mode(numeros_aleatorios)
    except Exception:
        from collections import Counter
        counts = Counter(numeros_aleatorios)
        max_freq = max(counts.values())
        modos = [val for val, freq in counts.items() if freq == max_freq]
        mda = min(modos)
    med = median(numeros_aleatorios)
    avg = mean(numeros_aleatorios)
    print("Lista generada (50 números 1-100):")
    print(numeros_aleatorios)
    print(f"Moda: {mda}\nMediana: {med}\nMedia (promedio): {avg:.2f}")
    if avg > med and med > mda:
        print("Distribución con sesgo positivo (a la derecha)")
    elif avg < med and med < mda:
        print("Distribución con sesgo negativo (a la izquierda)")
    elif avg == med == mda:
        print("Sin sesgo (media = mediana = moda)")
    else:
        print("No se cumple exactamente ninguno de los criterios simples de sesgo definidos (caso mixto o ambiguo).")

def ejercicio_7():
    texto = input("Ejercicio 7 - Ingrese una frase o palabra: ")
    if texto == "":
        print("Cadena vacía ingresada.")
        return
    if texto[-1].lower() in "aeiouáéíóú":
        texto += "!"
    print("Resultado:", texto)

def ejercicio_8():
    nombre = input("Ejercicio 8 - Ingrese su nombre: ")
    opcion = input("Ingrese 1 para MAYÚSCULAS, 2 para minúsculas, 3 para Primera letra mayúscula: ")
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.capitalize())
    else:
        print("Opción inválida. Debe ingresar 1, 2 o 3.")

def ejercicio_9():
    mag = input("Ejercicio 9 - Ingrese la magnitud del terremoto (ej: 4.5): ")
    try:
        mag = float(mag)
        if mag < 3:
            cat = "Muy leve (imperceptible)"
        elif 3 <= mag < 4:
            cat = "Leve (ligeramente perceptible)"
        elif 4 <= mag < 5:
            cat = "Moderado (sentido por personas, generalmente no causa daños)"
        elif 5 <= mag < 6:
            cat = "Fuerte (puede causar daños en estructuras débiles)"
        elif 6 <= mag < 7:
            cat = "Muy Fuerte (puede causar daños significativos)"
        else:  # mag >= 7
            cat = "Extremo (puede causar graves daños a gran escala)"
        print(f"Clasificación: {cat}")
    except ValueError:
        print("Entrada inválida. Ingrese un número (por ejemplo 4.5).")

def ejercicio_10():
    hemisferio = input("Ejercicio 10 - ¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
    mes = input("Ingrese el mes (nombre o número, ej 'marzo' o '3'): ").strip().lower()
    dia = input("Ingrese el día (número): ").strip()
    meses_map = {
        "enero":1, "febrero":2, "marzo":3, "abril":4, "mayo":5, "junio":6,
        "julio":7, "agosto":8, "septiembre":9, "setiembre":9, "octubre":10, "noviembre":11, "diciembre":12
    }
    try:
        if mes.isdigit():
            m = int(mes)
        else:
            m = meses_map.get(mes, None)
            if m is None:
                print("Mes inválido.")
                return
        d = int(dia)
    except ValueError:
        print("Entrada inválida en mes o día.")
        return


    fecha = (m, d)
    if (m == 12 and d >= 21) or (m in (1,2)) or (m == 3 and d <= 20):
        estacion_n = "Invierno"
    elif (m == 3 and d >= 21) or (m in (4,5)) or (m == 6 and d <= 20):
        estacion_n = "Primavera"
    elif (m == 6 and d >= 21) or (m in (7,8)) or (m == 9 and d <= 20):
        estacion_n = "Verano"
    elif (m == 9 and d >= 21) or (m in (10,11)) or (m == 12 and d <= 20):
        estacion_n = "Otoño"
    else:
        estacion_n = "Fecha fuera de rango (revisar día/mes)"

    if hemisferio == "N":
        print(f"Usted está en el hemisferio Norte. Estación: {estacion_n}")
    elif hemisferio == "S":
        opposites = {"Invierno":"Verano", "Primavera":"Otoño", "Verano":"Invierno", "Otoño":"Primavera"}
        estacion_s = opposites.get(estacion_n, "Desconocida")
        print(f"Usted está en el hemisferio Sur. Estación: {estacion_s}")
    else:
        print("Hemisferio inválido. Ingrese 'N' o 'S'.")

def menu():
    while True:
        print("\n--- Menú de ejercicios TP3 - Condicionales ---")
        print("1 - Ejercicio 1 (mayor de 18)")
        print("2 - Ejercicio 2 (nota aprobado/desaprobado)")
        print("3 - Ejercicio 3 (solo números pares)")
        print("4 - Ejercicio 4 (categorías por edad)")
        print("5 - Ejercicio 5 (contraseña 8-14 caracteres)")
        print("6 - Ejercicio 6 (moda, mediana, media y sesgo)")
        print("7 - Ejercicio 7 (agregar '!' si termina en vocal)")
        print("8 - Ejercicio 8 (transformar nombre según opción)")
        print("9 - Ejercicio 9 (clasificar magnitud de terremoto)")
        print("10 - Ejercicio 10 (estación según hemisferio, mes y día)")
        print("0 - Salir y finalizar")
        opcion = input("Seleccione una opción (0-10): ").strip()
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        elif opcion == "0":
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingrese un número entre 0 y 10.")

if __name__ == "__main__":
    menu()
