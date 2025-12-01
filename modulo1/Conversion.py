#Utilizando prática de conversão de tipos de variáveis

print(int(5.99))

calculo = "100"

print(int(calculo) + 50)

dolar = 5.33
reais = 169

reais = int(reais)

precoCalculado = dolar * reais

precoArredondado = int(precoCalculado)

print(precoArredondado)

#Para arredondar corretamente, é usado a função round()

print(round(precoCalculado))



