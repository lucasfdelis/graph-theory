from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def __warshallmatrix(self):
        E = []
        tam = len(self.N)
        for i in range(tam):
            M = []
            for j in range(tam):
                M.append(0)
            E.append(M)
        for i in range(tam):
            for j in range(tam):
                if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                    E[i][j] = 1
        return E

    def warshall(self):
        """
        Encontra a matriz de alcançabilidade de um grafo usando o algoritmo de Warshall.
        :return: Uma matriz com a alcançabilidade de um grafo (Os alcançáveis são marcados com "1".)
        """
        matriz = self.__warshallmatrix()
        tam=len(self.N)

        for i in range(tam):
            for j in range(tam):
                if(matriz[j][i] == 1):
                    for k in range(tam):
                        matriz[j][k] = max(matriz[j][k],matriz[i][k])
        return matriz
