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

