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

        # Grafos não direcionados
        self.g_nd = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_nd.adicionaAresta('a1', 'A', 'B')
        self.g_nd.adicionaAresta('a2', 'A', 'G')
        self.g_nd.adicionaAresta('a3', 'A', 'J')
        self.g_nd.adicionaAresta('a4', 'G', 'K')
        self.g_nd.adicionaAresta('a5', 'J', 'K')
        self.g_nd.adicionaAresta('a6', 'G', 'J')
        self.g_nd.adicionaAresta('a7', 'I', 'J')
        self.g_nd.adicionaAresta('a8', 'G', 'I')
        self.g_nd.adicionaAresta('a9', 'G', 'H')
        self.g_nd.adicionaAresta('a10', 'F', 'H')
        self.g_nd.adicionaAresta('a11', 'B', 'F')
        self.g_nd.adicionaAresta('a12', 'B', 'G')
        self.g_nd.adicionaAresta('a13', 'B', 'C')
        self.g_nd.adicionaAresta('a14', 'C', 'D')
        self.g_nd.adicionaAresta('a15', 'D', 'E')
        self.g_nd.adicionaAresta('a16', 'B', 'D')
        self.g_nd.adicionaAresta('a17', 'B', 'E')

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
    
    def test_dfs(self):
        self.assertEqual(list(self.g_p.dfs('C').A),['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('J').A),['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('E').A),['a2', 'a1', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('P').A),['a4', 'a1', 'a2', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('M').A),['a7', 'a1', 'a2', 'a4', 'a6', 'a9'])
        self.assertEqual(list(self.g_p.dfs('T').A),['a6', 'a1', 'a2', 'a4', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.dfs('Z').A),['a9', 'a6', 'a1', 'a2', 'a4', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('J').A),['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('C').A),['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('E').A),['a2', 'a1', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('P').A),['a3', 'a1', 'a2', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('M').A),['a5', 'a1', 'a2', 'a3', 'a4', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('T').A),['a4', 'a1', 'a2', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('Z').A),['a7', 'a4', 'a1', 'a2', 'a3', 'a5'])
        self.assertEqual(list(self.g_c.dfs('J').A),['a1', 'a4', 'a6'])
        self.assertEqual(list(self.g_c.dfs('C').A),['a1', 'a2', 'a6'])
        self.assertEqual(list(self.g_c.dfs('E').A),['a2', 'a1', 'a5'])
        self.assertEqual(list(self.g_c.dfs('P').A),['a3', 'a1', 'a4'])
        self.assertEqual(list(self.g_nd.dfs('A').A),['a1', 'a11', 'a10', 'a9', 'a4', 'a5', 'a7', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_nd.dfs('B').A),['a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_nd.dfs('C').A),['a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a16', 'a15'])
        self.assertEqual(list(self.g_nd.dfs('D').A),['a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a17'])
        self.assertEqual(list(self.g_nd.dfs('E').A),['a15', 'a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10'])
        self.assertEqual(list(self.g_nd.dfs('F').A),['a10', 'a9', 'a2', 'a1', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_nd.dfs('G').A),['a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_nd.dfs('H').A),['a9', 'a2', 'a1', 'a11', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_nd.dfs('I').A),['a7', 'a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_nd.dfs('J').A),['a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a8', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_nd.dfs('K').A),['a4', 'a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a7'])
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_bfs(self):
        self.assertEqual(list(self.g_p.bfs('C').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('E').A),['a2', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('J').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('M').A),['a7', 'a8', 'a1', 'a2', 'a4', 'a9'])
        self.assertEqual(list(self.g_p.bfs('P').A),['a4', 'a1', 'a2', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('T').A),['a6', 'a8', 'a9', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_p.bfs('Z').A),['a9', 'a6', 'a8', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_nd.bfs('A').A),['a1', 'a2', 'a3', 'a11', 'a13', 'a16', 'a17', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.g_nd.bfs('B').A),['a1', 'a11', 'a12', 'a13', 'a16', 'a17', 'a3', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.g_nd.bfs('C').A),['a13', 'a14', 'a1', 'a11', 'a12', 'a17', 'a3', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.g_nd.bfs('D').A),['a14', 'a15', 'a16', 'a1', 'a11', 'a12', 'a3', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.g_nd.bfs('E').A),['a15', 'a17', 'a14', 'a1', 'a11', 'a12', 'a3', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.g_nd.bfs('F').A),['a10', 'a11', 'a9', 'a1', 'a13', 'a16', 'a17', 'a4', 'a6', 'a8'])
        self.assertEqual(list(self.g_nd.bfs('G').A),['a2', 'a4', 'a6', 'a8', 'a9', 'a12', 'a10', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_nd.bfs('H').A),['a9', 'a10', 'a2', 'a4', 'a6', 'a8', 'a12', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_nd.bfs('I').A),['a7', 'a8', 'a3', 'a5', 'a9', 'a12', 'a10', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_nd.bfs('J').A),['a3', 'a5', 'a6', 'a7', 'a1', 'a9', 'a11', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_nd.bfs('K').A),['a4', 'a5', 'a2', 'a8', 'a9', 'a12', 'a10', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_l1.bfs('A').A),['a2'])
        self.assertEqual(list(self.g_l2.bfs('A').A),['a1'])
        self.assertEqual(list(self.g_l3.bfs('C').A),['a1'])
        self.assertEqual(list(self.g_l4.bfs('D').A),[])
        self.assertEqual(list(self.g_l5.bfs('C').A),['a1'])

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertTrue(self.g_nd.conexo())

    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(1), ['J', 'a1', 'C'])
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a6', 'T', 'a8', 'M'])

        self.assertEqual(self.g_p_sem_paralelas.caminho(1), ['J', 'a1', 'C'])
        self.assertEqual(self.g_p_sem_paralelas.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p_sem_paralelas.caminho(3), ['J', 'a1', 'C', 'a4', 'T', 'a6', 'M'])

        self.assertEqual(self.g_c.caminho(1), ['J', 'a1', 'C'])
        self.assertEqual(self.g_c.caminho(2), ['J', 'a1', 'C', 'a4', 'E'])
        self.assertEqual(self.g_c.caminho(3), ['J', 'a1', 'C', 'a4', 'E', 'a6', 'P'])

        self.assertEqual(self.g_nd.caminho(1), ['A', 'a1', 'B'])
        self.assertEqual(self.g_nd.caminho(2), ['A', 'a1', 'B', 'a11', 'F'])
        self.assertEqual(self.g_nd.caminho(3), ['A', 'a1', 'B', 'a11', 'F', 'a10', 'H'])
        self.assertEqual(self.g_nd.caminho(4), ['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G'])
        self.assertEqual(self.g_nd.caminho(5), ['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K'])
        self.assertEqual(self.g_nd.caminho(6), ['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K', 'a5', 'J'])
        self.assertEqual(self.g_nd.caminho(7), ['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K', 'a5', 'J', 'a7', 'I'])
        self.assertEqual(self.g_nd.caminho(8), ['E', 'a15', 'D', 'a14', 'C', 'a13', 'B', 'a1', 'A', 'a2', 'G', 'a4', 'K', 'a5', 'J', 'a7', 'I'])
    
if __name__ == '__main__':
    unittest.main()
