import unittest
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from meu_grafo import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "C", "E")
paraiba.adicionaAresta("a3", "C", "E")
paraiba.adicionaAresta("a4", "P", "C")
paraiba.adicionaAresta("a5", "P", "C")
paraiba.adicionaAresta("a6", "T", "C")
paraiba.adicionaAresta("a7", "M", "C")
paraiba.adicionaAresta("a8", "M", "T")
paraiba.adicionaAresta("a9", "T", "Z")
# print(list(paraiba.dfs('J').A))
# print(list(paraiba.dfs('C').A))
print(paraiba.bfs('M'))
# print(paraiba.dfs('J').A)
# print(list(paraiba.dfs('C').A))

    # def bfs(self, V):
    #     visited = []
    #     queue = [V]
    #     vertices = deepcopy(self.N)
    #     bfs = MeuGrafo(vertices)
    #     while queue:
    #         node = queue.pop(0)
    #         if node not in visited:
    #             visited.append(node)     
    #             for edge in self.A:
    #                 # print(self.A[edge].getV1(),self.A[edge].getV2(),node)
    #                 if self.A[edge].getV1() == node:
    #                     queue.append(self.A[edge].getV2())
    #                     try:
    #                         bfs.adicionaAresta(self.A[edge].getRotulo(), self.A[edge].getV1(), self.A[edge].getV2())
    #                     except Exception as e:
    #                         pass
    #                 elif self.A[edge].getV2() == node:
    #                     queue.append(self.A[edge].getV1())
    #                     try:
    #                         bfs.adicionaAresta(self.A[edge].getRotulo(), self.A[edge].getV1(), self.A[edge].getV2())
    #                     except:
    #                         pass
                    
    #     return bfs
            