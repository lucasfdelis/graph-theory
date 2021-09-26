import unittest

from meu_grafo_matriz_adjacencia_dir import MeuGrafo

eng_comp = MeuGrafo(['Pré-Cálculo','Inglês Instrumental','Introdução à Engenharia de Computação', 
'Algoritmos e Programação','Lab. de Algoritmos e Programação','Sistemas Digitais I',
'Medição Eletro-eletrônica','Cálculo I','Estatística Aplicada à Computação', 
'Leitura e Produção de Textos','Estruturas de Dados e Algoritmos',
'Laboratório de Estruturas de Dados e Algoritmos','Sistemas Digitais II',
'Educação Ambiental e Sustentabilidade','Cálculo II','Relações Humanas no Trabalho',
'Teoria dos Grafos','Programação Orientada a Objetos','Laboratório de Programação Orientada a Objetos',
'Organização e Arquitetura de Computadores','Física Clássica','Metodologia da Pesquisa Científica',
'Teoria da Computação','Sistemas Operacionais',
'Microprocessadores e Microcontroladores','Álgebra Linear Aplicada à Computação',
'Eletricidade e Eletromagnetismo','Redes de Computadore','Bancos de Dados', 
'Projeto de Sistemas Digitais','Métodos Numéricos','Inteligência Artificial',
'Padrões de Projetos','Sinais e Sistemas','Verificação Funcional de Sistemas Digitais',
'Libras','Análise e Técnicas de Algoritmos','Análise e Projeto de Sistemas',
'Desenho Assistido por Computador','Circuitos Eletro-Eletrônicos',
'Teste de Software','Gerência de Projetos','Técnicas de Prototipagem', 
'Processamento Digital de Sinais','Sensores e Atuadores',
'Empreendedorismo de Base Tecnológica','Projeto em Engenharia de Computação I',
'Sistemas Embarcados','Controle e Automação I','Educação em Direitos Humanos',
'Educação em Diversidade','Projeto em Engenharia de Computação II'])

eng_comp.adicionaAresta("a1","Pré-Cálculo","Cálculo I")
eng_comp.adicionaAresta("a2","Algoritmos e Programação","Estruturas de Dados e Algoritmos")
eng_comp.adicionaAresta("a3","Lab. de Algoritmos e Programação","Estruturas de Dados e Algoritmos")
eng_comp.adicionaAresta("a4","Algoritmos e Programação","Laboratório de Estruturas de Dados e Algoritmos")
eng_comp.adicionaAresta("a5","Lab. de Algoritmos e Programação","Laboratório de Estruturas de Dados e Algoritmos")
eng_comp.adicionaAresta("a6","Sistemas Digitais I","Sistemas Digitais II")
eng_comp.adicionaAresta("a7","Cálculo I","Cálculo II")
eng_comp.adicionaAresta("a8","Estruturas de Dados e Algoritmos","Teoria dos Grafos")
eng_comp.adicionaAresta("a9","Algoritmos e Programação","Programação Orientada a Objetos")
eng_comp.adicionaAresta("a10","Lab. de Algoritmos e Programação","Programação Orientada a Objetos")
eng_comp.adicionaAresta("a11","Algoritmos e Programação","Laboratório de Programação Orientada a Objetos")
eng_comp.adicionaAresta("a12","Lab. de Algoritmos e Programação","Laboratório de Programação Orientada a Objetos")
eng_comp.adicionaAresta("a13","Sistemas Digitais II","Organização e Arquitetura de Computadores")
eng_comp.adicionaAresta("a14","Cálculo I","Física Clássica")
eng_comp.adicionaAresta("a15","Estruturas de Dados e Algoritmos","Teoria da Computação")
eng_comp.adicionaAresta("a16","Estruturas de Dados e Algoritmos","Sistemas Operacionais")
eng_comp.adicionaAresta("a17","Organização e Arquitetura de Computadores","Sistemas Operacionais")
eng_comp.adicionaAresta("a18","Organização e Arquitetura de Computadores","Microprocessadores e Microcontroladores")
eng_comp.adicionaAresta("a19","Cálculo II","Álgebra Linear Aplicada à Computação")
eng_comp.adicionaAresta("a20","Cálculo II","Eletricidade e Eletromagnetismo")
eng_comp.adicionaAresta("a21","Estruturas de Dados e Algoritmos","Redes de Computadore")
eng_comp.adicionaAresta("a22","Estruturas de Dados e Algoritmos","Bancos de Dados")
eng_comp.adicionaAresta("a23","Organização e Arquitetura de Computadores","Projeto de Sistemas Digitais")
eng_comp.adicionaAresta("a24","Sistemas Operacionais","Projeto de Sistemas Digitais")
eng_comp.adicionaAresta("a25","Álgebra Linear Aplicada à Computação","Métodos Numéricos")
eng_comp.adicionaAresta("a26","Teoria da Computação","Inteligência Artificial")
eng_comp.adicionaAresta("a27","Programação Orientada a Objetos","Padrões de Projetos")
eng_comp.adicionaAresta("a28","Laboratório de Programação Orientada a Objetos","Padrões de Projetos")
eng_comp.adicionaAresta("a29","Cálculo II","Sinais e Sistemas")
eng_comp.adicionaAresta("a30","Projeto de Sistemas Digitais","Verificação Funcional de Sistemas Digitais")
eng_comp.adicionaAresta("a31","Estruturas de Dados e Algoritmos","Análise e Técnicas de Algoritmos")
eng_comp.adicionaAresta("a32","Padrões de Projetos","Análise e Projeto de Sistemas")
eng_comp.adicionaAresta("a33","Eletricidade e Eletromagnetismo","Circuitos Eletro-Eletrônicos")
eng_comp.adicionaAresta("a34","Sinais e Sistemas","Circuitos Eletro-Eletrônicos")
eng_comp.adicionaAresta("a35","Programação Orientada a Objetos","Teste de Software")
eng_comp.adicionaAresta("a36","Laboratório de Programação Orientada a Objetos","Teste de Software")
eng_comp.adicionaAresta("a37","Bancos de Dados","Teste de Software")
eng_comp.adicionaAresta("a38","Análise e Projeto de Sistemas","Gerência de Projetos")
eng_comp.adicionaAresta("a39","Desenho Assistido por Computador","Técnicas de Prototipagem")
eng_comp.adicionaAresta("a40","Métodos Numéricos","Processamento Digital de Sinais")
eng_comp.adicionaAresta("a41","Sinais e Sistemas","Processamento Digital de Sinais")
eng_comp.adicionaAresta("a42","Circuitos Eletro-Eletrônicos","Sensores e Atuadores")
eng_comp.adicionaAresta("a43","Técnicas de Prototipagem","Projeto em Engenharia de Computação I")
eng_comp.adicionaAresta("a44","Sistemas Operacionais","Sistemas Embarcados")
eng_comp.adicionaAresta("a45","Microprocessadores e Microcontroladores","Sistemas Embarcados")
eng_comp.adicionaAresta("a46","Métodos Numéricos","Controle e Automação I")
eng_comp.adicionaAresta("a47","Circuitos Eletro-Eletrônicos","Controle e Automação I")
eng_comp.adicionaAresta("a48","Projeto em Engenharia de Computação I","Projeto em Engenharia de Computação II")
print(eng_comp.topologicalSort())

