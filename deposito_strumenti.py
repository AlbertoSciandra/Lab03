from operator import attrgetter

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)
        self.in_prestito = False

    def __str__(self):
        return f"[{self.codice}] {self.tipo} - {self.marca} ({self.anno_acquisto}) - €{self.valore:.2f}"


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.strumenti=[]
        self.prestiti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        file=open("strumenti.csv", "r")
        for line in file:
            campi = line.strip().split(",")
            codice = campi[0]  # C1
            strumento = campi[1]  # C2
            marca = campi[2]  # C3
            anno = campi[3]  # C4
            prezzo = campi[4]  # C5
        nuovo_strumento = Strumento(codice, strumento, marca, anno, prezzo)
        self.strumenti.append(nuovo_strumento)
        file.close()
    def aggiungi_strumento(self, strumento, marca, anno, prezzo):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if self.strumenti:
            ultimo_codice = self.strumenti[-1].codice
            num_prog = int(ultimo_codice[1:]) + 1
        else:
            num_prog = 1

        codice = f"S{num_prog}"
        nuovo_strumento = Strumento(codice, tipo, marca, int(anno), float(prezzo))

        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti,key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        strumento_trovato = None
        for s in self.strumenti:
            if s.codice == id_strumento:
                strumento_trovato = s
                break

        if not strumento_trovato:
            raise Exception(f"Errore: Strumento con codice {id_strumento} non trovato.")

        if strumento_trovato.in_prestito:
            raise Exception(f"Errore: Lo strumento {id_strumento} è già in prestito.")
        if self.prestiti:
            ultimo_id_prestito = self.prestiti[-1]["id_prestito"]
            num_prog = int(ultimo_id_prestito[1:]) + 1
        else:
            num_prog = 1

        id_prestito = f"P{num_prog}"
        strumento_trovato.in_prestito = True

        prestito = {
            "id_prestito": id_prestito,
            "data": data,
            "id_strumento": id_strumento,
            "cognome_allievo": cognome_allievo
        }
        self.prestiti.append(prestito)
        return prestito
    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        prestito_trovato = None
        for p in self.prestiti:
            if p["id_prestito"] == id_prestito:
                prestito_trovato = p
                break

        if not prestito_trovato:
            raise Exception(f"Errore: Prestito con codice {id_prestito} non esistente.")

        id_strumento = prestito_trovato["id_strumento"]
        for s in self.strumenti:
            if s.codice == id_strumento:
                s.in_prestito = False
                break
        self.prestiti.remove(prestito_trovato)