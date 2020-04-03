def notas(*notas, sit=False):
    """
    -> Retorna dados sobre as notas dos alunos
    :param notas: recebe as notas dos alunos
    :param sit: "True" para saber se a média da turma foi "ÓTIMA", "RAZOÁVEL" ou "RUIM"
    :return: Retorna um dicionário com os dados da turma baseados nas notas
    """
    valores = {"QTD de Notas": len(notas), "Maior Nota": max(notas), "Menor nota": min(notas)}
    media = 0
    for val in notas:
        media += val
    media /= len(notas)
    valores["Média"] = media
    if sit:
        if media < 5:
            valores["Situação"] = "RUIM"
        elif 5 <= media < 7:
            valores["Situação"] = "RAZOÁVEL"
        else:
            valores["Situação"] = "ÓTIMA"
    return valores


alunos = notas(5.5, 2.5, 10, 6.5, sit=True)
print(alunos)
help(notas)
