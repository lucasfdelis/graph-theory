from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations
from copy import deepcopy
from collections import defaultdict

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
            if(f"{self.A[a].getV1()}-{self.A[a].getV2()}" in lista):
                lista.remove(f"{self.A[a].getV1()}-{self.A[a].getV2()}")
            if(f"{self.A[a].getV2()}-{self.A[a].getV1()}" in lista):
                lista.remove(f"{self.A[a].getV2()}-{self.A[a].getV1()}")
        return lista
        
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if(self.A[a].getV1() == self.A[a].getV2()):
                return True
        return False
        
    def grau(self, V):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(V not in self.N):
            raise(VerticeInvalidoException)
        grau = 0
        for a in self.A:
            if(self.A[a].getV1() == V):
                grau = grau+1
            if(self.A[a].getV2() == V):
                grau = grau+1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.A:
            aresta = [self.A[a].getV1(),self.A[a].getV2()]
            for b in self.A:
                if(b!=a):
                    aresta2 = [self.A[b].getV1(),self.A[b].getV2()]
                    if(sorted(aresta) == sorted(aresta2)):
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
        for a in self.A:
            if(self.A[a].getV1() == V):
                lista.append(self.A[a].getRotulo())
            if(self.A[a].getV2() == V):
                lista.append(self.A[a].getRotulo())    
        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        n = len(self.N)
        if(self.ha_laco()):
            return False
        else:
            if(n*(n-1)/2 == len(self.A)):
                return True
            return False
    
    def vertices_adjacentes(self):
        dicionario = self.N
        conexoes = defaultdict(list)
        for a in self.A:
            conexoes[self.A[a].getV1()].append(self.A[a].getV2())
            conexoes[self.A[a].getV2()].append(self.A[a].getV1())
        return conexoes

    def dfs(self, V): 
        '''
        Busca o grafo de profundidade a partir de um vértice V.
        :param V: O vértice raiz por onde começará a busca.
        :return: Um grafo com todos os vértices de um grafo e as arestas necessárias para formar seu grafo de profundidade.
        '''
        def dfs_rec(V, visitado):
            visitado.append(V)
            if(self.cont != 0):
                dfs.adicionaAresta(self.aresta[2], self.aresta[0], self.aresta[1])
            self.cont = 1
            for i in range(len(self.lista_vertices)):
                if (V in self.lista_vertices[i]):
                    self.aresta = self.lista_vertices[i]
                    aresta2 = [self.aresta[0],self.aresta[1]]
                    for neighbour in aresta2:
                        if neighbour not in visitado:
                            dfs_rec(neighbour, visitado)
        self.cont = 0
        vertices = deepcopy(self.N)
        dfs = MeuGrafo(vertices)
        self.lista_vertices = []
        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])
        visitado = []
        dfs_rec(V, visitado)
        return dfs

    def bfs(self, start):
        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])
        grafo = self.vertices_adjacentes()
        print(grafo)
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]
 
        # keep looping until there are nodes still to be checked
        while queue:
            # pop shallowest node (first node) from queue
            node = queue.pop(0)
            if node not in explored:
                print(node)
                # add node to list of checked nodes
                explored.append(node)
                neighbours = grafo[node]
 
                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored
            