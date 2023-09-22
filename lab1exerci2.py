#Alunas: Ana Luísa da Costa Alencar; Marcella Alves Athaydes
#Entrada: raio, altura e massa do cilindro.
#R<-le o valor do raio.
#H<-le o valor da altura.
#M<-pi * raio ao quadrado * altura.
#Escreve M.
#Saida: valor da massa calculado.

import math
R = float(input('Digite o valor do raio em centimetros:'))
H = float(input('Digite o valor da altura em centimetros:'))
M = ((math.pi * R**2)*H)*0.001
print('O valor da massa do cilindro é:', M)