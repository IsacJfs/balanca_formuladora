import random


class SimuladorBalanca:
    def __init__(self):
        self._recebe_peso = 0

    def novo_peso(self):
        self._recebe_peso = float(input('Digite o Peso: '))
        novo_peso = self._recebe_peso
        return novo_peso

    def gera_peso(self):
        rand = random.random()
        peso_gerado = self._recebe_peso * rand
        return peso_gerado

    def retorna_peso(self):
        return self._recebe_peso
