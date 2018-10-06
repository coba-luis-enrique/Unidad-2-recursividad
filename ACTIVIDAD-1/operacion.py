"""se define la clase"""

class operaciones:  #operaciones (identacion)

    def __init__(self,lista):
        self.lista=lista

    def palindromo(self):
        if len(self.lista) <= 1:
            return True
        else:
            return self.lista[0] == self.lista[-1]
