from medirDistanciaEuclidiana import *

def preverNotas(dictFilmesInput):
    dictTodasDistancias = distanciaEntreVizinhos(dictFilmesInput)
    arrayNomesProximos = vizinhosProximos(3, dictTodasDistancias)

    dictPessoasProximas = {}

    dictNotasPrevistas = {}

    for pessoa in arrayNomesProximos:
        dictPessoasProximas.update({pessoa:dictPessoas.get(pessoa)})

    for filme in arrayFilmes:
        arrayNotasFilmes = []
        if not dictFilmesInput.get(filme):
            for pessoa in dictPessoasProximas:
                if dictPessoasProximas.get(pessoa).get(filme):
                    notaDaPessoa = dictPessoasProximas.get(pessoa).get(filme)
                    arrayNotasFilmes.append(notaDaPessoa)

            mediaNota = mediaDeArray(arrayNotasFilmes)

            dictNotasPrevistas.update({filme : mediaNota})

    return dictNotasPrevistas


def mediaDeArray(array):
    soma = 0

    for valor in array:
        soma += valor

    return soma/len(array)
