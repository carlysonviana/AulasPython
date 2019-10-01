#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
n4 = int(input("Digite o quarto numero: "))

maior = n1
menor = n1
media = (n1 + n2 + n3 + n4)/4

# verifica menor numero
if n2 < n1 and n2 < n3 and n2 < n4 :
    menor = n2
if n3 < n1 and n3 < n2 and n3 < n4:
    menor = n3
if n4 < n1 and n4 < n2 and n4 < n3:
    menor = n4

# verifica maior numero
if n2 > n1 and n2 > n3 and n2 > n4 :
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3:
    maior = n4

print("O maior numero: %d" % maior)
print("O menor numero: %d" % menor)
print("A media: %.2f" % media)
print("A diferença entre %.2f e %d: %.2f" % (media, n1, media - n1))
print("A diferença entre %.2f e %d: %.2f" % (media, n2, media - n2))
print("A diferença entre %.2f e %d: %.2f" % (media, n3, media - n3))
print("A diferença entre %.2f e %d: %.2f" % (media, n4, media - n4))

