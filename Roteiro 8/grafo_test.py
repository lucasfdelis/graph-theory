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
    
        self.g_2 = MeuGrafo(['A','B','C','D','S','T'])
        self.g_2.adicionaAresta('a1','A','B',6)
        self.g_2.adicionaAresta('a2','A','B',9)
        self.g_2.adicionaAresta('a3','B','C',4)
        self.g_2.adicionaAresta('a4','C','D',3)
        self.g_2.adicionaAresta('a5','D','B',2)
        self.g_2.adicionaAresta('a6','A','C',3)
        self.g_2.adicionaAresta('a7','C','C',1)
        self.g_2.adicionaAresta('a8','A','S',7)
        self.g_2.adicionaAresta('a9','C','S',8)
        self.g_2.adicionaAresta('a10','B','T',5)
        self.g_2.adicionaAresta('a11','D','T',2)

        self.g_3 = MeuGrafo(['A','B','C','D','E'])
        self.g_3.adicionaAresta('a1','A','B',1)
        self.g_3.adicionaAresta('a2','B','C',3)
        self.g_3.adicionaAresta('a3','C','D',4)
        self.g_3.adicionaAresta('a4','D','E',2)
        self.g_3.adicionaAresta('a5','A','E',5)
        self.g_3.adicionaAresta('a6','D','A',10)
        self.g_3.adicionaAresta('a7','C','A',7)

        self.g_4 = MeuGrafo(['A','B','C','D','S','T'])
        self.g_4.adicionaAresta('a1','A','B',5)
        self.g_4.adicionaAresta('a3','A','D',3)
        self.g_4.adicionaAresta('a4','C','D',2)
        self.g_4.adicionaAresta('a5','D','B',3)
        self.g_4.adicionaAresta('a6','A','C',1)
        self.g_4.adicionaAresta('a8','A','S',9)
        self.g_4.adicionaAresta('a9','C','S',4)
        self.g_4.adicionaAresta('a10','B','T',8)
        self.g_4.adicionaAresta('a11','D','T',7)

    def test_prim(self):
        self.assertEqual(self.paraiba.lista_arestas_prim(),['7-0', '0-1', '2-5', '2-3', '3-4', '5-6', '6-7', '8-2'])
        self.assertEqual(self.g_2.lista_arestas_prim(),['A-C', 'D-B', 'C-D', 'A-S', 'D-T'])
        self.assertEqual(self.g_3.lista_arestas_prim(),['A-B', 'B-C', 'C-D', 'D-E'])
        self.assertEqual(self.g_4.lista_arestas_prim(),['D-B', 'A-C', 'C-D', 'C-S', 'D-T'])

    def test_kruskall(self):
        self.assertEqual(self.paraiba.lista_arestas_kruskall(),['6-7', '5-6', '8-2', '0-1', '2-5', '2-3', '1-2', '3-4'])
        self.assertEqual(self.g_2.lista_arestas_kruskall(),['D-B', 'D-T', 'C-D', 'A-C', 'A-S'])
        self.assertEqual(self.g_3.lista_arestas_kruskall(),['A-B', 'D-E', 'B-C', 'C-D'])
        self.assertEqual(self.g_4.lista_arestas_kruskall(),['A-C', 'C-D', 'D-B', 'C-S', 'D-T'])