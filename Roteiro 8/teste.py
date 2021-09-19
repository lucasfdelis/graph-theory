import unittest

from meu_grafo import MeuGrafo

paraiba = MeuGrafo(['0','1','2','3','4','5','6','7','8'])
paraiba.adicionaAresta("a1", '0','1',4)
paraiba.adicionaAresta("a2", '1','2',8)
paraiba.adicionaAresta("a3", '2','3',7)
paraiba.adicionaAresta("a4", '3','4',9)
paraiba.adicionaAresta("a5", '4','5',10)
paraiba.adicionaAresta("a6", '5','6',2)
paraiba.adicionaAresta("a7", '6','7',1)
paraiba.adicionaAresta("a8", '7','0',8)
paraiba.adicionaAresta("a9", '7','1',11)
paraiba.adicionaAresta("a10", '7','8',7)
paraiba.adicionaAresta("a11", '8','6',6)
paraiba.adicionaAresta("a12", '8','2',2)
paraiba.adicionaAresta("a13", '2','5',4)
paraiba.adicionaAresta("a14", '5','3',14)
print(paraiba.Kruskall_modificado())
