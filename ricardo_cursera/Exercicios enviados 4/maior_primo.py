def maior_primo(k):
  n = 2
  numero = 0
  if k<2:
    return "Teste: Não é possivel calcular"
  else:
    while n<=k:
      if all(n%x!=0 for x in range(2,n)):
        numero=n
        n=n+1
      else:
        n=n+1
  return numero
