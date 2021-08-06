from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.rapha = Usuario("Raphaela", 1500.0)
        self.lance_da_rapha = Lance(self.rapha, 950.0)
        self.leilao = Leilao('Quadro: Monalisa')
        self.menor_valor_esperado = 950.0

    def test_deve_retornar_o_maior_e_o_menor_numero_de_dois_lances_quando_adicionados_em_ordem_crescente(self):
        victor = Usuario('Victor', 1500.0)

        lance_do_victor = Lance(victor, 1000.0)

        self.leilao.propoe_lance(self.lance_da_rapha)
        self.leilao.propoe_lance(lance_do_victor)

        maior_valor_esperado = 1000.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_o_lance_caso_o_valor_seja_menor_do_que_o_valor_do_ultimo_lance(self):
        with self.assertRaises(ValueError):
            victor = Usuario('Victor', 1500.0)

            lance_do_victor = Lance(victor, 1000.0)

            self.leilao.propoe_lance(lance_do_victor)
            self.leilao.propoe_lance(self.lance_da_rapha)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_existir_apenas_um_lance(self):
        self.leilao.propoe_lance(self.lance_da_rapha)

        maior_valor_esperado = 950.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_lance_quando_existir_mais_do_que_dois_lances(self):
        victor = Usuario('Victor', 1500.0)
        najara = Usuario("Najara", 1500.0)

        lance_do_victor = Lance(victor, 959.9)
        lance_da_najara = Lance(najara, 1000.0)

        self.leilao.propoe_lance(self.lance_da_rapha)
        self.leilao.propoe_lance(lance_do_victor)
        self.leilao.propoe_lance(lance_da_najara)

        maior_valor_esperado = 1000.0

        self.assertEqual(self.menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # verifica se a lista está vazia, caso esteja, o usuário ainda deve conseguir propor o lance:

    def test_deve_permitir_o_usuario_propor_o_lance_caso_o_leilao_ainda_nao_tenha_lances(self):
        self.leilao.propoe_lance(self.lance_da_rapha)

        self.assertEqual(1, len(self.leilao.lances))

    # verifica se o último usuário é diferente do usuário que está propondo o lance, caso sim, o usuário consegue propor:

    def test_deve_permitir_o_usuario_propor_o_lance_caso_o_ultimo_usuario_seja_diferente(self):
        victor = Usuario("Victor", 1500.0)
        lance_do_victor = Lance(victor, 1500.0)

        self.leilao.propoe_lance(self.lance_da_rapha)
        self.leilao.propoe_lance(lance_do_victor)

        self.assertEqual(2, len(self.leilao.lances))

    # verifica se o último usuário é igual ao usuário que está propondo o lance, caso sim, o usuário não consegue propor:

    def test_nao_deve_permitir_que_o_usuario_proponha_o_lance_caso_o_usuario_seja_o_mesmo(self):
        with self.assertRaises(ValueError):
            novo_lance_da_rapha = Lance(self.rapha, 980.0)
            self.leilao.propoe_lance(self.lance_da_rapha)
            self.leilao.propoe_lance(novo_lance_da_rapha)