import json
from Particula.particula import Particula

class MainClass:
    def __init__(self):
        self.__particulas = []

    def agregarInicio(self, particula):
        self.__particulas.insert(0, particula)

    def agregarFinal(self, particula):
        self.__particulas.append(particula)

    def __str__(self):
        return ''.join(
            str(particula) for particula in self.__particulas
        )

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
