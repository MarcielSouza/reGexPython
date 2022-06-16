# Sets (Conjuntos)
# Um conjunto é um conjunto de caracteres dentro de um par de colchetes [] com um significado especial

import re

#----==============================================================================================================================================================----#

print("\n000-----------------------------------------\n")

# Set 	                                            Description
# [arn]      Retorna uma correspondência em que um dos caracteres especificados (a, r ou n) está presente

txta = "The rain in Spain"

#Verifique se a string tem algum caractere a, r ou n:

a = re.findall("[arn]", txta)

print(a)

if a:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n001-----------------------------------------\n")

# Set 	                                            Description
# [a-n]       Retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre a e n

txtb = "The rain in Spain"

b = re.findall("[a-n]",txtb)

print(b)

if b:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n002-----------------------------------------\n")

# Set 	                                            Description
# [^arn]                      Retorna uma correspondência para qualquer caractere EXCETO a, r e n

txtc = "The rain in Spain"

#Verifique se a string tem outros caracteres além de a, r ou n:

c = re.findall("[^arn]",txtc)

print(c)

if c:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n003-----------------------------------------\n")

# Set 	                                            Description
# [0123] 	        Retorna uma correspondência onde qualquer um dos dígitos especificados (0, 1, 2 ou 3) está presente

txtd = "The rain in Spain"

#Verifique se a string tem 0, 1, 2 ou 3 dígitos:

d = re.findall("[0123]",txtd)

print(d)

if d:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n004-----------------------------------------\n")

# Set 	                                            Description
# [0-9] 	                        Retorna uma correspondência para qualquer dígito entre 0 e 9

txte = "The rain in Spain"

#Verifica se a string tem algum dígito:

e = re.findall("[0-9]",txte)

print(e)

if e:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n005-----------------------------------------\n")

# Set 	                                            Description
# [0-5][0-9]                Retorna uma correspondência para qualquer número de dois dígitos de 00 e 59

txtf = "8 times before 11:45 AM"

#Verifique se a string possui números de dois dígitos, de 00 a 59:

f = re.findall("[0-5][0-9]", txtf)

print(f)

if f:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----==============================================================================================================================================================----#

print("\n006-----------------------------------------\n")

# Set 	                                            Description
# [a-zA-Z]           Retorna uma correspondência para qualquer caractere em ordem alfabética entre aez, minúsculas OU maiúsculas

txtf = "8 times before 11:45 AM"

#Verifique se a string possui números de dois dígitos, de 00 a 59:

f = re.findall("[0-5][0-9]", txtf)

print(f)

if f:
  print("Yes, there is at least one match!")
else:
  print("No match")

