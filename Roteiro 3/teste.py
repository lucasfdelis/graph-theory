import unittest
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from meu_grafo import MeuGrafo

g_nd = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
# g_nd.adicionaAresta('a1', 'A', 'B')
g_nd.adicionaAresta('a2', 'A', 'G')
g_nd.adicionaAresta('a3', 'A', 'J')
g_nd.adicionaAresta('a4', 'G', 'K')
g_nd.adicionaAresta('a5', 'J', 'K')
g_nd.adicionaAresta('a6', 'G', 'J')
g_nd.adicionaAresta('a7', 'I', 'J')
g_nd.adicionaAresta('a8', 'G', 'I')
g_nd.adicionaAresta('a9', 'G', 'H')
g_nd.adicionaAresta('a10', 'F', 'H')
g_nd.adicionaAresta('a11', 'B', 'F')
g_nd.adicionaAresta('a12', 'B', 'G')
g_nd.adicionaAresta('a13', 'B', 'C')
g_nd.adicionaAresta('a14', 'C', 'D')
g_nd.adicionaAresta('a15', 'D', 'E')
g_nd.adicionaAresta('a16', 'B', 'D')
g_nd.adicionaAresta('a17', 'B', 'E')
print(g_nd.caminho_dois_vertices('A','B'))
#unittest.main()
