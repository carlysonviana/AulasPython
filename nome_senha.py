#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    nome = input("Digite o nome do usuario: ")
    senha = input("Digite a senha do usuario: ")
    
    if nome != senha and len(nome) >= 5 and len(senha) >= 5:
        print("VÁLIDOS")
        break

