class Televisao:
    def _init_(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)