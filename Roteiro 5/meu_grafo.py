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

    def ha_ciclo(self):
        '''
        Usando DFS, essa função percorre o grafo procurando por um ciclo.
        :return: uma lista no formato [v1, a1, v2, a2, v3, a3, …, an, v1] 
        (onde vx são vértices e ax são arestas) indicando os vértices e arestas que formam o ciclo.
        Se não existir nenhum ciclo no grafo, ele retorna 'False'.
        '''
        visitado = []
        for V in self.N:
            visitado.append(V)
            arestas_paralelas = []
            if(len(self.arestas_sobre_vertice(V))>1):
                for aresta in self.arestas_sobre_vertice(V):
                    if(self.A[aresta].getV1() == V):
                        arestas_paralelas.append(self.A[aresta].getV2())
                    if(self.A[aresta].getV2() == V):
                        arestas_paralelas.append(self.A[aresta].getV1())
            arestas_paralelas_2 = []
            for i in arestas_paralelas:
                if(len(self.arestas_sobre_vertice(i))>1):
                    arestas_paralelas_2.append(i)
            if(len(arestas_paralelas_2)>1):
             for i in self.A:
                try:
                 if([V,arestas_paralelas_2[0]] == [self.A[i].getV1(),self.A[i].getV2()]):
                    grafo = deepcopy(self)
                    grafo.removeAresta(i)
                    ciclo = grafo.caminho_dois_vertices(self.A[i].getV1(),self.A[i].getV2())
                    ciclo.append(i)
                    ciclo.append(self.A[i].getV1())
                    return ciclo
                 if([V,arestas_paralelas_2[0]] == [self.A[i].getV2(),self.A[i].getV1()]):
                    grafo = deepcopy(self)
                    grafo.removeAresta(i)
                    ciclo = grafo.caminho_dois_vertices(self.A[i].getV2(),self.A[i].getV1())
                    ciclo.append(i)
                    ciclo.append(self.A[i].getV2())
                    return ciclo
                except:
                    pass
        return False

    def caminho_dois_vertices(self, s, d):
        '''
        Função auxiliar que verifica se há um caminho entre 2 vértices.
        '''
        self.visited =[]
        self.path = []
        val = []
        aresta = ''
        self.lista_vertices = []

        for i in self.A:
            self.lista_vertices.append([self.A[i].getV1(), self.A[i].getV2(), i])

        def caminho_dois_vertices_rec(u, d, aresta):

            self.visited.append(u)
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
                                caminho_dois_vertices_rec(i, d, aresta)

                self.path.remove(u)
        
        sys.stdout = io.StringIO()
        caminho_dois_vertices_rec(s, d, aresta)
        val = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__
        val = eval(val)
        caminho_lista = []
        for i in range(len(val)-1):
            caminho_lista.append(val[i])
            for a in self.A:
                if([self.A[a].getV1(),self.A[a].getV2()] == [val[i],val[i+1]]):
                    caminho_lista.append(a)
                if([self.A[a].getV2(),self.A[a].getV1()] == [val[i],val[i+1]]):
                    caminho_lista.append(a)
        caminho_lista.append(val[-1])
        return caminho_lista

    def caminho(self,n):
        '''
        Percorre o grafo para encontrar um caminho de comprimento n
        :param n: O tamanho do caminho a ser buscado
        :return: Uma lista no formato [v1, a1, v2, a2, v3, a3, ...] onde vx são vértices e ax são arestas
        Se não existir nenhum caminho com o tamanho dado, ele retorna 'None'
        '''
        N = self.N
        lista = [''.join(x) for x in permutations(N, 2)]
        for i in lista:
            path = self.caminho_dois_vertices(i[0],i[1])
            if len(path) == n * 2 + 1:
                return path

    def conexo(self):
        '''
        Função para analisar se o grafo é conexo ou não.
        :return: Um valor booleano que indica se o grafo é conexo.
        '''
        visitados = []
        vertices = self.N
        vertices_percorridos = self.dfs(vertices[0])
        if(len(self.N)==1):
            return True
        for i in vertices_percorridos.A:
            if(vertices_percorridos.A[i].getV1() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV1())
            if(vertices_percorridos.A[i].getV2() not in visitados):
                visitados.append(vertices_percorridos.A[i].getV2())
        if(len(self.N) == len(visitados)):
            return True
        return False

    def vertices_adjacentes(self,v):
        '''
        Provê uma lista de vértices adjacentes a um vértice dado como parametro. A lista terá o seguinte formato: [X,Y,W...]
        Onde X, Z e W são vértices no grafo que tem uma aresta entre o vértice V.
        :return: Uma lista com os pares de vértices adjacentes
        '''
        N = self.N
        lista = []
        for a in self.A:
            if(self.A[a].getV1() == v):
                lista.append(self.A[a].getV2())
            if(self.A[a].getV2() == v):
                lista.append(self.A[a].getV1())           
        return lista    

    def ehEuleriano(self):
        '''
        Verifica se o grafo é euleriano
        :return 0: Se o grafo não tiver nenhuma aresta com grau ímpar
        :return 1: Se o grafo não for euleriano (ter apenas 1 aresta ímpar ou mais de 2)
        :return 2: Se o grafo tiver 2 arestas com grau ímpar
        '''
        if(self.conexo() == False):
            return 1
        else:
            grau = 0
            for i in self.N:
                if(self.grau(i) %2 != 0):
                    grau = grau+1
        if grau == 0:
            return 0
        elif grau == 2:
            return 2
        else:
            return 1

    def __arestaValidaEuler(euler,a):
        '''
        Verifica se uma aresta a pode ser passada como 
        próximo caminho do caminho euleriano
        :return: Um valor booleano que indica se a aresta pode ser o caminho
        '''
        u = euler.A[a].getV1()
        v = euler.A[a].getV2()

        if(euler.vertices_adjacentes(u) == [v]):
            return True
        else:
            contador1 = euler.dfs(u)
            euler.removeAresta(a)
            contador2 = euler.dfs(u)
            euler.adicionaAresta(a,u,v)
            return False if len(contador1.N) > len(contador2.N) else True
                       
    def __exibirEuler(euler,u):
        '''
        Adiciona o caminho euleriano em uma lista, começando do vértice u,
        passado como parametro em exibirCaminho()
        '''
        grafo = []
        for i in euler.A:
            if (u in euler.A[i].getV1() or u in euler.A[i].getV2()):
                grafo = [euler.A[i].getV1(),euler.A[i].getV2()]
                break
        if(grafo == []):
            return 0
        for v in grafo:
            if u!=v:
                if(euler.__arestaValidaEuler(i)):
                    if(len(euler.visitados)>0):
                        euler.visitados.append(i)
                        euler.visitados.append(v)
                    if(len(euler.visitados)==0):
                        euler.visitados.append(u)
                        euler.visitados.append(i)
                        euler.visitados.append(v)
                    euler.removeAresta(i)
                    euler.__exibirEuler(v)
                        
    
    def exibirCaminho(self):
        '''
        A função principal que exibe o caminho euleriano. Ela primeiro verifica
        se o grafo é euleriano. Se ele for, a função chama _exibirEuler() para
        printar o caminho.
        :return: Uma lista com o caminho euleriano
        '''
        
        euler = deepcopy(self)

        euler.visitados = []
        if(euler.ehEuleriano() == 1):
            return 'O grafo não é euleriano.'
        if(euler.ehEuleriano() == 0):
            u = euler.N[0]
        else:
            for i in euler.N:
                if(euler.grau(i) %2 != 0):
                    u = i
                    break
        euler.__exibirEuler(u)
        return euler.visitados            
