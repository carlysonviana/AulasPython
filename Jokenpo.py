#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rd

opcoes = ['Pedra', 'Papel', 'Tesoura']
meuPlacar = 0
maquinaPlacar = 0

while (meuPlacar or maquinaPlacar) < 3:
    maquinaOpcao = rd.choice(opcoes)
    minhaOpcao = input('pedra, papel ou tesoura?: ')
    print ('máquina: ' + maquinaOpcao)
    
    if minhaOpcao.capitalize() == 'Papel' and  maquinaOpcao == 'Pedra':
        meuPlacar += 1
    elif minhaOpcao.capitalize() == 'Tesoura' and maquinaOpcao == 'Papel':
        meuPlacar += 1
    elif minhaOpcao.capitalize() == 'Pedra' and maquinaOpcao == 'Tesoura':
        meuPlacar += 1
    elif minhaOpcao.capitalize() == maquinaOpcao:
        continue
    else: 
        maquinaPlacar += 1
    
    print('Placar atualizado:')
    print ('eu: ' + str(meuPlacar))
    print ('máquina: ' + str(maquinaPlacar))
        
    if meuPlacar == 2:
        print ('Parabéns você venceu!!!')
        break
    elif maquinaPlacar == 2:
        print('Que pena você perdeu!!!')
        break

