from preverNotas import *

dictNotas = {}
print('Digite uma nota de 0 a 5 para os filmes a seguir.')
print(' Caso não tenha visto o filme, apenas aperte enter e te darei a nota que você provalvemente dará para os filmes não vistos')
for filme in arrayFilmes:
    notaFilme = input('Digite sua nota para o filme %s: ' %filme)

    if notaFilme:
        dictNotas.update({filme: notaFilme})

resultado = preverNotas(dictNotas)
print(resultado)