import math
def ejercicio_1():
    print("Hola Mundo!")

def ejercicio_2():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}!")

def ejercicio_3():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def ejercicio_4():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

def ejercicio_5():
    segundos = float(input("Ingresa la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

def ejercicio_6():
    numero = int(input("Ingresa un número: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def ejercicio_7():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    
    if num2 != 0:
        print(f"División: {num1 / num2:.2f}")
    else:
        print("No se puede dividir por cero.")

def ejercicio_8():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal es: {imc:.2f}")

def ejercicio_9():
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (9 / 5) * celsius + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

def ejercicio_10():
    numeros = [float(input(f"Ingresa el número {i+1}: ")) for i in range(3)]
    promedio = sum(numeros) / len(numeros)
    print(f"Promedio Total: {promedio:.2f}")

def mostrar_menu(opciones):
    items = [f"{i}. Ejercicio {i}" for i in range(1, 11)]
    items.append("0. Salir")

    max_len = max(len(item) for item in items)
    ancho = max_len + 4

    print("Alumna: Nazarena Florencia Rusin \nComisión:12")

    print("╔" + "═" * ancho + "╗")
    titulo = "MENÚ DE EJERCICIOS"
    print("║" + titulo.center(ancho) + "║")
    print("╚" + "═" * ancho + "╝")

    for item in items:
        print("║ " + item.ljust(max_len) + " ║")

    print("╚" + "═" * ancho + "╝")


# ------------------------------
# Main
# ------------------------------
def main():
    ejercicios = {
        "1": ejercicio_1,
        "2": ejercicio_2,
        "3": ejercicio_3,
        "4": ejercicio_4,
        "5": ejercicio_5,
        "6": ejercicio_6,
        "7": ejercicio_7,
        "8": ejercicio_8,
        "9": ejercicio_9,
        "10": ejercicio_10,
    }

    while True:
        mostrar_menu(ejercicios)
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Adios!")
            break
        elif opcion in ejercicios:
            ejercicios[opcion]()
            input("\nPresiona Enter para volver al menú...")
        else:
            print("Opción inválida, intenta nuevamente.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
