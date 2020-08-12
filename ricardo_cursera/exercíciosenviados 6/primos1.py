def ehPrimo(n):
    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        i = 3
        while (i <= (n / i)):
            if ((n % i) == 0):
                return False
            i += 2
        return True

    return False

       
def n_primos(n):

    if (n < 2):
        return 0
    elif (n == 2):
        return 1
    else:
        contador = 1
        while (n > 2):
            if (ehPrimo(n)):
                contador += 1
            n -= 1
        return contador

    return 0

#funcao para retornar o maior numero primo
def maior_primo(n):

    if (n < 2):
        return 0
    elif (n == 2):
        return 2
    else:
        
        while (n > 2):
            if (ehPrimo(n)):
                return n
            n -= 1
        return n

    return 0
