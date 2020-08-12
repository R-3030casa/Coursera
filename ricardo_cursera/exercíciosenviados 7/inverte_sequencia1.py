lista =[]
num = 1
while num != 0:
    num = int(input('[Para sair digite "0"]digite um número: '))
    if num != 0:
        lista.append(num)
    else:
        break
for i in lista[::-1]:
        print(i)


'''# Lista de valores:
seq = []
# Executa até ocorrer `break`
while True:
    # Pede ao usuário um valor inteiro:
    n = int(input("Digite n: "))    
    # Se for zero, pare o loop:
    if n == 0: break
    # Se não, adiciona o valor a lista:
    seq.append(n)
# Percorre toda a lista de trás para frente:
for i in reversed(seq):
    # Exibe o valor na tela:
    print(i)'''

'''seq = []
while True:
    numero = int(input('N = '))
    if (numero != 0):
        seq.append(numero)
    else:
        break
for i in seq[::-1]:
    print (i)'''
    
