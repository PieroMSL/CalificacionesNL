class Calificador:
    def __init__(self, nota):
        self.nota = nota

    def calificar(self):
        if self.nota >= 19.0:
            return "A+"
        elif self.nota >= 18.5:
            return "A"
        elif self.nota > 16.0:
            return "B"
        elif self.nota >= 10.5:
            return "C"
        else:
            return "F"