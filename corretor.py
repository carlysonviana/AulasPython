#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('GABARITO.TXT', 'r') as f:
    gabarito = f.read()    
    CORRETO = gabarito.split()


# In[2]:


with open('RESPOSTA.TXT', 'r') as f:
    resposta = f.read()    
    resp = resposta.split()
    
    MATRICULA = []
    RESPOSTA = []
    for r in resp:
        MATRICULA.append(r[0:5])
        RESPOSTA.append(r[5:25])


# In[3]:


# avaliar respostas se corretas 'S' ou erradas 'N'
RESULTADO = []
for x in range(25):
    RESP_split = list(RESPOSTA[x])
    result = ""
    for y in range(20):
        if CORRETO[y] == RESP_split[y]: # compara gabarito com resposta individualmente
            result = result + CORRETO[y] + RESP_split[y] + "S "
        else:
            result = result + CORRETO[y] + RESP_split[y] + "N "
    
    RESULTADO.append(MATRICULA[x] + result)

# contar quantidade de acertos por matricula
for x in range(25):
    count = 0
    for y in RESULTADO[x]:
        if y == 'S':
            count+=1
        # calcular a nota final
        if count > 13:
            nota = "A"
        elif count > 8 and count < 14:
            nota = "X"
        else:
            nota = "R"
        
  
    if count < 10:
        count = "0" + str(count)
    else:
        count = str(count)
    
    RESULTADO[x] = RESULTADO[x] + count + " " +  nota
        

with open('RESULTADO.TXT', 'w') as f:
    f.write('\n'.join(RESULTADO))


# In[4]:


# verificar quantidade de aprovados, em exame e reprovados
count_ap = 0
count_ex = 0
count_rep = 0
for n in RESULTADO:
    if n[-1] == 'A':
        count_ap+=1
    elif n[-1] == 'X':
        count_ex+=1
    else:
        count_rep+=1

print("A qtde de aprovados: %s" % (str(count_ap)))
print("A qtde de em exame: %s" % (str(count_ex)))
print("A qtde de reprovados: %s" % (str(count_rep)))


# In[61]:


# verificar questões com mais acertos e erros
acertos = []
erros = []
for m in range(7,84,4):
    count_S = 0
    count_N = 0
    for n in RESULTADO:
        if n[m] == 'S':
            count_S+=1
        else:
            count_N+=1
    acertos.append(count_S)
    erros.append(count_N)

max_acertos_index = []
max_erros_index = []
for a in acertos:
    if a == max(acertos):
        max_acertos_index.append(str(acertos.index(a) + 1))
        
for e in erros:
    if e == max(erros):
        max_erros_index.append(str(erros.index(e) + 1))
    

print("A(s) questão(ões) que tiveram mais acertos: %s" % (" ".join(max_acertos_index)))
print("A(s) questão(ões) que tiveram mais erros: %s" % (" ".join(max_erros_index)))

# quantidade de acertos e erros de cada questão
ultima_linha = ""
for n in range(20):
    if acertos[n] < 10:
        acertos_str = "0" + str(acertos[n])
    else:
        acertos_str = str(acertos[n])
    if erros[n] < 10:
        erros_str = "0" + str(erros[n])
    else:
        erros_str = str(erros[n])
    if n == 0:
        ultima_linha = ultima_linha + " " + acertos_str + erros_str
    else:
        ultima_linha = ultima_linha + ", " + acertos_str + erros_str
        
print("     %s" % ultima_linha)

