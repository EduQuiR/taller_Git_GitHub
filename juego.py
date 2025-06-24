import random

class JuegoAdivina:
    def __init__(self):
        self.nombre = ""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def iniciar(self, nombre):
        if not nombre:
            raise ValueError("Nombre vacío")
        self.nombre = nombre

    def verificar_intento(self, intento):
        self.intentos += 1
        if intento < self.numero_secreto:
            return "Demasiado bajo"
        elif intento > self.numero_secreto:
            return "Demasiado alto"
        else:
            return "Correcto"
