CBF = (
  'Flamengo', 'Santos',
  'Palmeiras', 'Grêmio',
  'Athletico-PR', 'São Paulo',
  'Internacional', 'Corinthians',
  'Fortaleza', 'Goiás',
  'Bahia', 'Vasco da Gama',
  'Atlético-MG', 'Fluminense',
  'Botafogo', 'Ceará',
  'Cruzeiro', 'CSA',
  'Chapecoense', 'Avaí'
)
print(f'''Os cinco primeiros do CBF foram:
{CBF[:5]}.

Os últimos quatro colocados foram:
{CBF[-4:]}

Todos os times em ordem alfabética:
{sorted(CBF)}

Posição da Chapecoense:
{CBF.index('Chapecoense') + 1}° posição ''')