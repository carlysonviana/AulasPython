#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lista = ['A','B','C','D','E','F','G','H','I','J']

while True:
    senha = input("Digite uma senha: ")
    if len(senha) < 6:
        print("Senha invalida!")
        pass
    elif len([x for x in senha if x not in lista]) != 0:
        print("Senha invalida!")
        pass
    else:
        senha = senha.replace('A','@')
        senha = senha.replace('B','>')
        senha = senha.replace('C','Ç')
        senha = senha.replace('D','4')
        senha = senha.replace('E','3')
        senha = senha.replace('F','\\')
        senha = senha.replace('G',']')
        senha = senha.replace('H','?')
        senha = senha.replace('I','(')
        senha = senha.replace('J','+')
        break

print("Nova senha criptografada é: %s" % senha)

