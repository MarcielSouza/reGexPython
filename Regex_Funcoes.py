import re

print("\n000------------------------------------------------------------\n")

# findall() : A função retorna uma lista contendo todas as correspondências.

# Exemplo 00 : Imprime uma lista de todas as correspondências:

txta = 'The rain Spain'

#Retorna uma lista contendo todas as ocorrências de "ai":

a = re. findall('ai',txta)

print(a)

print("\n------------------------------------------------------------\n")

#A lista contém as correspondências na ordem em que são encontradas. Se nenhuma correspondência for encontrada, uma lista vazia será retornada [].

# Exemplo 02 : Imprime uma lista de todas as correspondências, caso exista:

txtb = "The rain in Spain"

b = re.findall("Portugal", txtb)

print(b)

#----==============================================================================================================================================================----#

print("\n001------------------------------------------------------------\n")

# search() : A função search() pesquisa a string por uma correspondência e retorna um objeto Match se houver uma correspondência.
#            Se houver mais de uma correspondência, apenas a primeira ocorrência da correspondência será retornada:

# Exemplo 00: Procura o primeiro caractere de espaço em branco na string:

txtc = "The rain in Spain"

c = re.search("\s",txtc)

print("O primeiro caractere de espaço em branco está localizado na posição:", c.start())

print("\n------------------------------------------------------------\n")

# Exemplo 01: Faça uma pesquisa que não retorne nenhuma correspondência:

# Se nenhuma correspondência for encontrada, retornará None.

import re

txtd = "The rain in Spain"

d = re.search("Portugal", txtd)

print(d)

#----==============================================================================================================================================================----#

print("\n002------------------------------------------------------------\n")

# split() : A função retorna uma lista onde a string foi dividida em cada partida:

# Exemplo 00: Dividir em cada caractere de espaço em branco:

txte = "The rain in Spain"

#Divide a string em cada caractere de espaço em branco:

e = re.split("\s", txte)

print(e)

print("\n------------------------------------------------------------\n")

#Você pode controlar o número de ocorrências especificando o parâmetro maxsplit:

# Exemplo 01: Divide a string apenas na primeira ocorrência:

# Divida a string no primeiro caractere de espaço em branco:

txtf = "The rain in Spain"

f = re.split("\s", txtf, 1)

print(f)

#----==============================================================================================================================================================----#

print("\n003------------------------------------------------------------\n")


# sub() : A função substitui as correspondências pelo texto de sua escolha:

# Exemplo 00: Substitua cada caractere de espaço em branco pelo número 9:

txtg = "The rain in Spain"

g = re.sub("\s", "9", txtg)

print(g)

print("\n------------------------------------------------------------\n")

# Você pode controlar o número de substituições especificando o parâmetro count:

# Exemplo 01: Substitua as 2 primeiras ocorrências:

# Substitua as duas primeiras ocorrências de um caractere de espaço em branco pelo dígito 9:

txth = "The rain in Spain"

h = re.sub("\s", "9", txth, 2)

print(h)

#----==============================================================================================================================================================----#

print("\n004------------------------------------------------------------\n")

# Match Object : É um objeto que contém informações sobre a pesquisa e o resultado.

#Observação: se não houver correspondência, o valor será retornado 'None', em vez do Match Object.

# Exemplo 00: Faça uma pesquisa que retornará um Match Object:

#A função search() retorna um objeto Match:

txti = "The rain in Spain"

i = re.search("ai", txti)

print(i) #irá imprimir um objeto

print("\n------------------------------------------------------------\n")

#-----------------------------------------------------------------------------------------------------------------
''' O objeto Match possui propriedades e métodos usados para recuperar informações sobre a pesquisa e o resultado: 
 
.span() retorna uma tupla contendo as posições inicial e final da correspondência.
.string retorna a string passada para a função
.group() retorna a parte da string onde houve uma correspondência '''
#-----------------------------------------------------------------------------------------------------------------

# Exemplo 01: Imprima a posição (posição inicial e final) da primeira ocorrência de correspondência.
#             A expressão regular procura qualquer palavra que comece com "S" maiúsculo:

#Procura um caractere "S" maiúsculo no início de uma palavra e imprima sua posição:

txtj = "The rain in Spain"

j = re.search(r"\bS\w+", txtj)

print(j.span())

print("\n------------------------------------------------------------\n")

# Exemplo 02: Imprima a string passada na função:

# A propriedade string retorna a string de pesquisa:

txtl = "The rain in Spain"

l = re.search(r"\bS\w+", txtl)

print(l.string)

print("\n------------------------------------------------------------\n")

# Exemplo 03: Imprima a parte da string onde houve uma correspondência.
#             A expressão regular procura qualquer palavra que comece com "S" maiúsculo:

#Procure um caractere "S" maiúsculo no início de uma palavra e imprima a palavra:

txtm = "The rain in Spain"

m = re.search(r"\bS\w+", txtm)

print(m.group())







