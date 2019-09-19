cont_asterisco = 1
cont_espaco = 5

for n in range(1, 10):
    print(cont_espaco*" " + cont_asterisco*"*")
    if n < 5:
        cont_asterisco = cont_asterisco + 2
        cont_espaco = cont_espaco - 1
    else:
        cont_asterisco = cont_asterisco - 2
        cont_espaco = cont_espaco + 1
