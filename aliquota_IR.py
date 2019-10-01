#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

count = 0
media = 0

while True:
    nome = input("Digite o nome do funcionario: ")
    salario = input("Digite o salario do funcionario: ")
    salario = re.sub(',', '.', salario)
    salario = float(salario)
    
    '''# calculo da aliquota anterior
        if  salario < 2500.00:
            aliquota = salario*0.15
        else:
            aliquota = salario*0.25
    '''
    
    if salario <= 1500.00:
        aliquota = salario*0.07
    elif 1500.01 <= salario <= 2500.00:
        aliquota = salario*0.12
    elif 2500.01 <= salario <= 5000.00:
        aliquota = salario*0.20
    else:
        aliquota = salario*0.25
        
    print("Deve ser aplicado %d%% ao salario de %s, aliquota recolhida eh R$ %.2f" % 
            (round((aliquota/salario)*100), nome, aliquota)
         )
        
    count = count + 1
    media = media + salario 
    
    continua = input('Deseja inserir outro funcionario: (S/N)').capitalize()
    
    if continua == 'N':
        break

media = media/count
print("A media dos salarios dos funcionarios eh R$ %.2f" % media)

