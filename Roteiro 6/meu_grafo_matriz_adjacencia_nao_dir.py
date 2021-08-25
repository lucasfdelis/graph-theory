from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista = []
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if(i < j and len(self.M[i][j])==0):
                    lista.append(f'{self.N[i]}-{self.N[j]}')
        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.N)):
            if(len(self.M[i][i])>0):
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(V not in self.N):
            raise(VerticeInvalidoException)
        indexV = self.N.index(V)
        grau = 0
        for j in range(indexV, len(self.M)):
            if(indexV == j):
                grau = grau+(len(self.M[indexV][j]))*2
            else:
                grau = grau+(len(self.M[indexV][j]))
        
        for j in range(indexV):
            grau = grau+(len(self.M[j][indexV]))
        return grau



    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (len(self.M[i][j])>1):
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(V not in self.N):
            raise(VerticeInvalidoException)
        lista = []
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (len(self.M[i][j])>0):
                    for a in (self.M[i][j]):
                        if(self.N[i] == V and a!='-'):
                            lista.append(a)
                        if(self.N[j] == V and a!='-'):
                            lista.append(a)
        return lista


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if(self.ha_laco()):
            return False
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (i < j and len(self.M[i][j])==0):
                    return False
        return True

    def warshall(self):
        E  = deepcopy(self)
        tam=len(self.N)

        for i in range(tam):
            for j in range(tam):
                if E.M[j][i] == 1:
                    for k in range(tam):
                        E.M[j][k]=max(E.M[j][k],E.M[i][k])

        return E
