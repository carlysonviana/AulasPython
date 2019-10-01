#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print("MAIOR")
    print("A diferença entre %d e %d: %d" % (n1, n2, n1 - n2))
if n2 > n1:
    print("MENOR")
    print("A diferença entre %d e %d: %d" % (n2, n1, n2 - n1))
if n1 == n2:
    print("IGUAIS")
    print("A soma de %d e %d: %d" % (n1, n2, n1 + n2))

