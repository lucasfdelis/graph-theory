import unittest
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from meu_grafo import MeuGrafo


g_c = MeuGrafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('a1','J','C')
g_c.adicionaAresta('a2', 'J', 'E')
g_c.adicionaAresta('a3', 'J', 'P')
g_c.adicionaAresta('a4', 'E', 'C')
g_c.adicionaAresta('a5', 'P', 'C')
g_c.adicionaAresta('a6', 'P', 'E')

# print(type(a))
# # rint(g_p_sem_paralelas.caminho(4))
# # a = g_p_sem_paralelas.conexo()
print(g_c.caminho(1))
print(g_c.caminho(2))
print(g_c.caminho(3))
print(g_c.caminho(4))
print(g_c.caminho(5))

unittest.main()
