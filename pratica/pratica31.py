class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circunferencia = circuferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor


bola = Bola('vermelha', 70, 'couro')
print(bola.mostrar_cor())

bola.trocar_cor('azul')
print(bola.mostrar_cor())
