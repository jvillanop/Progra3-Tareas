from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.generar_visualizacion()
    
    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        self.generar_visualizacion()
    
    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                self.generar_visualizacion()
                return
            actual = actual.siguiente
    
    def mostrar_lista(self):
        actual = self.cabeza
        resultado = "None"
        while actual:
            resultado += f" <- [{actual.nombre} {actual.apellido} ({actual.carnet})] -> "
            actual = actual.siguiente
        resultado += "None"
        print(resultado)
    
    def generar_visualizacion(self):
        dot = Digraph()
        actual = self.cabeza
        while actual:
            dot.node(str(actual.carnet), f"{actual.nombre} {actual.apellido}\n{actual.carnet}")
            if actual.siguiente:
                dot.edge(str(actual.carnet), str(actual.siguiente.carnet), dir="both")
            actual = actual.siguiente
        dot.render('lista_doblemente_enlazada', format='png', cleanup=True)

def menu():
    lista = ListaDoblementeEnlazada()
    while True:
        print("\nMenú:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
