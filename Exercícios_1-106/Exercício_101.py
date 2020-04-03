def voto(ano):
    from datetime import date
    global idade
    idade = date.today().year - ano
    if 16 <= idade < 18 or idade >= 65:
        return "OPCIONAL"
    elif idade < 16:
        return "NEGADO"
    elif idade >= 18:
        return "OBRIGATÓRIO"


valor = int(input('Em que ano você nasceu? '))
valor = voto(valor)
print('Com', idade, 'anos: VOTO', valor)
