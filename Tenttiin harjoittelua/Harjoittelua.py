class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
    def siirry_kerrokseen(self,kohde_kerros):
        self.kohde_kerros = kohde_kerros
        if self.kohde_kerros < self.kerros:
            while self.kohde_kerros != self.kerros:
                self.kerros_alas()
        elif self.kohde_kerros > self.kerros:
            while self.kohde_kerros != self.kerros:
                self.kerros_ylös()

    def kerros_ylös(self):
        self.kerros +=1
        print(f"Hissin kerroksessa: {self.kerros}")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissin kerroksessa: {self.kerros}")


class Talo:
    def __init__(self,alin_kerros,ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissit = []

        #for i in range(self.hissien_lkm):



hissi = Hissi(1,10)
