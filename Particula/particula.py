from Particula.algoritmos import distanciaEuclidiana

class Particula:
    def __init__(self, idParticula, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue):
        self.__idParticula = idParticula
        self.__origenX = origenX
        self.__origenY = origenY
        self.__destinoX = destinoX
        self.__destinoY = destinoY
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distanciaEuclidiana(origenX, destinoX, origenY, destinoY)

    def __str__(self):
        return (
            "id: " + self.__idParticula + '\n' +
            "Origen X: " + str(self.__origenX) + '\n' +
            "Origen Y: " + str(self.__origenY) + '\n' +
            "Destino X: " + str(self.__destinoX) + '\n' +
            "Destino Y: " + str(self.__destinoY) + '\n' +
            "Velocidad: " + self.__velocidad + '\n' +
            "Red: " + str(self.__red) + '\n' +
            "Blue: " + str(self.__blue) + '\n' +
            "Green: " + str(self.__blue) + '\n' +
            "Distancia: " + str(self.__distancia) + '\n' +
            "----------------------------------------------" + '\n'
        )

    def toDict(self):
        return {
            "idParticula": self.__idParticula,
            "origenX": self.__origenX,
            "origenY": self.__origenY,
            "destinoX": self.__destinoX,
            "destinoY": self.__destinoY,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
