#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re 

dic = {}

while True:
    nome = input("Digite um nome: ")
    
    salario = input("Digite o salario R$: ")
    salario = re.sub(',', '.', salario)
    salario = float(salario)
    
    dic[nome] = salario
    
    continua = input("Deseja continuar? (S/N): ").capitalize()
    if continua == 'N':
        break

maior = max(dic.items(), key = lambda x: x[1])
menor = min(dic.items(), key = lambda x: x[1])
media = sum(dic.values())/len(dic)
        
print("%s tem o maior salario: R$ %.2f" % (maior[0], maior[1]))
print("%s tem o menor salario: R$ %.2f" % (menor[0], menor[1]))
print("A media dos salarios: R$ %.2f" % media)

