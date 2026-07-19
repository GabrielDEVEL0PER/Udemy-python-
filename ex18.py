class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome

motor_v8 = Motor("V8 4.0")
motor_1_0 = Motor("1.0 fiat")

ford = Fabricante("Ford")
fiat = Fabricante("Fiat")

carro1 = Carro("Mustang")
carro1.motor = motor_v8
carro1.fabricante = ford

carro2 = Carro("Argo")
carro2.motor = motor_1_0
carro2.fabricante = fiat

carro3 = Carro("Uno")
carro3.motor = motor_1_0
carro3.fabricante = fiat

print(f'Carro: {carro1.nome}| Motor: {carro1.motor.nome}| Fabricante: {carro1.fabricante.nome}')
print(f'Carro: {carro2.nome}| Motor: {carro2.motor.nome}| Fabricante: {carro2.fabricante.nome}')
print(f'Carro: {carro3.nome}| Motor: {carro3.motor.nome}| Fabricante: {carro3.fabricante.nome}')



