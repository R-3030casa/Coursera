import re

def le_assinatura():
    """A função le os valores dos traços linguisticos do modelo e
        devolve uma assinatura a ser comparada com os textos fornecidos"""
    print('Bem-vindo ao detector automático de COH-PIAH.')
    print('Informe a assinatura típica de um aluno infectado:')
    
    wal = float(input('Entre o tamanho médio de palavra:' ))
    ttr = float(input('Entre a relação Type-Token:' ))
    hlr = float(input('Entre a razão Hapax Legomana:' ))
    sal = float(input('Entre o tamanho médio de sentenças:' ))
    sac = float(input('Entre a complexidade média da sentença:' ))
    pal = float(input('Entre o tamanho médio de frase:' ))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    """A função le todos os textos a serem comparados e devolve uma
        lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input('Digite o texto ' + str(i) + '(aperte enter para sair):')
    while texto:
        textos.append(texto)
        i += 1
        texto = input('Digite o texto ' + str(i) + '(aperte enter para sair):')
        
    return textos
    
def separa_sentencas(texto):
    """"A Função recebe um texto e devolve uma lista das sentenças
        dentro do texto"""
    sentencas = re.split(r'[.!?]+',texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    """A Função recebe uma sentenca e devolve uma lista das
        frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    """A Função recebe uma frase e devolve uma lista das
        palavras dentro da frase"""
    return frase.split()

def n_palavras_unicas(lista_palavras):
    """Essa Função recebe uma lista de palavras e devolve o número
        de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
            
    return unicas
            
def n_palavras_diferentes(lista_palavras):
    """Essa função recebe uma lista de palavras e devolve o número
        de palavras diferentes utilizadas."""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
            
    return len(freq)

def compara_assinatura(as_a, as_b):
    """Essa função recebe duas assinaturas de texto e deve
        devolver o grau de similaridade nas assinaturas."""
    Sab = 0
    i = 0
    while i < 6:
        Sab = Sab + abs(as_a[i] - as_b[i])
        i += 1
    return Sab/6

def avalia_textos(textos, ass_cp):
    """Essa função recebe uma lista de textos e uma assinatura ass_cp
        e deve devolver o numero (1 a n) do texto com maior probalbilidade
        de ter sido infectado por COH-PIAH."""
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    comparacao = []
    for assinatura in assinaturas:
        comparacao.append(compara_assinatura(assinatura, ass_cp))
    comp = comparacao[0]
    n = 0
    texto = 1
    for compara in comparacao:
        n += 1
        if compara < comp:
            comp = compara
            texto = n
    return texto

def conta_tamanho_palavras_sentencas(texto):
    tamanho = 0
    pontuacoes_espaco = ['.', '!', '?']
    for letra in texto:
        if not letra in pontuacoes_espaco:
            tamanho += 1
    return tamanho

def conta_tamanho_palavras_frases(texto):
    tamanho = 0
    pontuacoes_espaco = [':', ',', ';']
    for letra in texto:
        if not letra in pontuacoes_espaco:
            tamanho += 1
    return tamanho

def conta_tamanho_palavras(texto):
    tamanho = 0
    pontuacoes_espaco = ['.', ':', ',', ';', '!', '?']
    for letra in texto:
        if not letra in pontuacoes_espaco:
            tamanho += 1
    return tamanho

                         
def calcula_assinatura(texto):
    """Essa Função recebe um texto e deve devolver a assinatura do texto """
    sentencas = []
    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    tamanho_sentencas = 0
    tamanho_frases = 0
    tamanho_palavras = 0

    for sentenca in sentencas:
        tamanho_sentencas = tamanho_sentencas + conta_tamanho_palavras_sentencas(sentenca)
    
    for frase in frases:
        tamanho_frases = tamanho_frases + conta_tamanho_palavras_frases(frase)

    for palavra in palavras:
        tamanho_palavras = tamanho_palavras + conta_tamanho_palavras(palavra)
    #Tamanho médio de palavra - soma dos tamanhos das palavras dividida pelo número total de palavras    
    wal = tamanho_palavras/len(palavras)
    palavras_diferentes = n_palavras_diferentes(palavras)
    #Relação Type-Token - número de palavras diferentes dividido pelo número total de palavras
    ttr = palavras_diferentes/len(palavras)
    palavras_unicas = n_palavras_unicas(palavras)
    #Razão Hapax Legomana - número de palavras que aparecem uma única vez dividido pelo total de palavras
    hlr = palavras_unicas/len(palavras)
    #Tamanho médio de sentença -  soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    sal = tamanho_sentencas/len(sentencas)
    #Complexidade média da sentença - número total de frases divido pelo número de sentenças
    sac = len(frases)/len(sentencas)
    #Tamanho medio de frase - soma do número de caracteres em cada frase dividida pelo número de frases
    pal = tamanho_frases/len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

assinatura_modelo = le_assinatura()
textos = le_textos()
texto_infectado = avalia_textos(textos, assinatura_modelo)
print("O autor do texto", texto_infectado,"está infectado com COH-PIAH")
        
                           
                    

    
    






















    






















