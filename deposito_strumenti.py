from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti=[]
        self.prestiti=[]

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r") as filein:
                for line in filein:
                    campi=line.strip().split(",")
                    s=Strumento(campi[0],campi[1],campi[2],int(campi[3]),float(campi[4]))
                    self.strumenti.append(s)
                    print(s, end=",")
        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: Il file '{file_path}' non esiste")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        ultimoStrum=self.strumenti[-1]
        ultimoNum=int(ultimoStrum.codiceUnivoco[1:])
        nuovoStrumento=Strumento("S"+str(ultimoNum+1),tipo,marca,anno_acquisto,valore)
        self.strumenti.append(nuovoStrumento)
        return nuovoStrumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumento_trovato = False
        for s in self.strumenti:
            if s.codiceUnivoco == id_strumento:
                strumento_trovato = True
                break
        if not strumento_trovato:
            raise Exception(f"Lo strumento {id_strumento} non è presente nel sistema.")
        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception(f"Lo strumento {id_strumento} è già attualmente in prestito.")
        id_nuovo_prestito = str(len(self.prestiti) + 1)
        nuovoPrestito = Prestito("P"+id_nuovo_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(nuovoPrestito)
        return nuovoPrestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        prestito_da_rimuovere = None
        for p in self.prestiti:
            if p.codiceUnivoco == id_prestito:
                prestito_da_rimuovere = p
                break
        if prestito_da_rimuovere is None:
            raise Exception(f"Errore: Il codice {id_prestito} non corrisponde ad alcun prestito attivo.")
        self.prestiti.remove(prestito_da_rimuovere)