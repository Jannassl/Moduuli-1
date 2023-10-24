class Hissi:
    def __init__(self,numero, alin_kerros, ylimm_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimm_kerros


    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.kerros > kohde_kerros:
            self.kerros_alas()
        while self.kerros < kohde_kerros:
            self.kerros_ylos()

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f'Hissi on kerroksessa {self.kerros}')

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f'Hissi on kerroksessa {self.kerros}')

class Talo:

    def __init__(self,alin_kerros,ylin_kerros,hissien_maara):
        self.alin_kerros = int(alin_kerros)
        self.ylin_kerros = int(ylin_kerros)
        self.hissien_maara = int(hissien_maara)
        self.hissit = self.hissien_luonti()

    def hissien_luonti(self):
        hissi_lista=[]
        for i in range(self.hissien_maara):
            hissi= (i +1, self.alin_kerros, self.ylin_kerros)
            hissi_lista.append(hissi)

        return hissi_lista

    def aja_hissia(self,hissi_numero, kohde_kerros):
        self.hissi_numero = int(hissi_numero)
        self.kohde_kerros = int(kohde_kerros)
        print(f"Hissin numero {self.hissi_numero} ja kerros {self.kohde_kerros}")
    def palohälytys(self):
        for hissi in self.hissit:
             hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)

hissi = Hissi
talo = Talo(1,7,3)
talo.hissien_luonti()

talo.aja_hissia(1,5)
talo.palohälytys()