#!/usr/bin/env python
# coding: utf-8

# In[119]:


NOME = []
IDADE = []
SEXO = []

nome = ''
while nome != 'FIM':
    nome = input("Digite o Nome e o Sobrenome: ")
    # garante que encontre um espaço na string
    if nome.find(" ") != -1:
        # garante que: 
        # 1 - até a posição nome[2] não tenha um espaço, logo no mínimo, tem 3 primeiros caracteres antes
        # 2 - existe no mínimo 7 posições na nome, ou seja, 3 no nome + espaço + 3 no sobrenome
        # 3 - caso encontre um espaço, o valor posição encontrado esteja no mínimo antes do nome[-3]
        if nome.find(" ") > 2 and len(nome) >= 7 and ((len(nome) - 1) - nome.find(" ")) > 2:
            NOME.append(nome) 
            #idade = input("Digite a Idade: ")
            #IDADE.append(idade)
            #sexo = input("Digite o sexo: ")
            #SEXO.append(sexo)
        else:
            print("ATENÇÃO: Nome e Sobrenome devem conter mais de 3 caracteres")
    elif nome == 'FIM':
        print("Programa finalizado!")
    else:
        print("ATENÇÃO: Nome devem conter Nome/Sobrenome separados por espaço!")

#faz um cópia independente, senão tudo que seja modificado no ORDEM____, modifica o original
ORDEMNOME = NOME.copy() 
ORDEMIDADE = IDADE.copy()
ORDEMSEXO = SEXO.copy()

# ordenaçao
ordenado = "nao"
tamanho = len(ORDEMNOME)
while ordenado == "nao":
    ordenado = "sim"
    for i in range(0,tamanho -1):
        j = i + 1
        while j < tamanho:
            if ORDEMNOME[i] > ORDEMNOME[j]:
                ordenado = "nao"
                troca = ORDEMNOME[i]
                ORDEMNOME[i] = ORDEMNOME[j]
                ORDEMNOME[j] = troca
            j = j+1
        
    
    
    


# In[117]:


NOME


# In[118]:


ORDEMNOME

