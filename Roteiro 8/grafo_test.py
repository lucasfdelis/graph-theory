import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.paraiba = MeuGrafo(['0','1','2','3','4','5','6','7','8'])
        self.paraiba.adicionaAresta("a1", '0','1',4)
        self.paraiba.adicionaAresta("a2", '1','2',8)
        self.paraiba.adicionaAresta("a3", '2','3',7)
        self.paraiba.adicionaAresta("a4", '3','4',9)
        self.paraiba.adicionaAresta("a5", '4','5',10)
        self.paraiba.adicionaAresta("a6", '5','6',2)
        self.paraiba.adicionaAresta("a7", '6','7',1)
        self.paraiba.adicionaAresta("a8", '7','0',8)
        self.paraiba.adicionaAresta("a9", '7','1',11)
        self.paraiba.adicionaAresta("a10", '7','8',7)
        self.paraiba.adicionaAresta("a11", '8','6',6)
        self.paraiba.adicionaAresta("a12", '8','2',2)
        self.paraiba.adicionaAresta("a13", '2','5',4)
        self.paraiba.adicionaAresta("a14", '5','3',14)
    
    def test_prim(self):
        self.assertEqual(self.paraiba.lista_arestas_prim(),['7-0', '0-1', '2-5', '2-3', '3-4', '5-6', '6-7', '8-2'])
    
    def test_kruskall(self):
        self.assertEqual(self.paraiba.lista_arestas_kruskall(),['6-7', '5-6', '8-2', '0-1', '2-5', '2-3', '1-2', '3-4'])