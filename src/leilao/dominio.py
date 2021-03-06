from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_do_lance_nao_eh_valido(valor):
            raise LanceInvalido("O valor do lance não pode ser maior que o valor disponível na carteira")

        lance = Lance(self, valor)
        leilao.propoe_lance(lance)
        self.__carteira -= valor

    def _valor_do_lance_nao_eh_valido(self, valor):
        return valor > self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe_lance(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuarios_sao_diferentes(self, lance):
        if self.lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode propor lances seguidos")

    def _valor_eh_maior_que_o_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance não pode ser menor do que o lance anterior")

    def lance_eh_valido(self, lance):
        return not self._tem_lances() or self._usuarios_sao_diferentes(lance) and self._valor_eh_maior_que_o_lance_anterior(lance)