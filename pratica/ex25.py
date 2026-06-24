class carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def descricao (self):
        return f'Carro {self.modelo} {self.marca}'
        