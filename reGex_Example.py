#Site tutorial  https://www.w3schools.com/python/python_regex.asp

import re

#Verifica se a string começa com "The" a termina com "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
