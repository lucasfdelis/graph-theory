import unittest
from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T'])

paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "C", "E")
paraiba.adicionaAresta("a3", "E", "C")
paraiba.adicionaAresta("a4", "C", "P")
paraiba.adicionaAresta("a5", "P", "C")
paraiba.adicionaAresta("a6", "C", "M")
paraiba.adicionaAresta("a7", "C", "T")
paraiba.adicionaAresta("a8", "M", "T")

print(paraiba)
print(paraiba.warshall())

unittest.main()