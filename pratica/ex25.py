class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def descricao (self):
        return f'Carro {self.modelo} {self.marca}'
    
    def acelerar(self, velocidade):
        return f'{self.marca} {self.modelo} está aceleradndo a {velocidade} km/h'


carro = Carro(marca='Toyota',modelo='Corolla')
print(carro.descricao())
print(carro.acelerar(80))