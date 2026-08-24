class Veiculo:

    def __init__(self, marca, modelo ):
        self.marca = marca
        self.modelo = modelo
    def buzinar(self):
        return "Fom fom!"
    def dados(self):
        return self.marca, self.modelo
class Carro(Veiculo): 
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def buzinar(self):
        return "Beep beep!"

carro = Carro('Fiat', 'Uno', 4)
print(carro.dados())
print(carro.buzinar())