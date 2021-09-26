from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def topologicalSort(self):
        """
        Algoritmo de Kahn para ordenação topológica.
        :return: Vértices do grafo analisado ordenados topologicamente.
        """

        in_degree = [0]*(len(self.N))

        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if(len(self.M[i][j])>0):
                    in_degree[self.N.index(self.N[j])] += 1

        queue = []
        for i in range(len(self.N)):
            if in_degree[i] == 0:
                queue.append(self.N[i])
        
        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if(self.N[i]==u):
                        in_degree[self.N.index(self.N[j])] -= 1
                        if( in_degree[self.N.index(self.N[j])] == 0):
                            queue.append(self.N[j])
            
            cnt = cnt+1
        
        return top_order
                    
                        

