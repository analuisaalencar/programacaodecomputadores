#Alunas: Ana Luísa da Costa Alencar e Marcella Alves Athaydes 
#Entradas: Número de 5 dígitos digitado 
#Saída: Ler o número de 5 digitos e dizer se é ou não palíndromo	


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
