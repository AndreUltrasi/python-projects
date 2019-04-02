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
  
  
"""
  all might
https://produto.mercadolivre.com.br/MLB-1204362386-boneco-funko-pop-my-hero-academy-all-might-figura-em-vinyl-_JM?quantity=1
70 + 11
de 1 a 3 dias úteis

https://produto.mercadolivre.com.br/MLB-1090121448-my-hero-academia-all-might-funko-pop-_JM?matt_tool=96481908&matt_word&gclid=Cj0KCQjwkIzlBRDzARIsABgXqV-ZtkLhxcY2TOMtoLqfNdo4cOpRUXM2QCPidBRudHfTouDAUA1xn5YaAv8iEALw_wcB&quantity=1
R$ 69,95 +  R$ 11,90
De 1 a 3 dias úteis

vegeta
https://www.americanas.com.br/produto/18166732/boneco-vegeta-dragonball-z-funko-pop?pfm_carac=funko%20pop%20vegeta&pfm_index=0&pfm_page=search&pfm_pos=grid&pfm_type=search_page%20&sellerId
72
10 dias uteis

https://produto.mercadolivre.com.br/MLB-1151312126-funko-pop-animation-dragonball-z-vegeta-10-_JM?matt_tool=96481908&matt_word=&gclid=Cj0KCQjwkIzlBRDzARIsABgXqV8fWUPTLdV_TJArjJxMfNVtg1GUGjgf8VxyHf0d_x3PNBNsZ4PNjkQaAnh3EALw_wcB
70 + 11
1 a 3 dias uteis


dumbo
https://produto.mercadolivre.com.br/MLB-1140513336-funko-pop-disney-series-5-dumbo-50-_JM
83 + 14
De 1 a 3 dias úteis

Boleto Ung
03399.70212 17800.000170 15915.601015 8 78750000076613
544,99

"""
  
