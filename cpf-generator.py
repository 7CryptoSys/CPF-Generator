import random
numeros = "1234567890"
digitos = 8
estado = {1: "DF, GO, MS, MT, TO",
          2: "AC, AM, AP, PA, RO, RR",
          3: "CE, MA, PI",
          4: "AL, PB, PE, RN",
          5: "BA, SE",
          6: "MG",
          7: "ES, RJ",
          8: "SP",
          9: "PR, SC",
          10:"RS"}

print(f"""
    1: {estado[1]}
    2: {estado[2]}
    3: {estado[3]}
    4: {estado[4]}
    5: {estado[5]}
    6: {estado[6]}
    7: {estado[7]}
    8: {estado[8]}
    9: {estado[9]}
    0: {estado[10]}""")
escolher_estado = input("Escolha um numero dos citados acima:")
cpf = "".join(random.sample(numeros, digitos))
cpf = cpf + escolher_estado
print(f"Seu cpf está quase completo, ele está assim:{cpf}")


def calculo_digitoX(cpf):
  multiplicador = 10
  soma_total = 0
  for digito in cpf:
    soma_total += int(digito) * multiplicador
    multiplicador -= 1
  resto = (soma_total*10) % 11 
  X = resto
  if resto > 9:
    X = 0
  print(f"O digito X é: {X}")
  cpf = cpf + str(X)
  return X

cpf = cpf + str(calculo_digitoX(cpf))


def calculo_digitoY(cpf):
    multiplicador = 11
    soma_totalY = 0
    for digitoY in cpf:
      soma_totalY += int(digitoY) * multiplicador
      multiplicador -= 1
    restoY = (soma_totalY*10) % 11
    Y = restoY
    if Y > 9:
      Y = 0
    print(f"Digito Y é: {Y}")
    return Y

cpf = cpf + str(calculo_digitoY(cpf))
print(f"Seu cpf gerado é {cpf}")
