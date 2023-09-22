#Alunas: Ana Luisa da Costa Alencar e Marcella Alves Athaydes.
#Entradas: nome da solução e a concentração de ions de hidrogenio em mol/litro.
#N<- le o nome da solução.
#H<- le a concentração de ions de higrogenio em mol/litro.
#ph<- -log10(H) ( calcula o ph ).
#Se o ph calculado for igual a 7, imprime que a solução é neutra.
#Se o ph calculado for menor do que 7, imprime que a solução é ácida.
#Se o ph calculado for maior do que 7, imprime que a solução é básica.
#Se o ph for menor que 0 ou maior que 14, imprime que o valor do ph está fora dos padrões.
#Saída: valor do ph calculado e o tipo da solução.

import math
N = input("Informe o nome da solução:")
H = float(input("Informe a concentração de íons de H da solução em mol/litro:"))
ph = -math.log10(H)
if ph == 7:
    print("O valor do ph de", N , "é", ph , ",logo, a solução é neutra")
elif ph < 7 and ph > 0:
    print("O valor do ph de", N , "é", ph , ",logo, a solução é ácida")
elif ph < 14:
    print("O valor do ph de", N , "é", ph , ",logo, a solução é básica")
else:
    print(" O valor do ph está fora dos padrões")
