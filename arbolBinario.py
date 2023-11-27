class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_elemento(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato == nodo.dato:
            print(f"El valor {nuevo_dato} ya existe en el árbol.")
            return

        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._agregar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._agregar_recursivo(nodo.derecha, nuevo_dato)

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, 0)

    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print("    " * nivel + str(nodo.dato))
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def buscar_elemento(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)

    def eliminar_elemento(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato

    def recorrer_pre_orden(self):
        resultado = []
        self._pre_orden(self.raiz, resultado)
        return resultado

    def _pre_orden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._pre_orden(nodo.izquierda, resultado)
            self._pre_orden(nodo.derecha, resultado)

    def recorrer_in_orden(self):
        resultado = []
        self._in_orden(self.raiz, resultado)
        return resultado

    def _in_orden(self, nodo, resultado):
        if nodo is not None:
            self._in_orden(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self._in_orden(nodo.derecha, resultado)

    def recorrer_post_orden(self):
        resultado = []
        self._post_orden(self.raiz, resultado)
        return resultado

    def _post_orden(self, nodo, resultado):
        if nodo is not None:
            self._post_orden(nodo.izquierda, resultado)
            self._post_orden(nodo.derecha, resultado)
            resultado.append(nodo.dato)


if __name__ == "__main__":
    arbol = ArbolBinario()

    elementos_predeterminados = [8, 3, 1, 10, 14, 6, 7, 4, 13]
    for elemento in elementos_predeterminados:
        arbol.agregar_elemento(elemento)

    arbol.mostrar_arbol()

    while True:
        respuesta = input("¿Desea ingresar números al Árbol? (si/no): ").lower()

        if respuesta != 'si':
            break

        numeros_ingresar = input("Ingrese el (los) números que desea poner en el Árbol separados por un espacio: ")
        numeros_ingresar = [int(num) for num in numeros_ingresar.split()]

        for numero_ingresar in numeros_ingresar:
            arbol.agregar_elemento(numero_ingresar)

    arbol.mostrar_arbol()

    dato_buscar = int(input("¿Qué número quieres buscar? "))
    nodo_encontrado = arbol.buscar_elemento(dato_buscar)
    if nodo_encontrado:
        print(f"El número {dato_buscar} fue encontrado en el Árbol.")
    else:
        print(f"El número {dato_buscar} no fue encontrado en el Árbol")

    dato_eliminar = int(input("¿Ingresa el número que quieres eliminar?: "))
    nodo_encontrado = arbol.buscar_elemento(dato_eliminar)

    if nodo_encontrado:
        arbol.eliminar_elemento(dato_eliminar)
        print(f"Se eliminó el número {dato_eliminar} correctamente del Árbol")
    else:
        print(f"El número {dato_eliminar} no existe en el Árbol")

    arbol.mostrar_arbol()

    print("El recorrido en PreOrden es: ", arbol.recorrer_pre_orden())
    print("El recorrido en InOrden es: ", arbol.recorrer_in_orden())
    print("El recorrido en PostOrden es: ", arbol.recorrer_post_orden())
