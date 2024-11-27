import string


senha = input("Digite sua senha para a validação: ")

numero_caracteres = len(senha)
maiusculas = 0
minusculas = 0
numeros = 0
simbolos = 0
meio = 0

for i in range(numero_caracteres):
    c = senha[i]
    if c.isupper():
        maiusculas += 1
    elif c.islower():
        minusculas += 1
    elif c.isdigit():
        numeros += 1
    elif c in string.punctuation:
        simbolos += 1
    if 1 <= i <= numero_caracteres - 2 and (c.isdigit() or c in string.punctuation):
        meio += 1

pontuacao = (numero_caracteres * 4) + ((numero_caracteres - maiusculas) * 2) + \
            ((numero_caracteres - minusculas) * 2) + (numeros * 4) + \
            (simbolos * 6) + (meio * 2)

regras = 0
if numero_caracteres >= 8:
    regras += 1
if maiusculas > 0:
    regras += 1
if minusculas > 0:
    regras += 1
if numeros > 0:
    regras += 1
if simbolos > 0:
    regras += 1

pontuacao += (regras * 2)

if senha.isalpha():
    pontuacao -= numero_caracteres
if senha.isdigit():
    pontuacao -= numeros

repetidos = 0
for c in set(senha.lower()):
    if senha.lower().count(c) > 1:
        repetidos += senha.lower().count(c) - 1
pontuacao -= repetidos

repeticao_maiusculas = 0
repeticao_minusculas = 0
repeticao_numeros = 0

for i in range(1, numero_caracteres):
    if senha[i].isupper() and senha[i - 1].isupper():
        repeticao_maiusculas += 1
    if senha[i].islower() and senha[i - 1].islower():
        repeticao_minusculas += 1
    if senha[i].isdigit() and senha[i - 1].isdigit():
        repeticao_numeros += 1

pontuacao -= (repeticao_maiusculas * 2 + repeticao_minusculas * 2 + repeticao_numeros * 2)

repeticao_maiusculas = 0
repeticao_numeros = 0

for i in range(numero_caracteres - 2):

    if (ord(senha[i].lower()) + 1 == ord(senha[i + 1].lower())) and (ord(senha[i + 1].lower()) + 1 == ord(senha[i + 2].lower())):
        repeticao_maiusculas += 1

    if senha[i].isdigit() and senha[i + 1].isdigit() and senha[i + 2].isdigit():
        if int(senha[i]) + 1 == int(senha[i + 1]) and int(senha[i + 1]) + 1 == int(senha[i + 2]):
            repeticao_numeros += 1

pontuacao -= (repeticao_maiusculas * 2 + repeticao_numeros * 2)


if pontuacao < 20:
    classificacao = "Muito fraca"
elif pontuacao < 40:
    classificacao = "Fraca"
elif pontuacao < 60:
    classificacao = "Boa"
elif pontuacao < 80:
    classificacao = "Forte"
else:
    classificacao = "Muito Forte"


print(f"Sua senha tem uma pontuação de {pontuacao}. Classificação: {classificacao}")