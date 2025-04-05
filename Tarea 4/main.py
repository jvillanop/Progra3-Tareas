import csv
import graphviz
from AVL import AVL

def graficar_arbol(dot, nodo):
    if nodo:
        dot.node(str(nodo.valor))
        if nodo.izquierda:
            dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
            graficar_arbol(dot, nodo.izquierda)
        if nodo.derecha:
            dot.edge(str(nodo.valor), str(nodo.derecha.valor))
            graficar_arbol(dot, nodo.derecha)

def generar_graphviz(raiz):
    dot = graphviz.Digraph()
    graficar_arbol(dot, raiz)
    dot.render("arbol_avl", format="png", cleanup=False)
    print("Árbol guardado como arbol_avl.png")

def cargar_csv(ruta, arbol):
    try:
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    if valor.strip().isdigit():
                        arbol.raiz = arbol.insertar(arbol.raiz, int(valor))
        print("Archivo cargado correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")

def menu():
    arbol = AVL()
    while True:
        print("\n1. Insertar un número")
        print("2. Buscar un número")
        print("3. Eliminar un número")
        print("4. Cargar desde archivo CSV")
        print("5. Visualizar en Graphviz")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            num = int(input("Ingrese el número a insertar: "))
            arbol.raiz = arbol.insertar(arbol.raiz, num)
        elif opcion == '2':
            num = int(input("Ingrese el número a buscar: "))
            encontrado = arbol.buscar(arbol.raiz, num)
            print("Número encontrado." if encontrado else "No encontrado.")
        elif opcion == '3':
            num = int(input("Ingrese el número a eliminar: "))
            arbol.raiz = arbol.eliminar(arbol.raiz, num)
        elif opcion == '4':
            ruta = input("Ingrese la ruta del archivo CSV: ")
            cargar_csv(ruta, arbol)
        elif opcion == '5':
            generar_graphviz(arbol.raiz)
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
