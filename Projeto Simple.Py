# Solicitação dos dados do usuário
tempo_fumando = float(input("Tempo como fumante (em anos).....: "))
valor_macos = float(input("Valor do maço......................: "))
macos_dia = float(input("Quantidade de maços por dia..........: "))

# Calculando o montante gasto com o tabagismo
dias_fumando = tempo_fumando * 12 * 30
macos_total = dias_fumando * macos_dia
montante_gasto = macos_total * valor_macos

# Verificando em qual faixa de valor o usuario se encaixa e exibindo o resultado
if montante_gasto < 20000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter dado entrada em um carro.")
elif montante_gasto >= 20000 and montante_gasto <= 50000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro zero.")