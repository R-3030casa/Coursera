def maior_elemento(lista):
    maior = 0
    for p in lista:
        if p > maior:
            maior = p
        if p < 0:
            maior = p
    return maior


lista = [6,2,3,50]
lista1 = [-90,-30,-12]


