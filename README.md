# AlgoritmoVizinhoMaisProximo

O algoritmo Vizinho Mais Próximo (Nearest Neighbour) é muito utilizado em aprendizado de máquina para classificar um dado input.
Um dos exemplos mais clássicos dele é o de sistemas de recomendação de filmes.

Ele consiste em: dado um banco de dados com usuários que deram notas para um conjunto de filmes, o algoritmo cálcula a distância euclidiana entre o usuário input e os usuários do
banco de dados, onde as notas dos filmes são as coordenadas dos usuários.

Nesse caso, que estou tentando prever as notas dos filmes que o input não viu, para cada não filme não visto, é retornado a média das notas dos 3 vizinhos mais próximos para dado
filme.

Esse exercício, eu retirei do canal The Coding Train:
Parte 1 - www.youtube.com/watch?v=N8Fabn1om2k
Parte 2 - www.youtube.com/watch?v=Lo89NLmSgl0
Parte 3 - https://www.youtube.com/watch?v=aMtckmWAzDg

- Lucas Duez
