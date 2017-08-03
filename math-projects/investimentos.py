def investimentos():
    # método que calcula quanto o dinheiro rende a uma certa taxa de juros
    montante = 0
    print("Voce pretende investir depositando:\n" +
          "1 - Todo mês\n" +
          "2 - Apenas uma vez")
    opcao = int(input(""))
    capital_inicial = float(input("Quanto pretende investir (em reais) ?\n"))
    taxa = float(input("Qual a taxa dos juros compostos em porcentagem ?\n"))
    print("Por quantos meses deseja investir ?".format(capital_inicial))
    tempo = float(input(""))
    if opcao == 1:
        tmp = tempo
        montante = capital_inicial*(1+(taxa/100))
        tmp -= 1
        print(montante)
        while tmp > 0:
            montante = montante*(1+(taxa/100)) + capital_inicial
            print(montante)
            tmp -= 1
      
    if opcao == 2:
        montante = capital_inicial*(1+(taxa/100))**tempo
    print("\nInvestindo R$ {}, durante {} meses a uma taxa de {}% da um total de R$ {}\n"
          .format(capital_inicial, tempo, taxa, montante))
while True:
    try:
        investimentos()
    except:
        print("Comando inválido !")
