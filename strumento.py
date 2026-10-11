class Strumento:
    def __init__(self,codiceUnivoco,tipo,marca,annoAcquisto,valore):
        self.codiceUnivoco = codiceUnivoco
        self.tipo = tipo
        self.marca = marca
        self.annoAcquisto = annoAcquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codiceUnivoco} {self.tipo} {self.marca} {self.annoAcquisto} {self.valore}"