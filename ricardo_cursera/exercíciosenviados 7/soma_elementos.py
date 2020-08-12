def soma_elementos(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma
l = [1,2,3]
print(soma_elementos(l))
