import unittest
from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo

paraiba = MeuGrafo(['0','1', '2', '3', '4', '5'])

paraiba.adicionaAresta("a1", "5", "2")
paraiba.adicionaAresta("a2", "5", "0")
paraiba.adicionaAresta("a3", "4", "0")
paraiba.adicionaAresta("a4", "4", "1")
paraiba.adicionaAresta("a5", "2", "3")
paraiba.adicionaAresta("a6", "3", "1")

print(paraiba)
print(paraiba.topologicalSort())

unittest.main()