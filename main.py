from preverNotas import *

dictNotas = {}
for filme in arrayFilmes:
    notaFilme = input('Digite sua nota para o filme %s: ' %filme)

    if notaFilme:
        dictNotas.update({filme: notaFilme})

resultado = preverNotas(dictNotas)
print(resultado)