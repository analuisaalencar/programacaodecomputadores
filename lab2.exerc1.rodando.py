#Alunas: Ana Luísa da Costa Alencar e Marcella Alves Athaydes 
#Entrada:Ler valores 4 valores inteiros 
#Saída: Ler os valores e dizer se é ou não aceito
#A <- Ler um valor inteiro
#B <- Ler um valor inteiro
#C <- Ler um valor inteiro
#D <- Ler um valor inteiro
#Se B > C e D > A e C + D > A + B e C > 0 e D > 0 e A % 2 == 0 
#Se for Escreva "Valores aceitos"
#Senão Escreva "Valores não aceitos"

A = int(input("Digite o primeiro valor inteiro:"))
B = int(input("Digite o segundo valor inteiro: "))
C = int(input("Digite o terceiro valor inteiro: "))
D = int(input("Digite o quarto valor inteiro:"))

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else: 
    print("Valores não aceitos")