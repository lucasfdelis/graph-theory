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
'Cálculo Diferencial e Integral I','Álgebra Vetorial e Geometria Analítica','Desenho Técnico','Introdução a Construção Edifícios',
'Física I','Metodologia da Pesquisa Científica','Materiais de Construção I','Des. Assist. por Computador I','Cálculo Diferencial e Integral II',
'Topografia I','Desenho e Projeto Arquitetônico','Matemática Financeira Aplicada','Resistência dos Materiais','Física II','Estatística Aplicada',
'Técnicas Construtivas I','Topografia II','Materiais de Construção II','Des. Assist. por Computador II','Instalações Hidrossanitárias',
'Instalações Elétricas Pred.','Especificações e Orcamentos I','Segurança do Trabalho','Técnicas Construtivas II','Estruturas de Concreto I',
'Mecânica dos Solos','Patologia das Construções','Manutenção Predial','Estruturas Metálicas','Fundações e Sistemas de Contenção',
'Estruturas de Madeira','Estruturas de Concreto II','Especificações e Orcamentos II','Instalações Especiais',
'Formação do Empreendedor','Planej. Gestão e Controle de Obra','Legislação Aplicada','Avaliação Pós-ocupação','Gestão da Qualidade e Produtividade',
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
const_edificios.adicionaAresta("a23","Topografia II","Técnicas Construtivas II")
const_edificios.adicionaAresta("a24","Materiais de Construção II","Técnicas Construtivas II")
const_edificios.adicionaAresta("a25","Desenho Técnico","Estruturas de Concreto I")
const_edificios.adicionaAresta("a26","Resistência dos Materiais","Estruturas de Concreto I")
const_edificios.adicionaAresta("a27","Informática Básica","Mecânica dos Solos")
const_edificios.adicionaAresta("a28","Materiais de Construção II","Mecânica dos Solos")
const_edificios.adicionaAresta("a29","Materiais de Construção II","Patologia das Construções")
const_edificios.adicionaAresta("a30","Especificações e Orcamentos I","Patologia das Construções")
const_edificios.adicionaAresta("a31","Técnicas Construtivas II","Patologia das Construções")
const_edificios.adicionaAresta("a32","Estruturas de Concreto I","Patologia das Construções")
const_edificios.adicionaAresta("a33","Instalações Hidrossanitárias","Manutenção Predial")
const_edificios.adicionaAresta("a34","Instalações Elétricas Pred.","Manutenção Predial")
const_edificios.adicionaAresta("a35","Técnicas Construtivas II","Manutenção Predial")
const_edificios.adicionaAresta("a36","Estruturas de Concreto I","Manutenção Predial")
const_edificios.adicionaAresta("a37","Desenho Técnico","Estruturas Metálicas")
const_edificios.adicionaAresta("a38","Resistência dos Materiais","Estruturas Metálicas")
const_edificios.adicionaAresta("a39","Mecânica dos Solos","Fundações e Sistemas de Contenção")
const_edificios.adicionaAresta("a40","Desenho Técnico","Estruturas de Madeira")
const_edificios.adicionaAresta("a41","Resistência dos Materiais","Estruturas de Madeira")
const_edificios.adicionaAresta("a42","Estruturas de Concreto I","Estruturas de Concreto II")
const_edificios.adicionaAresta("a43","Especificações e Orcamentos I","Especificações e Orcamentos II")
const_edificios.adicionaAresta("a44","Matemática Financeira Aplicada","Planej. Gestão e Controle de Obra")
const_edificios.adicionaAresta("a45","Segurança do Trabalho","Planej. Gestão e Controle de Obra")
const_edificios.adicionaAresta("a46","Metodologia da Pesquisa Científica","Avaliação Pós-ocupação")
const_edificios.adicionaAresta("a47","Desenho e Projeto Arquitetônico","Avaliação Pós-ocupação")
const_edificios.adicionaAresta("a48","Física II","Avaliação Pós-ocupação")
const_edificios.adicionaAresta("a49","Topografia II","Avaliação Pós-ocupação")
const_edificios.adicionaAresta("a50","Mecânica dos Solos","Gestão da Qualidade e Produtividade")
const_edificios.adicionaAresta("a51","Metodologia da Pesquisa Científica","Gestão Ambiental")
const_edificios.adicionaAresta("a52","Matemática Financeira Aplicada","Administração de Custos")
print(const_edificios.topologicalSort())

fisica = MeuGrafo(['Introdução à Física','Pré-Cálculo','Psicologia da Aprendizagem','Álgebra Vetorial e Geometria Analítica','Língua Portuguesa I',
'Metodologia do Trabalho Científico','História da Educação','Física Básica I','Física Experimental I','Cálculo Diferencial e Integral I',
'Álgebra Linear','Língua Portuguesa II','Inglês Instrumental','Filosofia da Educação','Física Básica II','Física Experimental II','Cálculo Diferencial e Integral II',
'Química Geral','Sociologia da Educação','Educação em Direitos Humanos','Educação Ambiental e Sustentabilidade','Física Básica III','Física Experimental III',
'Didática Geral','Políticas e Gestão Educacional','Cálculo Diferencial e Integral III','Computação Aplicada à Física','Física Básica IV','Física Experimental IV',
'Física Matemática I','Termodinâmica','Didática Aplicada ao Ensino de Física','Prática de Ensino I','Estágio Supervisionado I','Física Moderna',
'Física Moderna Experimental','Mecânica Analítica','Evolução do Pensamento Científico','Educação em Diversidade','Prática de Ensino II','Estágio Supervisionado II',
'Mecânica Quântica','Eletromagnetismo','Prática de Ensino III','Prática de Lab. e Inst. para o Ens. de Fís. I','Optativa','Estágio Supervisionado III',
'Libras','Prática de Lab. e Inst. para o Ens. de Fís. II','Prática de Ensino IV','Mecânica Estatística','TCC','Optativa','Estágio Supervisionado IV'])

