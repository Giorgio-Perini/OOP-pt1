class Rettangolo:
    def __init__(self, base, altezza, colore):
        self.base = base
        self.altezza = altezza
        self.colore = colore


    def area(self):
        if self.base == 0 and self.altezza == 0:
            print("non sono presenti alcuni valori")
        else:
            return (self.base * self.altezza)


    def stampa_info(self):
        print(f"il rettangolo ha la base {self.base} l' altezza {self.altezza}, l' area del rettangolo è {self.area()}, è di colore {self.colore}")
    


