# Metacaracteres

# Metacaracteres são caracteres com um significado especial:

print("\n000------------------------------------------\n")

import re  #modulo Regex Python

# Character	    Description         	    Example
# []	     A set of characters	        "[a-m]"

#Acha todos caraceteres minusculos em ordem alfabética entre "a" e "m":

txta = "The rain in Spain"

a = re.findall("[a-m]", txta)
print(a)

#----======================================================================================================================----#

print("\n001------------------------------------------\n")

# Character	                                    Description                                                        Example
# \	            Pega uma sequência numerica (também pode ser usada para escapar de caracteres especiais)            "\d"

#Achar todos os caracteres númericos:

txtb = "That will be 5989 dollars"

b = re.findall("\d", txtb)
print(b)

#----======================================================================================================================----#

print("\n002------------------------------------------\n")

# Character	                                    Description                                     Example
# .	                          Qualquer caractere (exceto caractere de nova linha)               "he..o"

#Procure uma sequência que comece com "he", seguido por dois (qualquer) caracteres e um "o":

txtc = "hello planet"

c = re.findall("he..o", txtc)
print(c)

#----======================================================================================================================----#

print("\n003------------------------------------------\n")

# Character	                                    Description                                     Example
# ^	                                            Comeca com                                     "^hello"

#Verifica se uma string comeca com 'hello'

txtd = "hello planet"

d = re.findall("^hello", txtd)
if d:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#----======================================================================================================================----#

print("\n004------------------------------------------\n")

# Character	                                    Description                                     Example
# $	                                            Termina com                                     "$planet"

#Verifica se uma string termina com 'planet'

txte = "hello planet"

e = re.findall("planet$", txte)
if e:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#----======================================================================================================================----#

print("\n005------------------------------------------\n")

# Character	                                    Description                                     Example
# *	                                       Zero ou mais ocorrencias                             "he.*o"

#Procura por uma sequencia que comeca com "he", seguido por 0 ou mais (qualquer) caracteres, e um "o":

txtf = "hello planet"

f = re.findall("he.*o",txtf)

print(f)

#----======================================================================================================================----#

print("\n006-----------------------------------------\n")

# Character	                                    Description                                     Example
# +	                                       Uma ou mais ocorrencias                              "he.+o"

#Procura por uma sequencia que comeca com "he", seguido por 1 ou mais (qualquer) caracteres, e um "o":

txtg = "hello planet"

g = re.findall("he.+o",txtg)

print(g)

#----======================================================================================================================----#

print("\n007-----------------------------------------\n")

# Character	                                    Description                                     Example
# ?	                                       Zero ou uma ocorrencias                              "he.?o"

#Procura por uma sequencia que comeca com "he", seguido por 0 ou 1 (qualquer) caracteres, e um "o":

txth = "hello planet"

h = re.findall("he.?o",txth)

print(h)

#Desta vez não obtivemos correspondência, porque não havia zero, nem um, mas dois caracteres entre "he" e "o"

#----======================================================================================================================----#

print("\n008-----------------------------------------\n")

# Character	                                    Description                                     Example
# {}	                        Exatamente o número especificado de ocorrências                "he.{2}o"

#Procura por uma sequencia que comeca com "he", seguido por exatamente 2 (qualquer) caracteres, e um "o"

txti = "hello planet"

i = re.findall("he.{2}o",txti)

print(i)

#----======================================================================================================================----#

print("\n009-----------------------------------------\n")

# Character	                                    Description                                     Example
# |	                                               ou                                        "falls|stays"

#Verifica se a string contém "falls" ou "stays"

txtj = "The rain in Spain falls mainly in the plain!"

j = re.findall("falls|stays",txtj)

print(j)

if j:
    print("Yes, there is at least one match!")
else:
    print("No match")

#----======================================================================================================================----#

print("\n010-----------------------------------------\n")

# Character	                                    Description                                     Example
# ()                                          Captura e agrupa


