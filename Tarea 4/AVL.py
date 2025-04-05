from ABB import ABB
from Nodo import Nodo

class AVL(ABB):
    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotacion_derecha(raiz)
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotacion_izquierda(raiz)
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def eliminar(self, raiz, valor):
        raiz = super().eliminar(raiz, valor)
        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierda) >= 0:
            return self.rotacion_derecha(raiz)
        if balance > 1 and self.obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) <= 0:
            return self.rotacion_izquierda(raiz)
        if balance < -1 and self.obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz
