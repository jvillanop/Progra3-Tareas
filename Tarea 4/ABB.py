from Nodo import Nodo

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, valor):
        if raiz is None:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        return raiz

    def buscar(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izquierda, valor)
        return self.buscar(raiz.derecha, valor)

    def minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def eliminar(self, raiz, valor):
        if raiz is None:
            return raiz
        if valor < raiz.valor:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.valor:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            temp = self.minimo(raiz.derecha)
            raiz.valor = temp.valor
            raiz.derecha = self.eliminar(raiz.derecha, temp.valor)
        return raiz