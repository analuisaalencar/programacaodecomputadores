"""

Faça um programa para, a partir de um valor
informado em centavos, indicar a menor
quantidade de moedas que representa esse valor
– Considere moedas de 1, 5, 10, 25 e 50 centavos, e 1 real
– Exemplo: para o valor 290 centavos, a menor
  quantidade de moedas é 2 moedas de 1 real, 1 moeda
  de 50 centavos, 1 moeda de 25 centavos, 1 moeda de
  10 centavos e 1 moeda de 5 centavos
"""

valor = int(input("Digite o valor em centavos\n"))

moeda100 = 100
moeda50 = 50
moeda25 = 25
moeda10 = 10
moeda5 = 5
moeda1 = 1

qt_moeda100 = valor // moeda100
valor = valor % moeda100
qt_moeda50 = valor // moeda50
valor = valor % moeda50
qt_moeda25 = valor // moeda25
valor = valor % moeda25
qt_moeda10 = valor // moeda10
valor = valor % moeda10
qt_moeda5 = valor // moeda5
valor = valor % moeda5
qt_moeda1 = valor // moeda1
valor = valor % moeda1
"""
print("Quantidade moedas 1  real     =", qt_moeda100)
print("Quantidade moedas 50 centavos =", qt_moeda50)
print("Quantidade moedas 25 centavos =", qt_moeda25)
print("Quantidade moedas 10 centavos =", qt_moeda10)
print("Quantidade moedas  5 centavos =", qt_moeda5)
print("Quantidade moedas  1 centavos =", qt_moeda1)
"""



print(("1 real = {}\n50 centavos = {}\n25 centavos = {}\n10 centavos {}\n"+
      "5 centavos {}\n 1 centavo {}").format(qt_moeda100, qt_moeda50, qt_moeda25,qt_moeda25,qt_moeda5,qt_moeda1))



