#Alunas: Ana Luísa da Costa Alencar; Marcella Alves Athaydes
#Entrada: numero de funcionarios, quantidade de horas trabalhadas e valor da hora trabalhada.
#N<-le o numero de funcionarios
#Q<-le a quantidade de horas trabalhadas
#V<-le o valor da hora trabalhada
#S<-Q*V
#Escreve S
#Saida: numero do funcionario e quantidade que deve receber

N = int(input(' Digite o numero do funcionario:'))
Q = int(input('Digite o numero de horas trabalhadas:'))
V = float(input('Digite o valor de cada hora trabalhada:'))
S = Q*V
print(' O funcionario de numero', N , 'deve receber', S)