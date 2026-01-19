def notas(*notas, situacao=False):
  """
    - > Analisa notas de alunos e retorna um dicionário com informações da turma.
  :param notas: uma ou mais notas dos alunos (valores númericos)
  :param situacao: opcional, indica se deve ou não mostrar a situação da turma
  :return: dicionário com quantidade, maior nota, menor nota, média e situação da turma
  """

  resultado = {}
  resultado["total"] = len(notas)
  resultado["maior"] = max(notas)
  resultado["menor"] = min(notas)
  resultado["media"] = sum(notas) / len(notas)

  if situacao:
    if resultado["media"] >= 7:
      resultado["situacao"] = "Boa"
    elif resultado["media"] >= 5:
      resultado["situacao"] = "Razoável"
    else:
      resultado["situacao"] = "Ruim"

  return resultado

resp = notas(7, 8, situacao=True)
print(resp)
help(notas)
