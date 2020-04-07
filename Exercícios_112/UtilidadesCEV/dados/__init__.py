def leiaDinheiro(msg):
    n = str(input(msg)).strip()
    while True:
        try:
            n = float(n.replace(',', '.'))
            return int(n)
        except:
            print(f'\033[31;1mERROR. valor "{n}" não é válido.\033[m')
            n = input(msg).strip()
