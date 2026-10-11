class Prestito:
    def __init__(self,codiceUnivoco,data,idStrumento,cognomeAllievo):
        self.codiceUnivoco = codiceUnivoco
        self.data = data
        self.idStrumento = idStrumento
        self.cognomeAllievo = cognomeAllievo

    def __str__(self):
        return f"{self.codiceUnivoco} {self.data} {self.idStrumento} {self.cognomeAllievo}"