def ficha(nome, gols):
    if not (nome.isalpha()):
        nome = "<desconhecido>"
    if not (gols.isnumeric()):
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s).')


jogador = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantidade de gols: ')).strip()
ficha(jogador, gols)