const_edificios = MeuGrafo(['Informática Básica','Inglês Instrumental','Português Instrumental','Química Aplicada',
'Cálculo Diferencial e Integral I','Álgebra Vetorial e Geometria Analítica', 'Desenho Técnico','Introdução a Construção Edifícios',
'Física I','Metodologia da Pesquisa Científica','Materiais de Construção I','Des. Assist. por Computador I','Cálculo Diferencial e Integral II',
'Topografia I','Desenho e Projeto Arquitetônico', 'Matemática Financeira Aplicada','Resistência dos Materiais','Física II','Estatística Aplicada',
'Técnicas Construtivas I','Topografia II','Materiais de Construção II','Des. Assist. por Computador II','Instalações Hidrossanitárias',
'Instalações Elétricas Pred.','Especificações e Orcamentos I','Segurança do Trabalho','Técnicas Construtivas II',' Estruturas de Concreto I',
'Mecânica dos Solos','Patologia das Construções','Manutenção Predial','Estruturas Metálicas','Fundações e Sistemas de Contenção',
'Estruturas de Madeira','Estruturas de Concreto II','Especificações e Orcamentos II','Instalações Especiais',
'Formação do Empreendedor','Planej.Gestão e Controle de Obra','Legislação Aplicada','Avaliação Pós-ocupação','Gestão da Qualidade e Produtividade',
'Gestão Ambiental','Administração de Custos','Relações Humanas no Trabalho','Trabalho de Conclusão de Curso','Estágio Supervisionado','Libras (optativa)'])

const_edificios.adicionaAresta("a1","Cálculo Diferencial e Integral I","Física I")
const_edificios.adicionaAresta("a2","Química Aplicada","Materiais de Construção I")
const_edificios.adicionaAresta("a3","Informática Básica","Des. Assist. por Computador I")
const_edificios.adicionaAresta("a4","Desenho Técnico","Des. Assist. por Computador I")
const_edificios.adicionaAresta("a5","Cálculo Diferencial e Integral I","Cálculo Diferencial e Integral II")
const_edificios.adicionaAresta("a6","Desenho Técnico","Topografia I")
const_edificios.adicionaAresta("a7","Desenho Técnico","Desenho e Projeto Arquitetônico")
const_edificios.adicionaAresta("a8","Cálculo Diferencial e Integral I","Resistência dos Materiais")
const_edificios.adicionaAresta("a9","Física I","Resistência dos Materiais")
const_edificios.adicionaAresta("a10","Física I","Física II")
const_edificios.adicionaAresta("a11","Cálculo Diferencial e Integral II","Física II")
const_edificios.adicionaAresta("a12","Cálculo Diferencial e Integral I","Estatística Aplicada")
const_edificios.adicionaAresta("a13","Informática Básica","Técnicas Construtivas I")
const_edificios.adicionaAresta("a14","Desenho e Projeto Arquitetônico","Técnicas Construtivas I")
const_edificios.adicionaAresta("a15","Topografia I","Topografia II")
const_edificios.adicionaAresta("a16","Materiais de Construção I","Materiais de Construção II")
const_edificios.adicionaAresta("a17","Des. Assist. por Computador I","Des. Assist. por Computador II")
const_edificios.adicionaAresta("a18","Desenho Técnico","Instalações Hidrossanitárias")
const_edificios.adicionaAresta("a19","Física I","Instalações Hidrossanitárias")
const_edificios.adicionaAresta("a20","Desenho Técnico","Instalações Elétricas Pred.")
const_edificios.adicionaAresta("a21","Física I","Instalações Elétricas Pred.")
const_edificios.adicionaAresta("a22","Materiais de Construção I","Especificações e Orcamentos I")
const_edificios.adicionaAresta("a23","Des. Assist. por Computador I","Segurança do Trabalho") #44
print(const_edificios.topologicalSort())
unittest.main()