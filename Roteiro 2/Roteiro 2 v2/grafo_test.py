import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):

        #Grafo MEGA
        self.g_mega = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega.adicionaAresta('ab', 'A', 'B')
        self.g_mega.adicionaAresta('ac', 'A', 'C')
        self.g_mega.adicionaAresta('bd', 'B', 'D')
        self.g_mega.adicionaAresta('cd1', 'C', 'D')
        self.g_mega.adicionaAresta('cd2', 'C', 'D')
        self.g_mega.adicionaAresta('cf', 'C', 'F')
        self.g_mega.adicionaAresta('de', 'D', 'E')
        self.g_mega.adicionaAresta('dh', 'D', 'H')
        self.g_mega.adicionaAresta('eh', 'E', 'H')
        self.g_mega.adicionaAresta('ei', 'E', 'I')
        self.g_mega.adicionaAresta('ej', 'E', 'J')
        self.g_mega.adicionaAresta('fg', 'F', 'G')
        self.g_mega.adicionaAresta('fl', 'F', 'L')
        self.g_mega.adicionaAresta('fm', 'F', 'M')
        self.g_mega.adicionaAresta('gh', 'G', 'H')
        self.g_mega.adicionaAresta('gi', 'G', 'I')
        self.g_mega.adicionaAresta('hi', 'H', 'I')
        self.g_mega.adicionaAresta('ik', 'I', 'K')
        self.g_mega.adicionaAresta('il1', 'I', 'L')
        self.g_mega.adicionaAresta('il2', 'I', 'L')
        self.g_mega.adicionaAresta('jo', 'J', 'O')
        self.g_mega.adicionaAresta('jw', 'J', 'W')
        self.g_mega.adicionaAresta('jz', 'J', 'Z')
        self.g_mega.adicionaAresta('kn', 'K', 'N')
        self.g_mega.adicionaAresta('ko', 'K', 'O')
        self.g_mega.adicionaAresta('ln', 'L', 'N')
        self.g_mega.adicionaAresta('mn', 'M', 'N')
        self.g_mega.adicionaAresta('mp1', 'M', 'P')
        self.g_mega.adicionaAresta('mp2', 'M', 'P')
        self.g_mega.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega.adicionaAresta('nq2', 'N', 'Q')
        self.g_mega.adicionaAresta('nq3', 'N', 'Q')
        self.g_mega.adicionaAresta('nr', 'N', 'R')
        self.g_mega.adicionaAresta('ns', 'N', 'S')
        self.g_mega.adicionaAresta('os', 'O', 'S')
        self.g_mega.adicionaAresta('pq', 'P', 'Q')
        self.g_mega.adicionaAresta('qt', 'Q', 'T')
        self.g_mega.adicionaAresta('qu', 'Q', 'U')
        self.g_mega.adicionaAresta('rs', 'R', 'S')
        self.g_mega.adicionaAresta('st', 'S', 'T')
        self.g_mega.adicionaAresta('sz', 'S', 'Z')
        self.g_mega.adicionaAresta('tv', 'T', 'V')
        self.g_mega.adicionaAresta('uv', 'U', 'V')
        self.g_mega.adicionaAresta('wx', 'W', 'X')
        self.g_mega.adicionaAresta('wy', 'W', 'Y')
        self.g_mega.adicionaAresta('xy', 'X', 'Y')
        self.g_mega.adicionaAresta('yz', 'Y', 'Z')


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

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

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
        self.g_c.adicionaAresta('a1', 'J', 'C')
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
        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

        '''
        Grafos DFS e BFS 
        '''

        # Grafos da Paraíba DFS

        # Vertice J
        self.g_p_DFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_DFS_J.adicionaAresta('a9', 'T', 'Z')

        # Vertice C
        self.g_p_DFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_C.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_C.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_C.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_C.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_C.adicionaAresta('a8', 'M', 'T')
        self.g_p_DFS_C.adicionaAresta('a9', 'T', 'Z')

        # Vertice E
        self.g_p_DFS_E = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_E.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_E.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_E.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_E.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_E.adicionaAresta('a8', 'M', 'T')
        self.g_p_DFS_E.adicionaAresta('a9', 'T', 'Z')

        # Vertice P
        self.g_p_DFS_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_P.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_P.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_P.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_P.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_P.adicionaAresta('a8', 'M', 'T')
        self.g_p_DFS_P.adicionaAresta('a9', 'T', 'Z')

        # Vertice M
        self.g_p_DFS_M = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_M.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_M.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_M.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_M.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_M.adicionaAresta('a7', 'M', 'C')
        self.g_p_DFS_M.adicionaAresta('a9', 'T', 'Z')

        # Vertice T
        self.g_p_DFS_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_T.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_T.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_T.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_T.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_T.adicionaAresta('a7', 'M', 'C')
        self.g_p_DFS_T.adicionaAresta('a9', 'T', 'Z')

        # Vertice Z
        self.g_p_DFS_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_Z.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_Z.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_Z.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_Z.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_Z.adicionaAresta('a7', 'M', 'C')
        self.g_p_DFS_Z.adicionaAresta('a9', 'T', 'Z')
        # Grafos MEGA DFS

        # A

        self.g_mega_dfs_A = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_A.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_A.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_A.adicionaAresta('cd1', 'C', 'D')
        self.g_mega_dfs_A.adicionaAresta('cf', 'C', 'F')
        self.g_mega_dfs_A.adicionaAresta('eh', 'E', 'H')
        self.g_mega_dfs_A.adicionaAresta('ei', 'E', 'I')
        self.g_mega_dfs_A.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_A.adicionaAresta('gh', 'G', 'H')
        self.g_mega_dfs_A.adicionaAresta('ik', 'I', 'K')
        self.g_mega_dfs_A.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_A.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_A.adicionaAresta('kn', 'K', 'N')
        self.g_mega_dfs_A.adicionaAresta('ln', 'L', 'N')
        self.g_mega_dfs_A.adicionaAresta('mn', 'M', 'N')
        self.g_mega_dfs_A.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_A.adicionaAresta('os', 'O', 'S')
        self.g_mega_dfs_A.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_A.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_A.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_A.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_A.adicionaAresta('tv', 'T', 'V')
        self.g_mega_dfs_A.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_A.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_A.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_A.adicionaAresta('yz', 'Y', 'Z')

        # C

        self.g_mega_dfs_C = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_C.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_C.adicionaAresta('ac', 'A', 'C')
        self.g_mega_dfs_C.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_C.adicionaAresta('de', 'D', 'E')
        self.g_mega_dfs_C.adicionaAresta('eh', 'E', 'H')
        self.g_mega_dfs_C.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_C.adicionaAresta('fl', 'F', 'L')
        self.g_mega_dfs_C.adicionaAresta('gh', 'G', 'H')
        self.g_mega_dfs_C.adicionaAresta('ik', 'I', 'K')
        self.g_mega_dfs_C.adicionaAresta('il1', 'I', 'L')
        self.g_mega_dfs_C.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_C.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_C.adicionaAresta('kn', 'K', 'N')
        self.g_mega_dfs_C.adicionaAresta('mn', 'M', 'N')
        self.g_mega_dfs_C.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_C.adicionaAresta('os', 'O', 'S')
        self.g_mega_dfs_C.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_C.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_C.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_C.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_C.adicionaAresta('tv', 'T', 'V')
        self.g_mega_dfs_C.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_C.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_C.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_C.adicionaAresta('yz', 'Y', 'Z')

        # E

        self.g_mega_dfs_E = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_E.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_E.adicionaAresta('ac', 'A', 'C')
        self.g_mega_dfs_E.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_E.adicionaAresta('cf', 'C', 'F')
        self.g_mega_dfs_E.adicionaAresta('de', 'D', 'E')
        self.g_mega_dfs_E.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_E.adicionaAresta('gh', 'G', 'H')
        self.g_mega_dfs_E.adicionaAresta('hi', 'H', 'I')
        self.g_mega_dfs_E.adicionaAresta('ik', 'I', 'K')
        self.g_mega_dfs_E.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_E.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_E.adicionaAresta('kn', 'K', 'N')
        self.g_mega_dfs_E.adicionaAresta('ln', 'L', 'N')
        self.g_mega_dfs_E.adicionaAresta('mn', 'M', 'N')
        self.g_mega_dfs_E.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_E.adicionaAresta('os', 'O', 'S')
        self.g_mega_dfs_E.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_E.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_E.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_E.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_E.adicionaAresta('tv', 'T', 'V')
        self.g_mega_dfs_E.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_E.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_E.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_E.adicionaAresta('yz', 'Y', 'Z')

        # G

        self.g_mega_dfs_G = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_G.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_G.adicionaAresta('ac', 'A', 'C')
        self.g_mega_dfs_G.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_G.adicionaAresta('cf', 'C', 'F')
        self.g_mega_dfs_G.adicionaAresta('de', 'D', 'E')
        self.g_mega_dfs_G.adicionaAresta('eh', 'E', 'H')
        self.g_mega_dfs_G.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_G.adicionaAresta('hi', 'H', 'I')
        self.g_mega_dfs_G.adicionaAresta('ik', 'I', 'K')
        self.g_mega_dfs_G.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_G.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_G.adicionaAresta('kn', 'K', 'N')
        self.g_mega_dfs_G.adicionaAresta('ln', 'L', 'N')
        self.g_mega_dfs_G.adicionaAresta('mn', 'M', 'N')
        self.g_mega_dfs_G.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_G.adicionaAresta('os', 'O', 'S')
        self.g_mega_dfs_G.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_G.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_G.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_G.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_G.adicionaAresta('tv', 'T', 'V')
        self.g_mega_dfs_G.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_G.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_G.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_G.adicionaAresta('yz', 'Y', 'Z')

        # I

        self.g_mega_dfs_I = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_I.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_I.adicionaAresta('ac', 'A', 'C')
        self.g_mega_dfs_I.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_I.adicionaAresta('cf', 'C', 'F')
        self.g_mega_dfs_I.adicionaAresta('de', 'D', 'E')
        self.g_mega_dfs_I.adicionaAresta('ei', 'E', 'I')
        self.g_mega_dfs_I.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_I.adicionaAresta('fl', 'F', 'L')
        self.g_mega_dfs_I.adicionaAresta('gh', 'G', 'H')
        self.g_mega_dfs_I.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_I.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_I.adicionaAresta('kn', 'K', 'N')
        self.g_mega_dfs_I.adicionaAresta('ko', 'K', 'O')
        self.g_mega_dfs_I.adicionaAresta('ln', 'L', 'N')
        self.g_mega_dfs_I.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_I.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_I.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_I.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_dfs_I.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_I.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_I.adicionaAresta('sz', 'S', 'Z')
        self.g_mega_dfs_I.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_I.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_I.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_I.adicionaAresta('yz', 'Y', 'Z')

        # K

        self.g_mega_dfs_K = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_dfs_K.adicionaAresta('ab', 'A', 'B')
        self.g_mega_dfs_K.adicionaAresta('ac', 'A', 'C')
        self.g_mega_dfs_K.adicionaAresta('bd', 'B', 'D')
        self.g_mega_dfs_K.adicionaAresta('cf', 'C', 'F')
        self.g_mega_dfs_K.adicionaAresta('de', 'D', 'E')
        self.g_mega_dfs_K.adicionaAresta('ei', 'E', 'I')
        self.g_mega_dfs_K.adicionaAresta('fg', 'F', 'G')
        self.g_mega_dfs_K.adicionaAresta('fl', 'F', 'L')
        self.g_mega_dfs_K.adicionaAresta('gh', 'G', 'H')
        self.g_mega_dfs_K.adicionaAresta('ik', 'I', 'K')
        self.g_mega_dfs_K.adicionaAresta('jo', 'J', 'O')
        self.g_mega_dfs_K.adicionaAresta('jw', 'J', 'W')
        self.g_mega_dfs_K.adicionaAresta('ln', 'L', 'N')
        self.g_mega_dfs_K.adicionaAresta('mn', 'M', 'N')
        self.g_mega_dfs_K.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_dfs_K.adicionaAresta('os', 'O', 'S')
        self.g_mega_dfs_K.adicionaAresta('pq', 'P', 'Q')
        self.g_mega_dfs_K.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_dfs_K.adicionaAresta('rs', 'R', 'S')
        self.g_mega_dfs_K.adicionaAresta('st', 'S', 'T')
        self.g_mega_dfs_K.adicionaAresta('tv', 'T', 'V')
        self.g_mega_dfs_K.adicionaAresta('uv', 'U', 'V')
        self.g_mega_dfs_K.adicionaAresta('wx', 'W', 'X')
        self.g_mega_dfs_K.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_dfs_K.adicionaAresta('yz', 'Y', 'Z')

        # Grafos MEGA BFS

        # B

        self.g_mega_bfs_B = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_B.adicionaAresta('ab', 'A', 'B')
        self.g_mega_bfs_B.adicionaAresta('ac', 'A', 'C')
        self.g_mega_bfs_B.adicionaAresta('bd', 'B', 'D')
        self.g_mega_bfs_B.adicionaAresta('cf', 'C', 'F')
        self.g_mega_bfs_B.adicionaAresta('de', 'D', 'E')
        self.g_mega_bfs_B.adicionaAresta('dh', 'D', 'H')
        self.g_mega_bfs_B.adicionaAresta('ei', 'E', 'I')
        self.g_mega_bfs_B.adicionaAresta('ej', 'E', 'J')
        self.g_mega_bfs_B.adicionaAresta('fl', 'F', 'L')
        self.g_mega_bfs_B.adicionaAresta('fm', 'F', 'M')
        self.g_mega_bfs_B.adicionaAresta('gh', 'G', 'H')
        self.g_mega_bfs_B.adicionaAresta('ik', 'I', 'K')
        self.g_mega_bfs_B.adicionaAresta('jo', 'J', 'O')
        self.g_mega_bfs_B.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_B.adicionaAresta('jz', 'J', 'Z')
        self.g_mega_bfs_B.adicionaAresta('ln', 'L', 'N')
        self.g_mega_bfs_B.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_B.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_B.adicionaAresta('nr', 'N', 'R')
        self.g_mega_bfs_B.adicionaAresta('os', 'O', 'S')
        self.g_mega_bfs_B.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_B.adicionaAresta('st', 'S', 'T')
        self.g_mega_bfs_B.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_B.adicionaAresta('wx', 'W', 'X')
        self.g_mega_bfs_B.adicionaAresta('wy', 'W', 'Y')

        # D

        self.g_mega_bfs_D = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_D.adicionaAresta('ab', 'A', 'B')
        self.g_mega_bfs_D.adicionaAresta('bd', 'B', 'D')
        self.g_mega_bfs_D.adicionaAresta('cd1', 'C', 'D')
        self.g_mega_bfs_D.adicionaAresta('cf', 'C', 'F')
        self.g_mega_bfs_D.adicionaAresta('de', 'D', 'E')
        self.g_mega_bfs_D.adicionaAresta('dh', 'D', 'H')
        self.g_mega_bfs_D.adicionaAresta('ei', 'E', 'I')
        self.g_mega_bfs_D.adicionaAresta('ej', 'E', 'J')
        self.g_mega_bfs_D.adicionaAresta('fl', 'F', 'L')
        self.g_mega_bfs_D.adicionaAresta('fm', 'F', 'M')
        self.g_mega_bfs_D.adicionaAresta('gh', 'G', 'H')
        self.g_mega_bfs_D.adicionaAresta('ik', 'I', 'K')
        self.g_mega_bfs_D.adicionaAresta('jo', 'J', 'O')
        self.g_mega_bfs_D.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_D.adicionaAresta('jz', 'J', 'Z')
        self.g_mega_bfs_D.adicionaAresta('ln', 'L', 'N')
        self.g_mega_bfs_D.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_D.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_D.adicionaAresta('nr', 'N', 'R')
        self.g_mega_bfs_D.adicionaAresta('os', 'O', 'S')
        self.g_mega_bfs_D.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_D.adicionaAresta('st', 'S', 'T')
        self.g_mega_bfs_D.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_D.adicionaAresta('wx', 'W', 'X')
        self.g_mega_bfs_D.adicionaAresta('wy', 'W', 'Y')

        # F

        self.g_mega_bfs_F = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_F.adicionaAresta('ab', 'A', 'B')
        self.g_mega_bfs_F.adicionaAresta('ac', 'A', 'C')
        self.g_mega_bfs_F.adicionaAresta('cd1', 'C', 'D')
        self.g_mega_bfs_F.adicionaAresta('cf', 'C', 'F')
        self.g_mega_bfs_F.adicionaAresta('de', 'D', 'E')
        self.g_mega_bfs_F.adicionaAresta('ej', 'E', 'J')
        self.g_mega_bfs_F.adicionaAresta('fg', 'F', 'G')
        self.g_mega_bfs_F.adicionaAresta('fl', 'F', 'L')
        self.g_mega_bfs_F.adicionaAresta('fm', 'F', 'M')
        self.g_mega_bfs_F.adicionaAresta('gh', 'G', 'H')
        self.g_mega_bfs_F.adicionaAresta('gi', 'G', 'I')
        self.g_mega_bfs_F.adicionaAresta('ik', 'I', 'K')
        self.g_mega_bfs_F.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_F.adicionaAresta('ko', 'K', 'O')
        self.g_mega_bfs_F.adicionaAresta('ln', 'L', 'N')
        self.g_mega_bfs_F.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_F.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_F.adicionaAresta('nr', 'N', 'R')
        self.g_mega_bfs_F.adicionaAresta('ns', 'N', 'S')
        self.g_mega_bfs_F.adicionaAresta('qt', 'Q', 'T')
        self.g_mega_bfs_F.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_F.adicionaAresta('sz', 'S', 'Z')
        self.g_mega_bfs_F.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_F.adicionaAresta('wx', 'W', 'X')
        self.g_mega_bfs_F.adicionaAresta('yz', 'Y', 'Z')

        # H

        self.g_mega_bfs_H = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_H.adicionaAresta('ab', 'A', 'B')
        self.g_mega_bfs_H.adicionaAresta('bd', 'B', 'D')
        self.g_mega_bfs_H.adicionaAresta('cd1', 'C', 'D')
        self.g_mega_bfs_H.adicionaAresta('dh', 'D', 'H')
        self.g_mega_bfs_H.adicionaAresta('eh', 'E', 'H')
        self.g_mega_bfs_H.adicionaAresta('ej', 'E', 'J')
        self.g_mega_bfs_H.adicionaAresta('fg', 'F', 'G')
        self.g_mega_bfs_H.adicionaAresta('fm', 'F', 'M')
        self.g_mega_bfs_H.adicionaAresta('gh', 'G', 'H')
        self.g_mega_bfs_H.adicionaAresta('hi', 'H', 'I')
        self.g_mega_bfs_H.adicionaAresta('ik', 'I', 'K')
        self.g_mega_bfs_H.adicionaAresta('il1', 'I', 'L')
        self.g_mega_bfs_H.adicionaAresta('jo', 'J', 'O')
        self.g_mega_bfs_H.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_H.adicionaAresta('jz', 'J', 'Z')
        self.g_mega_bfs_H.adicionaAresta('kn', 'K', 'N')
        self.g_mega_bfs_H.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_H.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_H.adicionaAresta('nr', 'N', 'R')
        self.g_mega_bfs_H.adicionaAresta('os', 'O', 'S')
        self.g_mega_bfs_H.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_H.adicionaAresta('st', 'S', 'T')
        self.g_mega_bfs_H.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_H.adicionaAresta('wx', 'W', 'X')
        self.g_mega_bfs_H.adicionaAresta('wy', 'W', 'Y')

        # J

        self.g_mega_bfs_J = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_J.adicionaAresta('ab', 'A', 'B')
        self.g_mega_bfs_J.adicionaAresta('bd', 'B', 'D')
        self.g_mega_bfs_J.adicionaAresta('cd1', 'C', 'D')
        self.g_mega_bfs_J.adicionaAresta('cf', 'C', 'F')
        self.g_mega_bfs_J.adicionaAresta('de', 'D', 'E')
        self.g_mega_bfs_J.adicionaAresta('eh', 'E', 'H')
        self.g_mega_bfs_J.adicionaAresta('ei', 'E', 'I')
        self.g_mega_bfs_J.adicionaAresta('ej', 'E', 'J')
        self.g_mega_bfs_J.adicionaAresta('gh', 'G', 'H')
        self.g_mega_bfs_J.adicionaAresta('il1', 'I', 'L')
        self.g_mega_bfs_J.adicionaAresta('jo', 'J', 'O')
        self.g_mega_bfs_J.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_J.adicionaAresta('jz', 'J', 'Z')
        self.g_mega_bfs_J.adicionaAresta('kn', 'K', 'N')
        self.g_mega_bfs_J.adicionaAresta('ko', 'K', 'O')
        self.g_mega_bfs_J.adicionaAresta('mn', 'M', 'N')
        self.g_mega_bfs_J.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_J.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_J.adicionaAresta('os', 'O', 'S')
        self.g_mega_bfs_J.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_J.adicionaAresta('rs', 'R', 'S')
        self.g_mega_bfs_J.adicionaAresta('st', 'S', 'T')
        self.g_mega_bfs_J.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_J.adicionaAresta('wx', 'W', 'X')
        self.g_mega_bfs_J.adicionaAresta('wy', 'W', 'Y')

        # R

        self.g_mega_bfs_R = MeuGrafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_mega_bfs_R.adicionaAresta('ac', 'A', 'C')
        self.g_mega_bfs_R.adicionaAresta('bd', 'B', 'D')
        self.g_mega_bfs_R.adicionaAresta('cf', 'C', 'F')
        self.g_mega_bfs_R.adicionaAresta('de', 'D', 'E')
        self.g_mega_bfs_R.adicionaAresta('ei', 'E', 'I')
        self.g_mega_bfs_R.adicionaAresta('fl', 'F', 'L')
        self.g_mega_bfs_R.adicionaAresta('gi', 'G', 'I')
        self.g_mega_bfs_R.adicionaAresta('hi', 'H', 'I')
        self.g_mega_bfs_R.adicionaAresta('ik', 'I', 'K')
        self.g_mega_bfs_R.adicionaAresta('jo', 'J', 'O')
        self.g_mega_bfs_R.adicionaAresta('jw', 'J', 'W')
        self.g_mega_bfs_R.adicionaAresta('kn', 'K', 'N')
        self.g_mega_bfs_R.adicionaAresta('ln', 'L', 'N')
        self.g_mega_bfs_R.adicionaAresta('mn', 'M', 'N')
        self.g_mega_bfs_R.adicionaAresta('mp1', 'M', 'P')
        self.g_mega_bfs_R.adicionaAresta('nq1', 'N', 'Q')
        self.g_mega_bfs_R.adicionaAresta('nr', 'N', 'R')
        self.g_mega_bfs_R.adicionaAresta('os', 'O', 'S')
        self.g_mega_bfs_R.adicionaAresta('qu', 'Q', 'U')
        self.g_mega_bfs_R.adicionaAresta('rs', 'R', 'S')
        self.g_mega_bfs_R.adicionaAresta('st', 'S', 'T')
        self.g_mega_bfs_R.adicionaAresta('sz', 'S', 'Z')
        self.g_mega_bfs_R.adicionaAresta('tv', 'T', 'V')
        self.g_mega_bfs_R.adicionaAresta('xy', 'X', 'Y')
        self.g_mega_bfs_R.adicionaAresta('yz', 'Y', 'Z')

        # Grafos da Paraíba BFS

        # Vertice J
        self.g_p_BFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_J.adicionaAresta('a7', 'C', 'M')
        self.g_p_BFS_J.adicionaAresta('a9', 'T', 'Z')

        # Vertice C
        self.g_p_BFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_C.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_C.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_C.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_C.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_C.adicionaAresta('a7', 'C', 'M')
        self.g_p_BFS_C.adicionaAresta('a9', 'T', 'Z')

        # Vertice E
        self.g_p_BFS_E = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_E.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_E.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_E.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_E.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_E.adicionaAresta('a7', 'C', 'M')
        self.g_p_BFS_E.adicionaAresta('a9', 'T', 'Z')

        # Vertice P
        self.g_p_BFS_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_P.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_P.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_P.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_P.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_P.adicionaAresta('a7', 'C', 'M')
        self.g_p_BFS_P.adicionaAresta('a9', 'T', 'Z')

        # Vertice M
        self.g_p_BFS_M = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_M.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_M.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_M.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_M.adicionaAresta('a7', 'M', 'C')
        self.g_p_BFS_M.adicionaAresta('a8', 'M', 'T')
        self.g_p_BFS_M.adicionaAresta('a9', 'T', 'Z')

        # Vertice T
        self.g_p_BFS_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_T.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_T.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_T.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_T.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_T.adicionaAresta('a8', 'M', 'T')
        self.g_p_BFS_T.adicionaAresta('a9', 'T', 'Z')

        # Vertice Z
        self.g_p_BFS_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_Z.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_Z.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_Z.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_Z.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_Z.adicionaAresta('a8', 'M', 'T')
        self.g_p_BFS_Z.adicionaAresta('a9', 'T', 'Z')

    '''
    TESTES 
    '''

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

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
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
        self.assertEqual(self.g_d2.grau('A'), 0)

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
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
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
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    '''
    Testes criados DFS e BFS
    '''

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), self.g_p_DFS_J)
        self.assertEqual(self.g_p.dfs('C'), self.g_p_DFS_C)
        self.assertEqual(self.g_p.dfs('E'), self.g_p_DFS_E)
        self.assertEqual(self.g_p.dfs('P'), self.g_p_DFS_P)
        self.assertEqual(self.g_p.dfs('M'), self.g_p_DFS_M)
        self.assertEqual(self.g_p.dfs('T'), self.g_p_DFS_T)
        self.assertEqual(self.g_p.dfs('Z'), self.g_p_DFS_Z)

        self.assertEqual(self.g_mega.dfs('A'), self.g_mega_dfs_A)
        self.assertEqual(self.g_mega.dfs('C'), self.g_mega_dfs_C)
        self.assertEqual(self.g_mega.dfs('E'), self.g_mega_dfs_E)
        self.assertEqual(self.g_mega.dfs('G'), self.g_mega_dfs_G)
        self.assertEqual(self.g_mega.dfs('I'), self.g_mega_dfs_I)
        self.assertEqual(self.g_mega.dfs('K'), self.g_mega_dfs_K)


    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), self.g_p_BFS_J)
        self.assertEqual(self.g_p.bfs('C'), self.g_p_BFS_C)
        self.assertEqual(self.g_p.bfs('E'), self.g_p_BFS_E)
        self.assertEqual(self.g_p.bfs('P'), self.g_p_BFS_P)
        self.assertEqual(self.g_p.bfs('M'), self.g_p_BFS_M)
        self.assertEqual(self.g_p.bfs('T'), self.g_p_BFS_T)
        self.assertEqual(self.g_p.bfs('Z'), self.g_p_BFS_Z)

        self.assertEqual(self.g_mega.bfs('B'), self.g_mega_bfs_B)
        self.assertEqual(self.g_mega.bfs('D'), self.g_mega_bfs_D)
        self.assertEqual(self.g_mega.bfs('F'), self.g_mega_bfs_F)
        self.assertEqual(self.g_mega.bfs('H'), self.g_mega_bfs_H)
        self.assertEqual(self.g_mega.bfs('J'), self.g_mega_bfs_J)
        self.assertEqual(self.g_mega.bfs('R'), self.g_mega_bfs_R)