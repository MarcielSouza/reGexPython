# Uma sequência especial é '\' seguida por um dos caracteres na lista abaixo e tem um significado especial:

import re

#----==============================================================================================================================================================----#

print("\n000-----------------------------------------\n")

# Character	                                         Description                                                                                              Example
# \A                 Retorna uma correspondência se os caracteres especificados estiverem no início da string                                                 "\AThe"

#Verifica se a string comeca com "The"

txta = "The rain in Spain"

a = re.findall("\AThe",txta)

print(a)

if a:
    print("Yes, there is a match!")
else:
    print("No match")

#----==============================================================================================================================================================----#

print("\n001-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
# \b           Retorna uma correspondência em que os caracteres especificados estão no início ou no final de uma palavra                                     r"\bain"
#                  (o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")                                         r"ain\b"

#Verifica se "ain" existe no inicio da PALAVRA:

txtb = "The rain in Spain"

b = re.findall(r"\bain",txtb)

print(b)

if b:
    print("Yes, there is at least one match!")
else:
    print("No match")

print("\n-------------------------------------------------------------------\n")

#Verifica se "ain" existe no fim da PALAVRA:

txtc = "The rain in Spain"

c = re.findall(r"ain\b",txtc)

print(c)

if c:
    print("Yes, there is at least one match!")
else:
    print("No match")

#----==============================================================================================================================================================----#

print("\n002-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
# \B                Retorna uma correspondência onde os caracteres especificados estão presentes, mas NÃO no início (ou no final) de uma palavra             r"\Bain"
#                           (o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")                                r"ain\B"

txtd = "The rain in Spain"

#Verifique se "ain" está presente, mas NÃO no início de uma palavra:

d = re.findall(r"\Bain", txtd)

print(d)

if d:
  print("Yes, there is at least one match!")
else:
  print("No match")


print("\n-------------------------------------------------------------------\n")

txte = "The rain in Spain"

#Verifique se "ain" está presente, mas NÃO no início de uma palavra:

e = re.findall(r"ain\B", txte)

print(e)

if e:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n003-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\d 	                             Retorna uma correspondência em que a string contém dígitos (números de 0 a 9)                                            "\d"

txtf = "The rain in 29 Spain"

#Verifique se a string contém algum dígito (números de 0 a 9):

f = re.findall("\d",txtf)

print(f)

if f:
    print("Yes, there is at least one match!")
else:
    print("No match")

#----=============================================================================================================================================================----#

print("\n004-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\D                             Retorna uma correspondência onde a string NÃO contém dígitos                                                                  "\D"

txtg = "The rain in Spain"

#Retorna uma correspondência em cada caractere sem dígito:

g = re.findall("\D", txtg)

print(g)

if g:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n005-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\s                         Retorna uma correspondência onde a string contém um caractere de espaço em branco                                                 "\s"

txth = "The rain in Spain"

#Retorna uma correspondência em cada caractere de espaço em branco:

h = re.findall("\s", txth)

print(h)

if h:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n006-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\s                         Retorna uma correspondência onde a string contém um caractere de espaço em branco                                                 "\s"

txti = "The rain in Spain"

#Retorna uma correspondência em que a string NÃO contém um caractere de espaço em branco:

i = re.findall("\S", txti)

print(i)

if i:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n007-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\w                         Retorna uma correspondência em que a string contém qualquer caractere de                                                          "\w"
#                           palavra (caracteres de a a Z, dígitos de 0 a 9 e o caractere sublinhado _)

txtj = "The rain in Spain"

#Retorna uma correspondência em cada caractere de palavra (caracteres de a a Z, dígitos de 0 a 9 e o caractere sublinhado _ ):

j = re.findall("\w", txtj)

print(j)

if j:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n008-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\W                           Retorna uma correspondência em que a string NÃO contém nenhum caractere de palavra                                               "\W"

txtl = "The rain in Spain"

#Retorna uma correspondência em cada caractere NÃO de palavra (caracteres NÃO entre a e Z. Como "!", "?" espaço em branco etc.):

l = re.findall("\W", txtl)

print(l)

if l:
  print("Yes, there is at least one match!")
else:
  print("No match")

#----=============================================================================================================================================================----#

print("\n009-----------------------------------------\n")

# Character	                                         Description                                                                                             Example
#\Z                          Retorna uma correspondência se os caracteres especificados estiverem no final da string                                        "Spain\Z"

txtm = "The rain in Spain"

#Verifique se a string termina com "Spain":

m = re.findall("Spain\Z", txtm)

print(m)

if m:
  print("Yes, there is a match!")
else:
  print("No match")
