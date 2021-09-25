import unittest
from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo

# paraiba = MeuGrafo(['11', '13', '14', '15', '16','17','21','22', '23', '24', '25', '26','27',
# '31','32', '33', '34', '35', '36','41','42', '43', '44', '45','51','52', '53', '54', '55',
# '61','62', '63', '64', '65','71','72', '73', '74', '75','81','82', '83', '84', '85',
# '91','92', '93', '94', '101','102','103'])

paraiba = MeuGrafo(['11', '14', '15', '16','21', '24', '25', '26',
'31', '33', '34', '35', '36','41','42', '43', '44', '45','51','52', '53', '54', '55',
'61','62', '63', '64', '65','71','72', '73', '74', '75','81','82', '83', '84', '85','92', '93', '94','103'])

paraiba.adicionaAresta("a1", "11","21")
paraiba.adicionaAresta("a2", "14","24")
paraiba.adicionaAresta("a3", "15","24")
paraiba.adicionaAresta("a4", "14","25")
paraiba.adicionaAresta("a5", "15","25")
paraiba.adicionaAresta("a6", "16","26")
paraiba.adicionaAresta("a7", "21","31")
paraiba.adicionaAresta("a8", "24","33")
paraiba.adicionaAresta("a9", "14","34")
paraiba.adicionaAresta("a10", "15","34")
paraiba.adicionaAresta("a11", "14","35")
paraiba.adicionaAresta("a12", "15","35")
paraiba.adicionaAresta("a13", "26","36")
paraiba.adicionaAresta("a14", "21","41")
paraiba.adicionaAresta("a15", "24","43")
paraiba.adicionaAresta("a16", "24","44")
paraiba.adicionaAresta("a17", "36","44")
paraiba.adicionaAresta("a18", "36","45")
paraiba.adicionaAresta("a19", "31","51")
paraiba.adicionaAresta("a20", "31","52")
paraiba.adicionaAresta("a21", "24","53")
paraiba.adicionaAresta("a22", "24","54")
paraiba.adicionaAresta("a23", "36","55")
paraiba.adicionaAresta("a24", "44","55")
paraiba.adicionaAresta("a25", "51","61")
paraiba.adicionaAresta("a26", "43","62")
paraiba.adicionaAresta("a27", "34","63")
paraiba.adicionaAresta("a28", "35","63")
paraiba.adicionaAresta("a29", "31","64")
paraiba.adicionaAresta("a30", "55","65")
paraiba.adicionaAresta("a31", "24","72")
paraiba.adicionaAresta("a32", "63","73")
paraiba.adicionaAresta("a33", "52","75")
paraiba.adicionaAresta("a34", "64","75")
paraiba.adicionaAresta("a35", "34","81")
paraiba.adicionaAresta("a36", "35","81")
paraiba.adicionaAresta("a37", "54","81")
paraiba.adicionaAresta("a38", "73","82")
paraiba.adicionaAresta("a39", "74","83")
paraiba.adicionaAresta("a40", "61","84")
paraiba.adicionaAresta("a41", "64","84")
paraiba.adicionaAresta("a42", "75","85")
paraiba.adicionaAresta("a43", "83","92")
paraiba.adicionaAresta("a44", "44","93")
paraiba.adicionaAresta("a45", "45","93")
paraiba.adicionaAresta("a46", "61","94")
paraiba.adicionaAresta("a47", "75","94")
paraiba.adicionaAresta("a48", "92","103")
print(paraiba)
print(paraiba.topologicalSort())

unittest.main()