from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.rapha = Usuario("Raphaela")
        self.lance_da_rapha = Lance(self.rapha, 950.0)
        self.leilao = Leilao('Quadro: Monalisa')
        self.menor_valor_esperado = 950.0

    def test_deve_retornar_o_maior_e_o_menor_numero_de_dois_lances_quando_adicionados_em_ordem_crescente(self):
        victor = Usuario('Victor')

        lance_do_victor = Lance(victor, 1000.0)

        self.leilao.propoe_lance(self.lance_da_rapha)
        self.leilao.propoe_lance(lance_do_victor)

        maior_valor_esperado = 1000.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_numero_de_dois_lances_quando_adicionados_em_ordem_decrescente(self):
        victor = Usuario('Victor')

        lance_do_victor = Lance(victor, 1000.0)

        self.leilao.propoe_lance(lance_do_victor)
        self.leilao.propoe_lance(self.lance_da_rapha)

        maior_valor_esperado = 1000.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_existir_apenas_um_lance(self):
        self.leilao.propoe_lance(self.lance_da_rapha)

        maior_valor_esperado = 950.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_existir_mais_do_que_dois_lances(self):
        victor = Usuario('Victor')
        najara = Usuario("Najara")

        lance_do_victor = Lance(victor, 1000.0)
        lance_da_najara = Lance(najara, 959.9)

        self.leilao.propoe_lance(self.lance_da_rapha)
        self.leilao.propoe_lance(lance_do_victor)
        self.leilao.propoe_lance(lance_da_najara)

        maior_valor_esperado = 1000.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)



