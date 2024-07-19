import random

#Gerador de CPF

numero = "0123456789"
tamanho_cpf = 9

menu = int(input("""
        [1] Gerar um CPF
        [2] Verificar se um CPF é valido
        Escolha uma opção:"""))

def gerar_cpf():
  cpf = "".join(random.sample(numero, tamanho_cpf))
  cpf = cpf[0:3] + "." + cpf [2:5] + "." + cpf [5:8] + "-" + "".join(random.sample(numero, 2))
  #Usei os comandos "-" + "".join(random.sample(numero, 2)) para ser gerado os ultimos 2 digitos do cpf.
  #Já que o numeros só vão de 0 a 9, e o cpf precisa de 11, então o sample dava erro
  print(cpf)


def validar_cpf():
  cpf_verify = int(input("Digite os numeros do cpf:"))
  cpf_verify = str(cpf_verify)
  cpf_verify = cpf_verify[0:3] + "." + cpf_verify [2:5] + "." + cpf_verify [5:8] + "-" + "".join(random.sample(numero, 2))  
  if len(cpf_verify) == 14:
    print("CPF válido")
  else:
    print("CPF invalido")
    

if menu == 1:
  print(gerar_cpf())
elif menu == 2:
  print(validar_cpf())
