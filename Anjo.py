'''
tabela INSS
salario, aliquota
1751.81, 8%
2919.72, 9%
5839.45, 11%

tabela IRFF
base, aliquota, parcela a decidir
2826.65, 7.5%, 142.80
3751.05, 15%, 354.80
4664.68, 22.5, 636.13
Acima de 4664.68, 27.5, 869.36

#nome, proventos, inss, irff, salario final
'''

def CalculoINSS(salario):
  if salario <= 1751.81:
    salario = salario * 0.08
    return salario
  elif 1751.81 < salario <= 2919.72:
    salario = salario * 0.09
    return salario
  elif 2919.72 < salario <= 5839.45:
    salario = salario * 0.11
    return salario


def CalculoIRFF(salario):
  if salario <= 2826.65:
    salario = salario * 0.075
    return salario
  elif 2826.65 < salario <= 3751.05:
    salario = salario * 0.15
    print(salario)
    return salario
  elif 3751.05 < salario <= 4664.68:
    salario = salario * 0.225
    return salario
  elif 4664.68 < salario:
    salario = salario * 0.275
    return salario
    
while True:
  print("Insira o seu salário")
  salario = int(input(""))

  salarioFinal = salario - CalculoINSS(salario) - CalculoIRFF(salario)
  
  print("O seu salário final é de: " + str(salarioFinal))
