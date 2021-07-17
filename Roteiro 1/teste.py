import unittest
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

from meu_grafo import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "C", "E")
paraiba.adicionaAresta("a3", "C", "E")
paraiba.adicionaAresta("a4", "C", "P")
paraiba.adicionaAresta("a5", "C", "P")
paraiba.adicionaAresta("a6", "C", "M")
paraiba.adicionaAresta("a7", "C", "T")
paraiba.adicionaAresta("a8", "M", "T")
paraiba.adicionaAresta("a9", "T", "Z")
print('Grafo:')
print(paraiba)
print('')
print('Vértices não adjacentes: ',paraiba.vertices_nao_adjacentes())
print('O grafo tem laço: ',paraiba.ha_laco())
print('Grau do vértice C: ',paraiba.grau('C'))
print('O grafo tem arestas paralelas: ',paraiba.ha_paralelas())
print('Arestas que incidem no vértice C: ',paraiba.arestas_sobre_vertice('C'))
print('O grafo é completo: ',paraiba.eh_completo())

unittest.main()