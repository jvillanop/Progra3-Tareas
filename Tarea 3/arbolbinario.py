import os
import graphviz

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        self.raiz = self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, raiz, clave):
        if raiz is None:
            return Nodo(clave)
        if clave < raiz.clave:
            raiz.izquierda = self._insertar_recursivo(raiz.izquierda, clave)
        else:
            raiz.derecha = self._insertar_recursivo(raiz.derecha, clave)
        return raiz

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, raiz, clave):
        if raiz is None or raiz.clave == clave:
            return raiz
        if clave < raiz.clave:
            return self._buscar_recursivo(raiz.izquierda, clave)
        return self._buscar_recursivo(raiz.derecha, clave)

    def eliminar(self, clave):
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, raiz, clave):
        if raiz is None:
            return raiz
        if clave < raiz.clave:
            raiz.izquierda = self._eliminar_recursivo(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, clave)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            temp = self._nodo_minimo(raiz.derecha)
            raiz.clave = temp.clave
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, temp.clave)
        return raiz

    def _nodo_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    try:
                        numero = int(linea.strip())
                        self.insertar(numero)
                    except ValueError:
                        print(f"Omitiendo número inválido: {linea.strip()}")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def generar_graphviz(self, nombre_archivo="arbol"):
        dot = graphviz.Digraph()
        self._agregar_nodos_y_aristas(dot, self.raiz)
        dot.render(nombre_archivo, format='png', cleanup=False)
        print(f"Gráfico guardado como {nombre_archivo}.png")

    def _agregar_nodos_y_aristas(self, dot, nodo):
        if nodo is not None:
            dot.node(str(nodo.clave))
            if nodo.izquierda:
                dot.edge(str(nodo.clave), str(nodo.izquierda.clave))
                self._agregar_nodos_y_aristas(dot, nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.clave), str(nodo.derecha.clave))
                self._agregar_nodos_y_aristas(dot, nodo.derecha)

def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\n1. Insertar un número")
        print("2. Buscar un número")
        print("3. Eliminar un número")
        print("4. Cargar desde un archivo")
        print("5. Generar visualización Graphviz")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            num = int(input("Ingrese el número a insertar: "))
            arbol.insertar(num)
            print("Número insertado.")
        elif opcion == '2':
            num = int(input("Ingrese el número a buscar: "))
            resultado = arbol.buscar(num)
            print("Número encontrado." if resultado else "Número no encontrado.")
        elif opcion == '3':
            num = int(input("Ingrese el número a eliminar: "))
            arbol.eliminar(num)
            print("Número eliminado.")
        elif opcion == '4':
            nombre_archivo = input("Ingrese la ruta del archivo: ")
            arbol.cargar_desde_archivo(nombre_archivo)
            print("Archivo cargado correctamente.")
        elif opcion == '5':
            arbol.generar_graphviz()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()