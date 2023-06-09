"""
Programa criado para retornar os valores de uma formulação de ração para alimentação animal.
"""


class Formula:
    def __init__(self, receita, quantidade):
        # Inicia o programa recebendo as informações de qual receita e a quantidade.
        self._receita = receita
        self._quantidade = quantidade

    def escolha_receita(self):
        # Escolhe uma receita da lista.
        match self._receita:
            case '1' | 1:
                receita_01 = {'nuc_mineral': 0.05, 'fos_bicalcio': 0.2, 'sal_branco': 0.5, 'milho': 0.15, 'soja': 0.1}
                return receita_01
            case '2' | 2:
                receita_02 = {'nuc_mineral': 0.10, 'fos_bicalcio': 0.25, 'sal_branco': 0.3, 'milho': 0.15, 'soja': 0.2}
                return receita_02
            case '3' | 3:
                receita_03 = {'nuc_mineral': 0.08, 'fos_bicalcio': 0.15, 'sal_branco': 0.6, 'milho': 0.02, 'soja': 0.15}
                return receita_03
            case '4' | 4:
                receita_04 = {'nuc_mineral': 0.20, 'fos_bicalcio': 0.10, 'sal_branco': 0.4, 'milho': 0.10, 'soja': 0.2}
                return receita_04
            case _:
                raise ValueError('Opção Incorreta!')

    def escolha_quantidade(self):
        # A partir da quantidade selecionada, retorna a quantidade a ser produzida.
        match self._quantidade:
            case '1' | 1:
                return self._retorna_receita(200)
            case '2' | 2:
                return self._retorna_receita(400)
            case '3' | 3:
                return self._retorna_receita(500)
            case '4' | 4:
                return self.calculo_livre()
            case _:
                raise ValueError('Opção Incorreta!')

    def calculo_livre(self):
        # A partir da pesagem do primeiro ingrediente, retorna o valor dos outros.
        pass

    def _retorna_receita(self, quantidade):
        nova_receita = {}
        receita = self.escolha_receita().items()
        for x, y in receita:
            novo_valor = y * quantidade
            nova_receita[x] = novo_valor
        return nova_receita


