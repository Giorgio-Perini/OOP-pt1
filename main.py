from studente import Studente #da persona (il file) importo la classe Persona


studente = Studente("Giorgio", "3F")

studente.aggiungi_voto(4)
studente.aggiungi_voto(8)

print(studente.media())
print(studente.stampa_info())
