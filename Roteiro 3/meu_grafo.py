from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations, permutations
from copy import deepcopy
import sys, io

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
    
    def dfs(self, V): 
        '''
        Cria um grafo que contém as arestas do dfs
        :param V: O vértice raiz que inicia a busca
        :return: Um grafo DFS.
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(V not in self.N):
            raise(VerticeInvalidoException)

        def dfs_rec(V, visitado):

            visitado.append(V)
            if(self.eh_inicio == False):
                dfs.adicionaAresta(self.aresta[2], self.aresta[0], self.aresta[1])
            self.eh_inicio = False

            for i in range(len(self.lista_vertices)):
                if (V in self.lista_vertices[i]):
                    self.aresta = self.lista_vertices[i]
                    aresta2 = [self.aresta[0],self.aresta[1]]
                    for vizinho in aresta2: 
                        if vizinho not in visitado:
                            dfs_rec(vizinho, visitado)

        

        vertices = deepcopy(self.N)
        dfs = MeuGrafo(vertices)
        visitado = []

        self.lista_vertices = []
        self.eh_inicio = True

        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])
        
        dfs_rec(V, visitado)
        return dfs

    def bfs(self, V): 
        '''
        Cria um grafo que contém as arestas do bfs
        :param V: O vértice raiz que inicia a busca
        :return: Um grafo BFS.
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(V not in self.N):
            raise(VerticeInvalidoException)
            
        vertices = deepcopy(self.N)
        bfs = MeuGrafo(vertices)
        visitado = [V]

        self.lista_vertices = []
        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        fila = []
        rotulos = []
        fila.append(V)

        for a in self.A:
                rotulos.append(self.A[a].getRotulo())
        
        while fila:
            s = fila.pop(0)

            for i in range(len(self.lista_vertices)):
                if(s in self.lista_vertices[i]):
                    aresta = self.lista_vertices[i]
                    aresta2 = [aresta[0],aresta[1]]

                    for i in aresta2:
                        if i not in visitado:
                            bfs.adicionaAresta(aresta[2], aresta[0], aresta[1])
                            fila.append(i)
                            fila = list(dict.fromkeys(fila))
                            visitado.append(i)
        return bfs

    def conexo(self):
        visitados = []
        vertices = self.N
        vertices_percorridos = self.dfs(vertices[0])
        for i in vertices_percorridos.A:
            if(vertices_percorridos.A[i].getV1() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV1())
            if(vertices_percorridos.A[i].getV2() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV2())
        if(len(self.N) == len(visitados)):
            return True
        return False

    def __caminho_print(self, s, d):

        self.visited =[]
        self.path = []
        val = []
        aresta = ''
        self.lista_vertices = []
        self.eh_inicio = True

        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        def __caminho_print_rec(u, d, aresta):

            self.visited.append(u)
            if(self.eh_inicio == False):
                self.path.append(aresta)
            self.eh_inicio = False
            self.path.append(u)
         
            if(u == d):
                print(self.path)
            else:
                for i in range(len(self.lista_vertices)):
                    if (u in self.lista_vertices[i]):
                        self.aresta = self.lista_vertices[i]
                        aresta2 = [self.aresta[0],self.aresta[1]]
                        for i in aresta2:
                            if i not in self.visited:
                                aresta = self.aresta[2]
                                __caminho_print_rec(i, d, aresta)
                try:
                    self.path.remove(u)
                    self.path.remove(aresta)
                except:
                    pass
        
        sys.stdout = io.StringIO()
        __caminho_print_rec(s, d, aresta)
        val = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        val = eval(val)
        return val
    
    def caminho(self,n):
        N = self.N
        lista = [''.join(x) for x in permutations(N, 2)]
        for i in lista:
            path = self.__caminho_print(i[0],i[1])
            if len(path) == n * 2 + 1:
                return path