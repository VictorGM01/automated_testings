from src.leilao.dominio import Usuario, Leilao
import pytest
from src.leilao.excecoes import LanceInvalido


# funções que se repetem em todos os testes:
@pytest.fixture
def vic():
    return Usuario("Victor", 100.0)

@pytest.fixture
def leilao():
    return Leilao("livros")

# testes das funcionalidades da class Usuario
def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vic, leilao):
    vic.propoe_lance(leilao, 50.0)

    assert vic.carteira == 50.0

def test_deve_permitir_propor_um_lance_quanco_o_valor_for_menor_que_o_valor_da_carteira(vic, leilao):
    vic.propoe_lance(leilao, 2.0)

    assert vic.carteira == 98.0

def test_deve_permitir_propor_um_lance_quando_o_valor_for_igual_ao_valor_da_carteira(vic, leilao):
    vic.propoe_lance(leilao, 100.0)

    assert vic.carteira == 0.0

def test_nao_deve_permitir_propor_um_lance_quando_valor_for_maior_que_o_da_carteira(vic, leilao):
    with pytest.raises(LanceInvalido):

        vic.propoe_lance(leilao, 200.0)

        assert vic.carteira == 100.0

