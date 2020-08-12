def vogal(letra):
    vogais = "aeiou"
# verificar se a letra digitada minuscula nao existe na nossa variavel vogais    
    if letra.lower() not in vogais: 
        return False
    return True
