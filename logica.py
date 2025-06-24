import random

class JuegoLogica:
    def __init__(self):
        self.numero_secreto= random.randint(1,100)
        self.intentos=0