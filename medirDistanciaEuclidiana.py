import json

arquivo = open('dadosFilmes')
dados = json.load(arquivo)

arrayFilmes = dados.get('filmes')
dictPessoas = dados.get('pessoas')

def distanciaEntreVizinhos(dictNotasInput): #retorna um dicionario com a distancia entre o input e cada pessoa
    dictDistancias = {}

    for pessoa in dictPessoas:
        dictFilmesdaPessoa = dictPessoas.get(pessoa)
        soma = 0

        for filme in arrayFilmes:
            nota1 = dictFilmesdaPessoa.get(filme)
            nota2 = dictNotasInput.get(filme)

            if nota1 and nota2:
                soma += (float(nota1) + float(nota2)) ** 2


        distancia = round(soma**(0.5),3)

        dictDistancias.update({pessoa: distancia})

    return dictDistancias


def vizinhosProximos(numVizinhosProximos, dictInput): #dicionário  ou array com as 5 pessoas mais próximas em ordem crescente
    arrayValores = arrayValoresDict(dictInput)
    arrayValores.sort()
    arrayChaves = arrayChavesDict(dictInput)

    arrayValoresProximos = []

    for i in range(numVizinhosProximos): #Teremos uma array com as 5 distancias mais próximas
        arrayValoresProximos.append(arrayValores[i])

    arrayNomesProximos = []
    for i in range(len(arrayValoresProximos)): #teremos uma array com os 5 nomes mais próximos
        for j in range(len(arrayChaves)):
            if dictInput.get(arrayChaves[j]) == arrayValoresProximos[i]:
                arrayNomesProximos.append(arrayChaves[j])

    return arrayNomesProximos

def arrayChavesDict(dict):
    array = []

    for chave in dict:
        array.append(chave)

    return array

def arrayValoresDict(dict):
    array = []
    for item in dict:
        array.append(dict.get(item))

    return array