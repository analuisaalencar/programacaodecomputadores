#Alunas: Ana Luisa da Costa Alencar e Marcella Alves Athaydes.
#Entrada: numero de 5 digitos inserido.
#digito<- le o numero inserido.
#digito1<- le o digito 1 dividido por 10000.
#digito2<- le o resto da divisão de digito1 dividido por 1000.
#digito3<- le o resto da divisão de digito2 dividido por 100.
#digito4<- le o resto da divisão de digito3 dividido por 10.
#digito5< le o resto da divisão de digito4 dividido por 1.
#le se o digito1 é igual ao digito5 e se o digito2 é igual ao digito4.
#se forem iguais, imprime "é um palindromo".
#se não forem iguais, imprime "não é um palindromo".
#Saída: Dizer de o numero é palindromo ou não.

digito = int(input("Digite um número de 5 dígitos: "))
digito1 = digito // 10000
digito2 = (digito % 10000) // 1000
digito3 = (digito % 1000) // 100
digito4 = (digito % 100) // 10
digito5 = digito % 10

if digito1 == digito5 and digito2 == digito4:
    print("É palíndromo")
else:
    print("Não é palíndromo")
