import graphviz
import csv

class NodoB:
    def __init__(self, grado, hoja=False):
        self.grado = grado
        self.hoja = hoja
        self.claves = []
        self.hijos = []

class ArbolB:
    def __init__(self, grado):
        self.grado = grado
        self.raiz = NodoB(grado, hoja=True)

    def buscar(self, clave, nodo=None):
        if nodo is None:
            nodo = self.raiz

        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and clave == nodo.claves[i]:
            return True

        if nodo.hoja:
            return False

        return self.buscar(clave, nodo.hijos[i])

    def insertar(self, clave):
        raiz = self.raiz
        if len(raiz.claves) == self.grado - 1:
            nueva_raiz = NodoB(self.grado, hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self.dividir_hijo(nueva_raiz, 0)
            self.raiz = nueva_raiz
            self._insertar_no_lleno(self.raiz, clave)
        else:
            self._insertar_no_lleno(raiz, clave)

    def _insertar_no_lleno(self, nodo, clave):
        i = len(nodo.claves) - 1

        if nodo.hoja:
            nodo.claves.append(0)
            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == self.grado - 1:
                self.dividir_hijo(nodo, i)
                if clave > nodo.claves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], clave)

    def dividir_hijo(self, padre, i):
        grado = self.grado
        nodo_a_dividir = padre.hijos[i]
        nuevo_nodo = NodoB(grado, hoja=nodo_a_dividir.hoja)

        medio = (grado - 1) // 2

        # Claves para el nuevo nodo
        nuevo_nodo.claves = nodo_a_dividir.claves[medio + 1:]

        if not nodo_a_dividir.hoja:
            nuevo_nodo.hijos = nodo_a_dividir.hijos[medio + 1:]

        # Reducir el nodo a dividir
        nodo_a_dividir.claves = nodo_a_dividir.claves[:medio]
        nodo_a_dividir.hijos = nodo_a_dividir.hijos[:medio + 1] if not nodo_a_dividir.hoja else nodo_a_dividir.hijos

        # Insertar el nodo nuevo y la clave media en el padre
        padre.hijos.insert(i + 1, nuevo_nodo)
        padre.claves.insert(i, nodo_a_dividir.claves.pop())

    def eliminar(self, clave):
        # Eliminación completa de Árbol B es más extensa y la podemos agregar si quieres.
        print("Eliminar todavía no implementado completamente.")

    def cargar_desde_csv(self, archivo):
        try:
            with open(archivo, 'r') as f:
                lector = csv.reader(f)
                for fila in lector:
                    for valor in fila:
                        self.insertar(int(valor.strip()))
            print("Datos cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def graficar(self, nombre_archivo="arbol_b"):
        dot = graphviz.Digraph()
        self._graficar_nodo(self.raiz, dot)
        dot.render(nombre_archivo, format='png', cleanup=True)
        print(f"Árbol guardado como {nombre_archivo}.png")

    def _graficar_nodo(self, nodo, dot, id_padre=None):
        id_nodo = str(id(nodo))
        etiqueta = '|'.join(str(clave) for clave in nodo.claves)
        dot.node(id_nodo, etiqueta)

        if id_padre:
            dot.edge(id_padre, id_nodo)

        for hijo in nodo.hijos:
            self._graficar_nodo(hijo, dot, id_nodo)


def menu():
    grado = int(input("Ingrese el grado del Árbol B: "))
    arbol = ArbolB(grado)

    while True:
        print("\n1. Insertar una clave")
        print("2. Buscar una clave")
        print("3. Eliminar una clave")
        print("4. Cargar claves desde CSV")
        print("5. Visualizar árbol con Graphviz")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            clave = int(input("Ingrese la clave a insertar: "))
            arbol.insertar(clave)
        elif opcion == '2':
            clave = int(input("Ingrese la clave a buscar: "))
            encontrado = arbol.buscar(clave)
            print("Clave encontrada." if encontrado else "Clave no encontrada.")
        elif opcion == '3':
            clave = int(input("Ingrese la clave a eliminar: "))
            arbol.eliminar(clave)
        elif opcion == '4':
            archivo = input("Ingrese la ruta del archivo CSV: ")
            arbol.cargar_desde_csv(archivo)
        elif opcion == '5':
            arbol.graficar()
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()