class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaCompras:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_ultimo(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.next = Nodo(dato)

    def recorrido (self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.next
    
    def eliminar_inicio(self):
        self.primero = self.primero.next
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCompras()

        while opcion != 5:
            print("\n\n****LISTA DE COMPRAS**** \n1. Aregar\n2. Eliminar\n3. Lista Vacia?\n4. mostrar\n5. Salir ")
            opcion = int(input("Ingrese Opcion: "))

            if opcion == 1:
                n=int(input("cuantos elementos desea agregar: "))
                if 5>=n>0:
                    for i in range (n):
                        print("solo puede agregar maximo 5 elementos como maximo")
                        dato = input("\ningrese un dato: ")
                    lista.agregar_ultimo(dato)
                else:
                    print("incorrecto")
            elif opcion == 2:
                 lista.eliminar_inicio()
            elif opcion == 3:
                print("si" if lista.vacia()else "No")
            elif opcion == 4:
                lista.recorrido()
            elif opcion == 5:
                print("FIN")
            else:
                print("agrege un dato correcto: ")
except Exception as e:
    print(e)
