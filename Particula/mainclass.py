import json
from pprint import pformat
from collections import deque
from Particula.particula import Particula

class MainClass:
    def __init__(self):
        self.__particulas = []

    def agregarInicio(self, particula):
        self.__particulas.insert(0, particula)

    def agregarFinal(self, particula):
        self.__particulas.append(particula)

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.toDict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            archivo.close()
            return True
        except:
            return False

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            archivo.close()
            return True
        except:
            return False
            
    def generarGrafo(self):
        grafo = {}
        for particula in self.__particulas:
            origenX = particula.origenX
            origenY = particula.origenY
            destinoX = particula.destinoX
            destinoY = particula.destinoY
            distancia = particula.distancia
            
            origen = (origenX, origenY)
            destino = (destinoX, destinoY)
            arista_o = (destino, distancia)
            arista_d = (origen, distancia)
            
            if origen in grafo:
                grafo[origen].append(arista_o)
            else:
                grafo[origen] = [arista_o]
                
            if destino in grafo:
                grafo[destino].append(arista_d)
            else:
                grafo[destino] = [arista_d]
            
        return grafo, pformat(grafo, width=50, indent=1)
        
    def profundidad(self, inicio):
        grafo = self.generarGrafo()[0]
        if inicio in grafo:
            pila = []
            visitados = []
            recorrido = []
        
            pila.append(inicio)
            visitados.append(inicio)
            while len(pila) > 0:
                vertice = pila[-1]
                recorrido.append(vertice)
                pila.pop()
                
                adyacentes = grafo[vertice]
                for i in adyacentes:
                    if not i[0] in visitados:
                        pila.append(i[0])
                        visitados.append(i[0])
                        
            return recorrido
            
        else:
            return False
        
    def amplitud(self, inicio):
        grafo = self.generarGrafo()[0]
        if inicio in grafo:
            cola = deque()
            visitados = []
            recorrido = []
            
            cola.appendleft(inicio)
            visitados.append(inicio)
            while len(cola) > 0:
                vertice = cola[-1]
                recorrido.append(vertice)
                cola.pop()
                
                adyacentes = grafo[vertice]
                for i in adyacentes:
                    if not i[0] in visitados:
                        cola.appendleft(i[0])
                        visitados.append(i[0])
                        
            return recorrido
        
        else:
            return False

    def __str__(self):
        return ''.join(
            str(particula) for particula in self.__particulas
        )
        
    def __len__(self):
        return len(self.__particulas)
        
    def __iter__(self):
        self.cont = 0
        return self
        
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
