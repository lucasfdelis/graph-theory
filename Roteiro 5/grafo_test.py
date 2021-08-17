import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafos eulerianos
        self.g_euler1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T'])
        self.g_euler1.adicionaAresta("a1", "J", "C")
        self.g_euler1.adicionaAresta("a2", "C", "E")
        self.g_euler1.adicionaAresta("a3", "C", "E")
        self.g_euler1.adicionaAresta("a4", "C", "P")
        self.g_euler1.adicionaAresta("a5", "C", "P")
        self.g_euler1.adicionaAresta("a6", "C", "M")
        self.g_euler1.adicionaAresta("a7", "C", "T")
        self.g_euler1.adicionaAresta("a8", "M", "T")

        self.g_euler2  = MeuGrafo(['0','1','2','3'])
        self.g_euler2.adicionaAresta('a1','0','1')
        self.g_euler2.adicionaAresta('a2','0','2')
        self.g_euler2.adicionaAresta('a3','1','2')
        self.g_euler2.adicionaAresta('a4','2','3')

        self.g_euler3 = MeuGrafo(['0','1','2'])
        self.g_euler3.adicionaAresta('a1','0','1')
        self.g_euler3.adicionaAresta('a2','1','2')
        self.g_euler3.adicionaAresta('a3','2','0')

        self.g_euler4 = MeuGrafo(['0', '1', '2', '3', '4'])
        self.g_euler4.adicionaAresta("a1", "1", "0")
        self.g_euler4.adicionaAresta("a2", "0", "2")
        self.g_euler4.adicionaAresta("a3", "2", "1")
        self.g_euler4.adicionaAresta("a4", "0", "3")
        self.g_euler4.adicionaAresta("a5", "3", "4")
        self.g_euler4.adicionaAresta("a6", "3", "2")
        self.g_euler4.adicionaAresta("a7", "3", "1")
        self.g_euler4.adicionaAresta("a8", "2", "4")

        self.g_euler5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_euler5.adicionaAresta('1', 'A', 'B')
        self.g_euler5.adicionaAresta('2', 'B', 'C')
        self.g_euler5.adicionaAresta('3', 'C', 'D')
        self.g_euler5.adicionaAresta('4', 'D', 'E')
        self.g_euler5.adicionaAresta('5', 'A', 'C')
        self.g_euler5.adicionaAresta('6', 'A', 'D')
        self.g_euler5.adicionaAresta('7', 'A', 'E')
        self.g_euler5.adicionaAresta('8', 'B', 'D')
        self.g_euler5.adicionaAresta('9', 'B', 'E')
        self.g_euler5.adicionaAresta('10', 'C', 'E')

        self.g_euler6 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler6.adicionaAresta('a1', '1', '2')
        self.g_euler6.adicionaAresta('a2', '2', '3')
        self.g_euler6.adicionaAresta('a3', '3', '4')
        self.g_euler6.adicionaAresta('a4', '4', '2')
        self.g_euler6.adicionaAresta('a5', '5', '2')
        self.g_euler6.adicionaAresta('a6', '1', '5')

        self.g_euler7 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler7.adicionaAresta('a1', '1', '2')
        self.g_euler7.adicionaAresta('a2', '2', '3')
        self.g_euler7.adicionaAresta('a3', '3', '4')
        self.g_euler7.adicionaAresta('a4', '4', '5')
        self.g_euler7.adicionaAresta('a5', '5', '1')

        self.g_euler8 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler8.adicionaAresta('a1', '1', '3')
        self.g_euler8.adicionaAresta('a2', '3', '4')
        self.g_euler8.adicionaAresta('a3', '4', '1')
        self.g_euler8.adicionaAresta('a4', '4', '5')
        self.g_euler8.adicionaAresta('a5', '5', '3')
        self.g_euler8.adicionaAresta('a6', '2', '3')
        self.g_euler8.adicionaAresta('a7', '2', '4')

        self.g_euler9 = MeuGrafo(['1','2','3','4','5'])
        self.g_euler9.adicionaAresta('a1', '1', '2')
        self.g_euler9.adicionaAresta('a2', '2', '3')
        self.g_euler9.adicionaAresta('a3', '3', '4')
        self.g_euler9.adicionaAresta('a4', '4', '5')
        self.g_euler9.adicionaAresta('a5', '5', '1')
        self.g_euler9.adicionaAresta('a6', '1', '4')
        self.g_euler9.adicionaAresta('a7', '1', '3')
        self.g_euler9.adicionaAresta('a8', '2', '5')
        self.g_euler9.adicionaAresta('a9', '2', '4')
        self.g_euler9.adicionaAresta('a10', '3', '5')

        self.g_euler10 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler10.adicionaAresta('a1', '1', '2')
        self.g_euler10.adicionaAresta('a2', '2', '3')
        self.g_euler10.adicionaAresta('a3', '3', '4')
        self.g_euler10.adicionaAresta('a4', '4', '1')
        self.g_euler10.adicionaAresta('a5', '4', '2')
        self.g_euler10.adicionaAresta('a6', '2', '6')
        self.g_euler10.adicionaAresta('a7', '5', '6')
        self.g_euler10.adicionaAresta('a8', '5', '4')

        self.g_euler11 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler11.adicionaAresta('a1', '1', '2')
        self.g_euler11.adicionaAresta('a2', '2', '5')
        self.g_euler11.adicionaAresta('a3', '5', '3')
        self.g_euler11.adicionaAresta('a4', '3', '4')
        self.g_euler11.adicionaAresta('a5', '4', '5')
        self.g_euler11.adicionaAresta('a6', '5', '6')
        self.g_euler11.adicionaAresta('a7', '6', '1')

        self.g_euler12 = MeuGrafo(['1','2','3','4','5','6'])
        self.g_euler12.adicionaAresta('a1', '1', '2')
        self.g_euler12.adicionaAresta('a2', '2', '3')
        self.g_euler12.adicionaAresta('a3', '3', '4')
        self.g_euler12.adicionaAresta('a4', '4', '5')
        self.g_euler12.adicionaAresta('a5', '5', '6')
        self.g_euler12.adicionaAresta('a6', '6', '1')
        self.g_euler12.adicionaAresta('a7', '6', '2')
        self.g_euler12.adicionaAresta('a8', '2', '4')
        self.g_euler12.adicionaAresta('a9', '6', '4')
        
    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
    
    def test_euleriano(self):
        self.assertEqual(self.g_p.exibirCaminho(),'O grafo não é euleriano.')
        self.assertEqual(set(self.g_euler1.exibirCaminho()), set(['J', 'a1', 'C', 'a2', 'E', 'a3', 'C', 'a4', 'P', 'a5', 'C', 'a6', 'M', 'a8', 'T', 'a7', 'C']))
        self.assertEqual(set(self.g_euler2.exibirCaminho()), set(['2', 'a2', '0', 'a1', '1', 'a3', '2', 'a4', '3']))
        self.assertEqual(set(self.g_euler3.exibirCaminho()), set(['0', 'a1', '1', 'a2', '2', 'a3', '0']))
        self.assertEqual(set(self.g_euler4.exibirCaminho()), set(['0', 'a1', '1', 'a3', '2', 'a2', '0', 'a4', '3', 'a5', '4', 'a8', '2', 'a6', '3', 'a7', '1']))
        self.assertEqual(set(self.g_euler5.exibirCaminho()), set(['A', '1', 'B', '2', 'C', '3', 'D', '4', 'E', '7', 'A', '5', 'C', '10', 'E', '9', 'B', '8', 'D', '6', 'A']))
        