from formulador import Formula
from balanca import SimuladorBalanca
"""
Um simulador de menu de como a balança deveria funcionar em um hardware específico
"""


class SimulaMenu:
    def __init__(self):
        self._mensagem_inicial()
        self._exibe_pesagem()

    def _menu_receita(self):
        # Exibe as opções de receitas e recebe a opção desejada
        print("""
        |-------------------------------------|
        |     Selecione o tipo de ração:      |
        |                                     |
        |   (1) Seca          (2) Águas       |
        |                                     |
        |   (3) Reprodução    (4) Bezerros    |
        |                                     |
        |-------------------------------------|
        """)
        set_receita = input("Digite a opção desejada: ")
        return set_receita

    def _menu_quantidade(self):
        # Exibe as opções de quntidades e recebe a opção desejada
        print("""
        |-------------------------------------|
        |   Selecione a quantidade desejada:  |
        |                                     |
        |   (1) 200 kg        (2) 400 kg      |
        |                                     |
        |   (3) 500 kg        (4) Livre       |
        |                                     |
        |-------------------------------------| 
        """)
        set_quantidade = input("Digite a opção desejada: ")
        return set_quantidade

    def _mensagem_inicial(self):
        # Exibe a mensagem informativa inicial
        print("""
        |-------------------------------------|
        |      Balança auto-formualdora       |
        |                                     |
        |   Você irá selecionar a receita     |
        |      e a quantidade de ração        |
        |        que deseja produzir          |
        |                                     |
        |-------------------------------------|
        
        """)
        return input("Digite '1' para continuar.\n")

    def _exibe_pesagem(self):
        # Exibe o nome e a quantidade dos itens a serem pesados.
        receita = self._menu_receita()
        quantidade = self._menu_quantidade()
        formula = Formula(receita, quantidade)
        formula.escolha_receita()
        valores_pesados = {}
        for x, y in formula.escolha_quantidade().items():
            print(f"\nPese {y} Kg de {x}")
            valores_pesados[x] = float(SimuladorBalanca().novo_peso())
            print(f"Valor pesado {valores_pesados[x]}\n")
        print("O total pesado foi de: ", (sum(valores_pesados.values())), "kg")
        return valores_pesados




