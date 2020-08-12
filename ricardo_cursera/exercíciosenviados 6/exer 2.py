
largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))
# Imprime a borda superior:
print('#' * largura)
# Imprime bordas laterais:
for c in range(altura-2):
    print('#' + ' ' * (largura-2) + '#')
# Imprime borda inferior:
print('#' * largura)
