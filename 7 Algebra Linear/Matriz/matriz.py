# existe duas formas de criar uma matriz
# 1 -  criar uma matriz atrvez de uma lista dentro de outra lista.
matriz_A = [[1,2,3],[4,5,6]] # cada lista é uma linha a mais
# escrevendo a matriz na tela
#print(matriz_A)
# como acessar o elemento(2) que esta na primeira linha segunda coluna?
# lembrando que no python o indice começa no zero
#print(matriz_A[0][1]) # escrevendo o elemento na tela

# 2 - criar apartir de uma biblioteca do python
# numpy biblioteca para trabalhar com matrizes multidimencionais
import numpy as np #  importando e adicionando um alias(apelido) para a biblioteca
matriz_B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz_B) # escrever a matriz na tela
print("_"*9)
print(matriz_B[0][1]) # acessando o elemento (2) que esta na primeira linha segunda coluna
# como fazer uma transposicao de matriz(transformar linha em coluna)
print("_"*9)
print(f" matriz_B = {matriz_B}")
matriz_transposta = matriz_B.transpose()
print(F"matriz_transposta = {matriz_transposta}")

# podemos somar matrizes desde que elas tenham a mesma dimensao
print("_"*9)
print("soma de matrizes")
soma_de_matriz = matriz_B + matriz_B
print(f"soma de matriz = {soma_de_matriz}")

# podemos subtrair matrizes desde que elas tenham a mesma dimensao
print("_"*9)
print("subtracao de matrizes")
subtracao_de_matriz = soma_de_matriz - matriz_transposta
print(f"subtracao de matriz = {subtracao_de_matriz}")

# podemos multiplicar matrizes desde que o numero de linhas da primeira seja
#  o mesmo que o numero de colunas da segunda matriz.
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])
multiplicacao_de_matriz = np.dot(matriz1,matriz2)
print("_"*9)
print(multiplicacao_de_matriz)