fisica.adicionaAresta("a1","Introdução à Física","Física Básica I")
fisica.adicionaAresta("a2","Pré-Cálculo","Física Básica I")
fisica.adicionaAresta("a3","Introdução à Física","Física Experimental I")
fisica.adicionaAresta("a4","Pré-Cálculo","Física Experimental I")
fisica.adicionaAresta("a5","Pré-Cálculo","Cálculo Diferencial e Integral I")
fisica.adicionaAresta("a6","Pré-Cálculo","Álgebra Linear")
fisica.adicionaAresta("a7","Álgebra Vetorial e Geometria Analítica","Álgebra Linear")
fisica.adicionaAresta("a8","Língua Portuguesa I","Língua Portuguesa II")
fisica.adicionaAresta("a9","Física Básica I","Física Básica II")
fisica.adicionaAresta("a10","Cálculo Diferencial e Integral I","Física Básica II")
fisica.adicionaAresta("a11","Física Básica I","Física Experimental II")
fisica.adicionaAresta("a12","Física Experimental I","Física Experimental II")
fisica.adicionaAresta("a13","Cálculo Diferencial e Integral I","Cálculo Diferencial e Integral II")
fisica.adicionaAresta("a14","Física Básica I","Física Básica III")
fisica.adicionaAresta("a15","Física Básica II","Física Experimental III")
fisica.adicionaAresta("a16","Física Experimental II","Física Experimental III")
fisica.adicionaAresta("a17","Cálculo Diferencial e Integral I","Cálculo Diferencial e Integral III")
fisica.adicionaAresta("a18","Física Básica II","Computação Aplicada à Física")
fisica.adicionaAresta("a19","Física Básica III","Física Básica IV")
fisica.adicionaAresta("a20","Cálculo Diferencial e Integral III","Física Básica IV")
fisica.adicionaAresta("a21","Física Básica III","Física Experimental IV")
fisica.adicionaAresta("a22","Física Experimental III","Física Experimental IV")
fisica.adicionaAresta("a23","Cálculo Diferencial e Integral III","Física Matemática I")
fisica.adicionaAresta("a24","Física Básica II","Termodinâmica")
fisica.adicionaAresta("a25","Didática Geral","Didática Aplicada ao Ensino de Física")
fisica.adicionaAresta("a26","Física Básica I","Estágio Supervisionado I")
fisica.adicionaAresta("a27","Didática Geral","Estágio Supervisionado I")
fisica.adicionaAresta("a28","Física Moderna","Física Moderna")
fisica.adicionaAresta("a29","Física Básica IV","Física Moderna Experimental")
fisica.adicionaAresta("a30","Física Experimental IV","Física Moderna Experimental")
fisica.adicionaAresta("a31","Física Básica I","Mecânica Analítica")
fisica.adicionaAresta("a32","Física Matemática I","Mecânica Analítica")
fisica.adicionaAresta("a33","Física Básica IV","Evolução do Pensamento Científico")
fisica.adicionaAresta("a34","Prática de Ensino I","Prática de Ensino II")
fisica.adicionaAresta("a35","Física Básica II","Estágio Supervisionado II")
fisica.adicionaAresta("a36","Estágio Supervisionado I","Estágio Supervisionado II")
fisica.adicionaAresta("a37","Física Moderna","Mecânica Quântica")
fisica.adicionaAresta("a38","Física Básica III","Eletromagnetismo")
fisica.adicionaAresta("a39","Cálculo Diferencial e Integral III","Eletromagnetismo")
fisica.adicionaAresta("a40","Prática de Ensino II","Prática de Ensino III")
fisica.adicionaAresta("a41","Física Básica II","Prática de Lab. e Inst. para o Ens. de Fís. I")
fisica.adicionaAresta("a42","Didática Geral","Prática de Lab. e Inst. para o Ens. de Fís. I")
fisica.adicionaAresta("a43","Física Básica III","Estágio Supervisionado III")
fisica.adicionaAresta("a44","Estágio Supervisionado II","Estágio Supervisionado III")
fisica.adicionaAresta("a45","Educação em Diversidade","Libras")
fisica.adicionaAresta("a46","Prática de Lab. e Inst. para o Ens. de Fís. I","Prática de Lab. e Inst. para o Ens. de Fís. II")
fisica.adicionaAresta("a47","Prática de Ensino III","Prática de Ensino IV")
fisica.adicionaAresta("a48","Termodinâmica","Mecânica Estatística")
fisica.adicionaAresta("a49","Mecânica Quântica","Mecânica Estatística")
fisica.adicionaAresta("a50","Metodologia do Trabalho Científico","TCC")
fisica.adicionaAresta("a51","Língua Portuguesa II","TCC")
fisica.adicionaAresta("a52","Física Básica IV","Estágio Supervisionado IV")
fisica.adicionaAresta("a53","Estágio Supervisionado III","Estágio Supervisionado IV")
print(fisica.topologicalSort())
unittest.main()
