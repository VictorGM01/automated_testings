from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

victor = Usuario('Victor')
rapha = Usuario("Raphaela")
naja = Usuario("Najara")

lance_da_rapha = Lance(rapha, 950.0)
lance_do_victor = Lance(victor, 1000.0)
lance_da_najara = Lance(naja, 400.0)


leilao = Leilao('Monalisa')

leilao.lances.append(lance_do_victor)
leilao.lances.append(lance_da_rapha)
leilao.lances.append(lance_da_najara)


for lance in leilao.lances:
    print(f'O(a) usuario(a) {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f"O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}")



