class Studente:
    def __init__(self, nome, classe):
        self.nome = str(nome)
        self.classe = str(classe)
        self.voti = []


    def aggiungi_voto(self,voto):
        if voto > 1 and voto < 10:
            self.voti.append(voto)
        else:
            print("voto non valido")


    def media(self):
        if len(self.voti) == 0:
            return 0
        else:
            return sum(self.voti) / len(self.voti)
        

    def stampa_info(self):
        print(f"lo studente {self.nome} della classe {self.classe}, presenta una media sommativa dei voti di {self.media()}")
    


