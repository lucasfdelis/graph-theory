from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations
from copy import deepcopy

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        N = self.N
        lista = ['-'.join(x) for x in combinations(N, 2)]
        for a in self.A:
            b = f"{self.A[a].getV1()}-{self.A[a].getV2()}"
            if (b in lista):
                lista.remove(b)
            b = f"{self.A[a].getV2()}-{self.A[a].getV1()}"
            if (b in lista):
                lista.remove(b)
        return set(lista)

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if self.existeVertice(V) == False:
            raise VerticeInvalidoException
        grauV = 0
        for a in self.A:
            if V == self.A[a].getV1():
                grauV += 1
            if V == self.A[a].getV2():
                grauV += 1
        return grauV

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.A:
            count = -1
            for b in self.A:
                if (self.A[a].getV1() == self.A[b].getV1() and self.A[a].getV2() == self.A[b].getV2()) or \
                        (self.A[a].getV1() == self.A[b].getV2() and self.A[a].getV2() == self.A[b].getV1()):
                    count += 1
                    if count >= 1:
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if self.existeVertice(V) == False:
            raise VerticeInvalidoException
        listaRotulos = []
        for a in self.A:
            if V == self.A[a].getV1() or V == self.A[a].getV2():
                listaRotulos.append(self.A[a].getRotulo())
        return set(listaRotulos)

    def arestas_sobre_vertice_2(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if self.existeVertice(V) == False:
            raise VerticeInvalidoException
        listaRotulos = []
        for a in self.A:
            if V == self.A[a].getV1() or V == self.A[a].getV2():
                listaRotulos.append(self.A[a].getRotulo())
        return listaRotulos

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_paralelas() == True or self.ha_laco() == True:
            return False
        grauu = len(self.N) - 1
        for n in self.N:
            if self.grau(n) != grauu:
                return False
        vetorV = []
        for a in self.A:
            v1 = self.A[a].getV1()
            v2 = self.A[a].getV2()
            if v1 not in vetorV:
                vetorV.append(v1)
            if v2 not in vetorV:
                vetorV.append(v2)
        vet = len(vetorV)
        for i in range(vet):
            if self.grau(vetorV[i]) != vet - 1:
                return False
        return True

    # ROTEIRO II - DFS (profundidade) e BFS (largura)

    def dfs(self, v):
        '''
        Percorre o grafo com a finalidade de gerar um novo grafo através da busca por profundidade (DFS).
        :param v: O vértice passado como raiz, inicio da busca.
        :return: Um objeto do tipo MeuGrafo(), resultante da busca por profundidade.
        '''

        vertices = deepcopy(self.N)
        arvore_dfs = MeuGrafo(vertices)
        visitados = []
        self.dfs_rec(v, arvore_dfs, visitados)
        return arvore_dfs

    def dfs_rec(self, v, arvore, visitados):
        '''
        Função recursiva para auxílio da função dfs().
        :param v: O vértice passado como raiz, inicio da busca.
        :param arvore: Grafo (DFS) que está em construção.
        :param visitados: Vértices que já foram visitados pela busca.
        '''
        arestas = self.arestas_sobre_vertice_2(v)
        visitados.append(v)
        for i in arestas:
            outro_vertice = self.outro_vertice_adj(i, v)
            if outro_vertice not in visitados:
                arvore.adicionaAresta(i, v, outro_vertice)
                self.dfs_rec(outro_vertice, arvore, visitados)

    def bfs(self, v):
        '''
        Percorre o grafo com a finalidade de gerar um novo grafo através da busca por largura (BFS).
        :param v: O vértice passado como raiz, inicio da busca.
        :return: Um objeto do tipo MeuGrafo(), resultante da busca por largura.
        '''

        vertices = deepcopy(self.N)
        arvore_bfs = MeuGrafo(vertices)
        visitados = []
        pais = [v]
        self.bfs_rec(arvore_bfs, pais, visitados)
        return arvore_bfs

    def bfs_rec(self, arvore, pais, visitados):
        '''
        Função recursiva para auxílio da função bfs().
        :param v: O vértice passado como raiz, inicio da busca.
        :param arvore: Grafo (BFS) que está em construção.
        :param pais: lista contendo a os vértices de mesmo nível,
         ou seja, os vértices do nivel anterior aos que serão analisados.
        :param visitados: Vértices que já foram visitados pela busca.
        '''
        if pais == []:
            return
        nova = []
        for k in pais:
            arestas = self.arestas_sobre_vertice_2(k)
            visitados.append(k)
            for i in arestas:
                outro_vertice = self.outro_vertice_adj(i, k)
                if outro_vertice not in visitados:
                    nova.append(outro_vertice)
                    visitados.append(outro_vertice)
                    arvore.adicionaAresta(i, k, outro_vertice)

        self.bfs_rec(arvore, nova, visitados)

    def outro_vertice_adj(self, i, v_i):
        '''
        Função que busca os vértices adjacentes.
        :param i: aresta do vértice a ser analisado.
        :param v_i: vértice passado inicialmente, para que a função retorne seu adjacente.
        :return: retorna o vértice adjacente encontrado.
        '''
        if v_i == self.A[i].getV1():
            return self.A[i].getV2()
        else:
            return self.A[i].getV1()