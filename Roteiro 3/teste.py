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

print(paraiba.ha_ciclo())
print(paraiba.conexo())
print(paraiba.caminho(3))
unittest.main()
