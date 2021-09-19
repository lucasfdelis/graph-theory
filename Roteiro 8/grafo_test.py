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

    def menor_peso_da_aresta(self):
        dic = {}
        copia = deepcopy(self.M)
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if (len(self.M[i][j]) != 0) and (self.M[i][j]!= self.SEPARADOR_ARESTA):
                    aresta = '{}{}{}'.format(self.N[i],self.SEPARADOR_ARESTA,self.N[j])
                    dic[aresta]=min(self.M[i][j])

        return dic

    sets = {}

    def criar_floresta(self,v):
        self.sets[v]=[v]

    def procura(self,v):
        for i,x in self.sets.items():
            if v in x:
                return i
        return None


    def uniao(self,v1,v2):
        vertice1 = self.procura(v1)
        vertice2 = self.procura(v2)
        self.sets[vertice1]=self.sets[vertice1]+self.sets[vertice2]
        del self.sets[vertice2]


    def Kruskall_modificado(self):
        """
        Algoritmo original de Kruskal para encontrar a Árvore de Extensão Mínima (Minimum Spanning Tree) do Grafo.
        :return: Um Grafo/Árvore representando a Minimum Spanning Tree.
        """
        #Cria o Grafo/Árvore
        arvore_minima = MeuGrafo()
        teste = 1
        for i in self.N:
            self.criar_floresta(i)

        arvore = []
        dicionarioArestasComPesos = self.menor_peso_da_aresta()
        arestas_menor_peso = self.menor_peso_da_aresta()
        arestas_menor_peso = arestas_menor_peso.values()
        vertices_não_presentes_na_arvore = self.N
        if self.eh_conexo():
            for a in arestas_menor_peso:
                for i in dicionarioArestasComPesos:
                    if dicionarioArestasComPesos[i]== a:
                        if self.procura(i[0]) != self.procura(i[2]):
                            v1=i[0]
                            v2=i[2]
                            arvore.append(i)
                            arvore.append(v1)
                            arvore.append(v2)
                            existe_vertice1 = arvore_minima.existeVertice(v1)
                            existe_vertice2 = arvore_minima.existeVertice(v2)
                            if not existe_vertice1:
                                arvore_minima.adicionaVertice(v1)
                            if not existe_vertice2:
                                arvore_minima.adicionaVertice(v2)
                            if not (existe_vertice1 and existe_vertice2) or (existe_vertice1 and existe_vertice2):
                                arvore_minima.adicionaAresta(str(teste),i,a)
                                teste = teste+1
                            self.uniao(v1,v2)
            return arvore_minima


    def procurar_na_arvore(self,vertice,lista=[]):
        if vertice not in lista:
            return True
        else:
            return False



    def dicionario_peso_aresta(self):
        dic = {}
        copia = deepcopy(self.M)
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if (len(self.M[i][j]) != 0) and (self.M[i][j] != self.SEPARADOR_ARESTA):
                    aresta = '{}{}{}'.format(self.N[i], self.SEPARADOR_ARESTA, self.N[j])
                    dic[aresta] = self.M[i][j]

        return dic

    def vertices_adjacentes(self, v):
        lista_vertices_adjacentes = []
        posição = self.N.index(v)
        for i in range(len(self.M)):
            if i < posição:
                if self.M[i][posição]:
                    lista_vertices_adjacentes.append(self.N[i])
            elif i == posição:
                for j in range(posição, len(self.M[i])):
                    if self.M[i][j]:
                        lista_vertices_adjacentes.append(self.N[j])
            else:
                break
        return lista_vertices_adjacentes

    def criar_aresta(self,v1,v2):
        aresta = "{}{}{}".format(v1,self.SEPARADOR_ARESTA,v2)
        return aresta


    def PrimModificado(self):
        from math import inf
        teste = 1
        vertices = deepcopy(self.N)
        arestas = []
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if (len(self.M[i][j]) != 0) and (self.M[i][j] != self.SEPARADOR_ARESTA):
                    aresta1 = '{}{}{}'.format(self.N[i], self.SEPARADOR_ARESTA, self.N[j])
                    arestas.append(aresta1)
        dic_peso = self.dicionario_peso_aresta()
        Jet = {}
        P = {}
        guarda_peso = inf
        guarda_aresta =''
        arvore = MeuGrafo()
        for vertice in vertices:
            Jet[vertice] = inf
            P[vertice] = None

        for aresta in arestas:
            listap= dic_peso[aresta]
            peso = listap[0]
            if peso< guarda_peso:
                guarda_peso = peso
                guarda_aresta = aresta
                v1,v2 = aresta.split(self.SEPARADOR_ARESTA)
        Jet[v1] = 0
        lista_prioridade = deepcopy(self.N)
        while(len(lista_prioridade)!=0):
            menor_peso = inf
            vertice_menor_peso = ''
            for v in lista_prioridade:
                if isinstance(Jet[v],list)==True:#problema é aqui
                    jet = Jet[v][0]
                    if jet<menor_peso:
                        pesolista = Jet[v]
                        menor_peso = pesolista[0]
                        vertice_menor_peso= v
                else:
                    if Jet[v] < menor_peso:
                        menor_peso = Jet[v]
                        vertice_menor_peso = v
            x = vertice_menor_peso

            lista_prioridade.pop(lista_prioridade.index(vertice_menor_peso))
            lista_vertices_adjacente = self.vertices_adjacentes(x)
            for vertice_adjacente in lista_vertices_adjacente:
                aresta_y = x+"-"+vertice_adjacente
                if aresta_y not in arestas:
                    aresta_y = vertice_adjacente+'-'+x
                pesoy = dic_peso[aresta_y][0]
                jety = Jet[vertice_adjacente]
                if isinstance(jety,list)==True:
                    if vertice_adjacente in lista_prioridade and pesoy<jety[0]:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente]= dic_peso[aresta_y]
                else:
                    if vertice_adjacente in lista_prioridade and pesoy<jety:
                        P[vertice_adjacente] = x
                        Jet[vertice_adjacente]= dic_peso[aresta_y]
        for v in vertices:
            arvore.adicionaVertice(v)
        lista_final = []
        for a,i in P.items():
            if i:
                lista_final.append(self.criar_aresta(i,a))
        dic_menor_peso = self.menor_peso_da_aresta()
        for i in lista_final:
            if i in dic_menor_peso:
                arvore.adicionaAresta(str(teste),i,dic_menor_peso[i])
                teste = teste+1

        return arvore
    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                if self.M[l][c] =='-':
                    grafo_str += '-' + ' '
                else:
                    grafo_str += str(len(self.M[l][c])) + ' ' #recebe o tamanho de self.M[l][c] pois se tiverem dois pesos, então haverá duas arestas, se não tiver nenhum, n tem aresta e o len==0
            grafo_str += '\n'

        return grafo_str
