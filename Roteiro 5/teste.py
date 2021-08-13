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
print(paraiba.ehEuleriano())
print(paraiba.exibirCaminho())

paraiba  = MeuGrafo(['0','1','2','3'])
paraiba.adicionaAresta('a1','0','1')
paraiba.adicionaAresta('a2','0','2')
paraiba.adicionaAresta('a3','1','2')
paraiba.adicionaAresta('a4','2','3')
print(paraiba.ehEuleriano())
print(paraiba.exibirCaminho())

paraiba = MeuGrafo(['0','1','2'])
paraiba.adicionaAresta('a1','0','1')
paraiba.adicionaAresta('a2','1','2')
paraiba.adicionaAresta('a3','2','0')
print(paraiba.ehEuleriano())
print(paraiba.exibirCaminho())

paraiba = MeuGrafo(['0', '1', '2', '3', '4'])
paraiba.adicionaAresta("a1", "1", "0")
paraiba.adicionaAresta("a2", "0", "2")
paraiba.adicionaAresta("a3", "2", "1")
paraiba.adicionaAresta("a4", "0", "3")
paraiba.adicionaAresta("a5", "3", "4")
paraiba.adicionaAresta("a6", "3", "2")
paraiba.adicionaAresta("a7", "3", "1")
paraiba.adicionaAresta("a8", "2", "4")
print(paraiba.ehEuleriano())
print(paraiba.exibirCaminho())

unittest.main()