class nod:
    def __init__(self, Valor):
        self.Valor = Valor
        self.l = None #izq
        self.r = None #der

class Arbol:
    def __init__(self):
        self.raix = None

    def Add(self, Valor):
        nn = nod(Valor)
        if self.raix is None:
            self.raix = nn
        else:
            self.Agregarr(self.raix, nn)

    def Agregarr(self, an, nn):
        if an.Valor > nn.Valor:
            if an.l is None:
                an.l = nn
            else:
                self.Agregarr(an.l, nn)
        else:
            if an.r is None:
                an.r = nn
            else:
                self.Agregarr(an.r, nn)

    def Chow(self):
        self.Mostrarr(self.raix)

    def Mostrarr(self, an):
        if an is not None:
            print(an.Valor)
            self.Mostrarr(an.r)
            self.Mostrarr(an.l)
if __name__ == "__main__":
    Arbol = Arbol()

Arbol.Add(8)
Arbol.Add(6)
Arbol.Add(5)
Arbol.Add(9)
Arbol.Add(5)
Arbol.Add(4)
Arbol.Chow()
