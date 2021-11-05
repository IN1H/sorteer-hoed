
class User():
    
    # Puntentelling aan het begin van de quiz.

    IAT = 0
    SE = 0
    FICT = 0
    BDAM = 0
    niks = 0

    # Functies die ervoor zorgen dat de puntentelling omhoog gaat.

    def add_iat(self, count):
        self.IAT = self.IAT + int(count)
        return self


    def add_se(self, count):
        self.SE = self.SE + int(count)
        return self

    
    def add_fict(self, count):
        self.FICT = self.FICT + int(count)
        return self

    def add_bdam(self, count):
        self.BDAM = self.BDAM + int(count)
        return self

    def add_niks(self, count):
        self.niks = self.niks + int(count)
        return self

    def get_index_of_max(self):
        return [self.IAT, self.SE, self.FICT, self.BDAM, self.niks].index(max([self.IAT, self.SE, self.FICT, self.BDAM, self.niks]))

    def get_score(self):
        return [self.IAT, self.SE, self.FICT, self.BDAM, self.niks]
    # Functie zorgt ervoor dat er een specialisatie wordt gekozen met de meeste punten.

    def get_max(self):
        return ["IAT", "SE", "FICT", "BDAM", "niks"][[self.IAT, self.SE, self.FICT, self.BDAM, self.niks].index(max([self.IAT, self.SE, self.FICT, self.BDAM, self.niks]))]

        