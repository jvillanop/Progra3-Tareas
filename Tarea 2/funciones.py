import os

def limpiar_pantalla():
    os.system("cls" if os.name=="nt" else "clear")

def convertir_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return convertir_a_binario(n // 2) + str(n % 2)

def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

def calcular_raiz_cuadrada(n, i=1):
    if i * i > n:
        return i - 1
    return calcular_raiz_cuadrada(n, i + 1)

def raiz_cuadrada_entera(n):
    return calcular_raiz_cuadrada(n)

valores_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def convertir_a_decimal(romano, i=0):
    if i == len(romano):
        return 0
    if i < len(romano) - 1 and valores_romanos[romano[i]] < valores_romanos[romano[i + 1]]:
        return -valores_romanos[romano[i]] + convertir_a_decimal(romano, i + 1)
    return valores_romanos[romano[i]] + convertir_a_decimal(romano, i + 1)

def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)

def menu():
    while True:
        print("\nMenú:")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            n = int(input("Ingrese un número entero: "))
            limpiar_pantalla()
            print("Binario:", convertir_a_binario(n))
            input("\nPresiona Enter para continuar. ")
        elif opcion == "2":
            n = int(input("Ingrese un número entero: "))
            limpiar_pantalla()
            print("Cantidad de dígitos:", contar_digitos(n))
            input("\nPresiona Enter para continuar. ")
        elif opcion == "3":
            n = int(input("Ingrese un número entero: "))
            limpiar_pantalla()
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(n))
            input("\nPresiona Enter para continuar. ")
        elif opcion == "4":
            romano = input("Ingrese un número romano: ")
            limpiar_pantalla()
            print("Decimal:", convertir_a_decimal(romano))
            input("\nPresiona Enter para continuar. ")
        elif opcion == "5":
            n = int(input("Ingrese un número entero positivo: "))
            limpiar_pantalla()
            print("Suma de números enteros desde 0 hasta", n, "es:", suma_numeros_enteros(n))
            input("\nPresiona Enter para continuar. ")
        elif opcion == "6":       
            limpiar_pantalla()     
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()