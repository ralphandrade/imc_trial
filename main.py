# entrada de dados
nome = str(input('informe seu nome: '))
peso = str(input('informe seu peso: ')).replace(',', '.')
altura = str(input('informe sua altura: ')).replace(',', '.')

# converte para float
peso = float(peso)
altura = float(altura)

# calcula imc
imc = peso/(altura*altura)

# referencias/indices imc
if imc >40:
    print(f' O seu imc é {imc:,.2f} você está em obsesidade, grau III. ')
elif imc >=35:
    print(f' O seu imc é {imc:,.2f} você está em  obesidade, grau II. ')
elif imc >=30:
    print(f' O seu imc é {imc:,.2f} você está em obesidade, grau I. ')
elif imc >=25:
    print(f' O seu imc é {imc:,.2f} você está em sobrepeso. ')
elif imc >=18.6:
    print(f' O seu imc é {imc:,.2f} você está com peso normal. ')
else:
    print(f' O seu imc é {imc:,.2f} você está abaixo do peso normal. ')
    


