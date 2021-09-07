from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices(self,v):
        lista=[]
        n=0
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if len(self.M[i][j]) > 0 and self.M[i][j]!=self.SEPARADOR_ARESTA:
                    n=1
                    if ( (n >= 1) and (self.N[i] == v) ):
                        for c in range(n):
                            if self.N[i]==v:
                                if self.N[j] not in lista:
                                    lista.append(self.N[j])
        return lista

    def djikstra(self,u,v):
        import math

        vertices=self.N
        lista_aresta=[]
        lista_menor_caminho=[]

        beta={}
        pi={}

        nao_visitados=[]

        for vertice in vertices:
            beta[vertice]= math.inf
            pi[vertice]='0'
            nao_visitados.append(vertice)
        beta[u]=0
        nao_visitados.remove(u)
        R = 0 
        w=u
        while w!=v:
            lista_aresta = self.vertices_partindo_de(w)
            print(w,lista_aresta)
            for r in lista_aresta:
                if r in nao_visitados:
                    if beta[r]>(beta[w]+1):
                        beta[r]=(beta[w]+1)
                        pi[r]=w

            menor_beta= math.inf

            for r in nao_visitados:
                if beta[r]<menor_beta:
                    menor_beta=beta[r]
                    r_menor_beta=r

            if menor_beta == math.inf:
                return False

            R = r_menor_beta
            nao_visitados.remove(R)
            w=R

        lista_menor_caminho.append(v)
        while v!=u:
            lista_menor_caminho.append(pi[v])
            v=pi[v]
        lista_menor_caminho.reverse()
        return lista_menor_caminho

    def djikstra_modificada(self,u,v,c_inicial,c_max,pontos_recarga=[]):
        import math

        vertices=self.N
        lista_aresta=[]
        lista_menor_caminho=[]

        beta={}
        pi={}
        carga_v={}

        nao_visitados=[] 

        for vertice in vertices:
            beta[vertice]= math.inf
            pi[vertice]='0'
            carga_v[vertice]=math.inf
            nao_visitados.append(vertice)
        beta[u]=0

        if u in pontos_recarga:
            carga_v[u]=c_max
        else:
            carga_v[u]=c_inicial

        nao_visitados.remove(u)
        R=0
        w=u
        while w!=v:
            lista_aresta = self.vertices(w)
            for r in lista_aresta:

                if r in nao_visitados:
                    if beta[r]>=(beta[w]+1):
                        beta[r]=(beta[w]+1)
                        pi[r]=w
                        if r in pontos_recarga:
                            carga_v[r]=c_max
                        else:
                            carga_v[r]=carga_v[w]-1

            menor_beta= math.inf

            for i in nao_visitados:

                if carga_v[i]==0 and i!=u:
                    beta[i] = math.inf

            for r in nao_visitados:
                if beta[r]<menor_beta:
                    menor_beta=beta[r]
                    r_menor_beta=r

            if menor_beta == math.inf:
                return False

            R = r_menor_beta
            nao_visitados.remove(R)
            w=R

        lista_menor_caminho.append(v)
        while v!=u:
            lista_menor_caminho.append(pi[v])
            v=pi[v]
        lista_menor_caminho.reverse()
        return lista_menor_caminho