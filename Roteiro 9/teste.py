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
print("")

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
print("")

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
fisica.adicionaAresta("a14","Física Básica II","Física Básica III")
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
print("")

matematica = MeuGrafo(['Matemática para o Ensino Médio 1','Matemática para o Ensino Fundamental','Trigonometria','História da Educação',
'Psicologia da Aprendizagem','Língua Portuguesa 1','Inglês Instrumental','Matemática para o Ensino Médio 2','Cálculo 1','Álgebra Vetorial e Geometria Analítica',
'Epistemologia da Matemática','Filosofia da Educação','Língua Portuguesa 2','Educação em Diversidade','Matemática para o Ensino Médio 3','Cálculo 2',
'Argumentação Matemática','Prática de Laboratório de Ensino de Matemática 1','Sociologia da Educação','Didática Geral','Álgebra Linear 1','Cálculo 3',
'Didática da Matemática','Prática de Laboratório de Ensino de Matemática 2','Libras 1','Metodologia do Trabalho Científico','Introdução a Teoria dos Números',
'Desenho Geométrico','Física Básica 1','Prática de Ensino de Matemática 1','Introdução à Programação','Gestão Educacional e Planejamento',
'Estágio Supervisionado 1','Estruturas Algébricas 1','Geometria Euclidiana Plana','Estatística e Probabilidade','Prática de Ensino de Matemática 2',
'Pesquisa Aplicada em Matemática 1','Educação em Direitos Humanos','Estágio Supervisionado 2','Análise Real 1','Matemática Financeira 1',
'Equações Diferenciais Ordinárias','Prática de Ensino de Matemática 3','Pesquisa Aplicada em Matemática 2','Optativa 1','Estágio Supervisionado 3',
'Geometria Euclidiana Espacial','TCC','História da Matemática','Prática de Ensino de Matemática 4','Educação Ambiental e Sustentabilidade','Optativa 2',
'Estágio Supervisionado 4'])

matematica.adicionaAresta("a1","Matemática para o Ensino Médio 1","Matemática para o Ensino Médio 2")
matematica.adicionaAresta("a2","Matemática para o Ensino Médio 1","Cálculo 1")
matematica.adicionaAresta("a3","Trigonometria","Cálculo 1")
matematica.adicionaAresta("a4","Língua Portuguesa 1","Língua Portuguesa 2")
matematica.adicionaAresta("a5","Matemática para o Ensino Médio 2","Matemática para o Ensino Médio 3")
matematica.adicionaAresta("a6","Cálculo 1","Cálculo 2")
matematica.adicionaAresta("a7","Matemática para o Ensino Fundamental","Argumentação Matemática")
matematica.adicionaAresta("a8","Matemática para o Ensino Fundamental","Prática de Laboratório de Ensino de Matemática 1")
matematica.adicionaAresta("a9","Matemática para o Ensino Médio 2","Álgebra Linear 1")
matematica.adicionaAresta("a10","Álgebra Vetorial e Geometria Analítica","Álgebra Linear 1")
matematica.adicionaAresta("a11","Álgebra Vetorial e Geometria Analítica","Cálculo 3")
matematica.adicionaAresta("a12","Cálculo 2","Cálculo 3")
matematica.adicionaAresta("a13","Didática Geral","Didática da Matemática")
matematica.adicionaAresta("a14","Prática de Laboratório de Ensino de Matemática 1","Prática de Laboratório de Ensino de Matemática 2")
matematica.adicionaAresta("a15","Educação em Diversidade","Libras 1")
matematica.adicionaAresta("a16","Argumentação Matemática","Introdução a Teoria dos Números")
matematica.adicionaAresta("a17","Matemática para o Ensino Fundamental","Desenho Geométrico")
matematica.adicionaAresta("a18","Cálculo 2","Física Básica 1")
matematica.adicionaAresta("a19","Prática de Laboratório de Ensino de Matemática 2","Prática de Ensino de Matemática 1")
matematica.adicionaAresta("a20","Prática de Laboratório de Ensino de Matemática 2","Introdução à Programação")
matematica.adicionaAresta("a21","Prática de Laboratório de Ensino de Matemática 2","Estágio Supervisionado 1")
matematica.adicionaAresta("a22","Introdução a Teoria dos Números","Estruturas Algébricas 1")
matematica.adicionaAresta("a23","Desenho Geométrico","Geometria Euclidiana Plana")
matematica.adicionaAresta("a24","Cálculo 2","Estatística e Probabilidade")
matematica.adicionaAresta("a25","Prática de Ensino de Matemática 1","Prática de Ensino de Matemática 2")
matematica.adicionaAresta("a26","Metodologia do Trabalho Científico","Pesquisa Aplicada em Matemática 1")
matematica.adicionaAresta("a27","Estágio Supervisionado 1","Estágio Supervisionado 2")
matematica.adicionaAresta("a28","Cálculo 3","Análise Real 1")
matematica.adicionaAresta("a29","Cálculo 1","Matemática Financeira 1")
matematica.adicionaAresta("a30","Álgebra Linear 1","Equações Diferenciais Ordinárias")
matematica.adicionaAresta("a31","Cálculo 3","Equações Diferenciais Ordinárias")
matematica.adicionaAresta("a32","Prática de Ensino de Matemática 2","Prática de Ensino de Matemática 3")
matematica.adicionaAresta("a33","Pesquisa Aplicada em Matemática 1","Pesquisa Aplicada em Matemática 2")
matematica.adicionaAresta("a34","Estágio Supervisionado 2","Estágio Supervisionado 3")
matematica.adicionaAresta("a35","Geometria Euclidiana Plana","Geometria Euclidiana Espacial")
matematica.adicionaAresta("a36","Pesquisa Aplicada em Matemática 2","TCC")
matematica.adicionaAresta("a37","Cálculo 2","História da Matemática")
matematica.adicionaAresta("a38","Prática de Ensino de Matemática 3","Prática de Ensino de Matemática 4")
matematica.adicionaAresta("a39","Estágio Supervisionado 3","Estágio Supervisionado 4")
print(matematica.topologicalSort())
print("")

letras = MeuGrafo(['Introdução aos Estudos Literários','Introdução à Linguistica','Leitura e Produção de Texto I','Informática Básica','Fundamentos da Educação a Distância',
'Inglês Instrumental','História da Educação Brasileira','Teoria Literária I','Literatura e Ensino','Morfologia da Língua Portuguesa','Fundamentos da Linguística Românica',
'Linguística I','Filosofia da Educação','Metodologia da Pesquisa Científica','Teoria Literária II','Literatura Brasileira I','Literatura Portuguesa I',
'História da Língua Portuguesa','Linguística II','Psicologia da Aprendizagem','Seminário de Pesquisa Interdisciplinar I','Literatura Brasileira II',
'Literatura Portuguesa II','Fonética e Fonologia da Língua Portuguesa','Aquisição da Linguagem','Didática','Morfossintaxe','Seminário de Pesquisa Interdisciplinar II',
'Literatura Brasileira III','Semântica da Lingua Portuguesa','Leitura e Produção de Texto II','Orientação de Estágio Supervisionado I','Metodologia do Ensino de Língua Portuguesa',
'Metodologia do Ensino de Literatura','Seminário de Pesquisa Interdisciplinar III','Literatura Brasileira IV','Literaturas Africanas de Língua Portuguesa',
'Sociolinguística','Orientação de Estágio Supervisionado II','Língua Brasileira de Sinais (LIBRAS)','Educação Inclusiva','Seminário de Pesquisa Interdisciplinar IV',
'Estágio Supervisionado I','Literatura Brasileira V','Literatura Infantil e juvenil','Literatura e Cultura Popular','Orientação de Estágio Supervisionado III',
'Pragmática','Estrutura e Funcionamento da Educ. Básica','Orientação de TCC I','Estágio Supervisionado II','Língua Portuguesa como segunda língua para surdos (Optativa)',
'Gestão Educacional','Tópicos em Projetos Especiais','Sociologia da Educação','Orientação de Estágio Supervisionado IV','Educação e Direitos Humanos',
'Educação Ambiental e Interdisciplinaridade','Orientação de TCC II','Estágio Supervisionado III'])

letras.adicionaAresta("a1","Introdução aos Estudos Literários","Teoria Literária I")
letras.adicionaAresta("a2","Introdução aos Estudos Literários","Literatura e Ensino")
letras.adicionaAresta("a3","Introdução à Linguistica","Morfologia da Língua Portuguesa")
letras.adicionaAresta("a4","Introdução à Linguistica","Linguística I")
letras.adicionaAresta("a5","História da Educação Brasileira","Filosofia da Educação")
letras.adicionaAresta("a6","Teoria Literária I","Teoria Literária II")
letras.adicionaAresta("a7","Teoria Literária I","Literatura Brasileira I")
letras.adicionaAresta("a8","Teoria Literária I","Literatura Portuguesa I")
letras.adicionaAresta("a9","Fundamentos da Linguística Românica","História da Língua Portuguesa")
letras.adicionaAresta("a10","Linguística I","Linguística II")
letras.adicionaAresta("a11","Teoria Literária II","Literatura Brasileira II")
letras.adicionaAresta("a12","Literatura Portuguesa I","Literatura Portuguesa II")
letras.adicionaAresta("a13","Linguística I","Fonética e Fonologia da Língua Portuguesa")
letras.adicionaAresta("a14","Linguística I","Aquisição da Linguagem")
letras.adicionaAresta("a15","Psicologia da Aprendizagem","Aquisição da Linguagem")
letras.adicionaAresta("a16","Morfologia da Língua Portuguesa","Morfossintaxe")
letras.adicionaAresta("a17","Linguística II","Morfossintaxe")
letras.adicionaAresta("a18","Seminário de Pesquisa Interdisciplinar I","Seminário de Pesquisa Interdisciplinar II")
letras.adicionaAresta("a19","Teoria Literária II","Literatura Brasileira III")
letras.adicionaAresta("a20","Linguística II","Semântica da Lingua Portuguesa")
letras.adicionaAresta("a21","Leitura e Produção de Texto I","Leitura e Produção de Texto II")
letras.adicionaAresta("a22","Didática","Orientação de Estágio Supervisionado I")
letras.adicionaAresta("a23","Linguística II","Metodologia do Ensino de Língua Portuguesa")
letras.adicionaAresta("a24","Literatura e Ensino","Metodologia do Ensino de Literatura")
letras.adicionaAresta("a25","Seminário de Pesquisa Interdisciplinar I","Seminário de Pesquisa Interdisciplinar III")
letras.adicionaAresta("a26","Teoria Literária II","Literatura Brasileira IV")
letras.adicionaAresta("a27","Teoria Literária II","Literaturas Africanas de Língua Portuguesa")
letras.adicionaAresta("a28","Linguística II","Sociolinguística")
letras.adicionaAresta("a29","Orientação de Estágio Supervisionado I","Orientação de Estágio Supervisionado II")
letras.adicionaAresta("a30","Seminário de Pesquisa Interdisciplinar I","Seminário de Pesquisa Interdisciplinar IV")
letras.adicionaAresta("a31","Orientação de Estágio Supervisionado I","Estágio Supervisionado I")
letras.adicionaAresta("a32","Teoria Literária II","Literatura Brasileira V")
letras.adicionaAresta("a33","Teoria Literária II","Literatura Infantil e juvenil")
letras.adicionaAresta("a34","Teoria Literária II","Literatura e Cultura Popular")
letras.adicionaAresta("a35","Orientação de Estágio Supervisionado II","Orientação de Estágio Supervisionado III")
letras.adicionaAresta("a36","Linguística II","Pragmática")
letras.adicionaAresta("a37","Didática","Estrutura e Funcionamento da Educ. Básica")
letras.adicionaAresta("a38","Metodologia da Pesquisa Científica","Orientação de TCC I")
letras.adicionaAresta("a39","Leitura e Produção de Texto II","Orientação de TCC I")
letras.adicionaAresta("a40","Orientação de Estágio Supervisionado II","Estágio Supervisionado II")
letras.adicionaAresta("a41","Estágio Supervisionado I","Estágio Supervisionado II")
letras.adicionaAresta("a42","Língua Brasileira de Sinais (LIBRAS)","Língua Portuguesa como segunda língua para surdos (Optativa)")
letras.adicionaAresta("a43","História da Educação Brasileira","Sociologia da Educação")
letras.adicionaAresta("a44","Orientação de Estágio Supervisionado III","Orientação de Estágio Supervisionado IV")
letras.adicionaAresta("a45","Orientação de TCC I","Orientação de TCC II")
letras.adicionaAresta("a46","Orientação de Estágio Supervisionado III","Estágio Supervisionado III")
letras.adicionaAresta("a47","Estágio Supervisionado II","Estágio Supervisionado III")
print(letras.topologicalSort())
print("")

telematica = MeuGrafo(['Introdução à Telemática','Fundamentos de Eletricidade','Programação I','Lab. de Sist. Abertos',
'Inglês Instrumental','Pré-cálculo','Língua Portuguesa','Redes de Computadores','Eletrônica para Telecomunicações',
'Medição Eletroeletrônica','Programação II','Arquitetura de Computadores','Cálculo Diferencial e Integral',
'Educação em Diversidade','Tecnologias de Redes Locais','Estatística Aplicada à Telemática','Sinais e Sistemas',
'Administração de Sistemas','Sistemas Operacionais','Programação III','Metodologia da Pesquisa Científica',
'Interconexão de Redes','Cabeamento Estruturado','Teoria da Informação e Codificação','Sistemas de Comunicações',
'Processamento Digital de Sinais','Administração de Serviços','Educação Ambiental e Sustentabilidade','Redes de Longa Distância',
'Segurança de Redes de Computadores','Comunicações Sem Fio','Comunicações Ópticas','Projeto em Telemática','Formação do Empreendedor',
'Optativa I','Projeto de Redes de Computadores','Sistemas Telefônicos','Educação em Direitos Humanos','Relações Humanas no Trabalho',
'Ética','Optativa II','Trabalho de Conclusão de Curso (Obrigatória)','Estágio Supervisionado (Optativa)'])

telematica.adicionaAresta("a1","Introdução à Telemática","Redes de Computadores")
telematica.adicionaAresta("a2","Fundamentos de Eletricidade","Eletrônica para Telecomunicações")
telematica.adicionaAresta("a3","Pré-cálculo","Eletrônica para Telecomunicações")
telematica.adicionaAresta("a4","Fundamentos de Eletricidade","Medição Eletroeletrônica")
telematica.adicionaAresta("a5","Pré-cálculo","Medição Eletroeletrônica")
telematica.adicionaAresta("a6","Programação I","Programação II")
telematica.adicionaAresta("a7","Pré-cálculo","Cálculo Diferencial e Integral")
telematica.adicionaAresta("a8","Redes de Computadores","Tecnologias de Redes Locais")
telematica.adicionaAresta("a9","Cálculo Diferencial e Integral","Estatística Aplicada à Telemática")
telematica.adicionaAresta("a10","Eletrônica para Telecomunicações","Sinais e Sistemas")
telematica.adicionaAresta("a11","Medição Eletroeletrônica","Sinais e Sistemas")
telematica.adicionaAresta("a12","Cálculo Diferencial e Integral","Sinais e Sistemas")
telematica.adicionaAresta("a13","Lab. de Sist. Abertos","Administração de Sistemas")
telematica.adicionaAresta("a14","Arquitetura de Computadores","Sistemas Operacionais")
telematica.adicionaAresta("a15","Redes de Computadores","Programação III")
telematica.adicionaAresta("a16","Programação II","Programação III")
telematica.adicionaAresta("a17","Tecnologias de Redes Locais","Interconexão de Redes")
telematica.adicionaAresta("a18","Tecnologias de Redes Locais","Cabeamento Estruturado")
telematica.adicionaAresta("a19","Estatística Aplicada à Telemática","Teoria da Informação e Codificação")
telematica.adicionaAresta("a20","Estatística Aplicada à Telemática","Sistemas de Comunicações")
telematica.adicionaAresta("a21","Sinais e Sistemas","Sistemas de Comunicações")
telematica.adicionaAresta("a22","Sinais e Sistemas","Processamento Digital de Sinais")
telematica.adicionaAresta("a23","Redes de Computadores","Administração de Serviços")
telematica.adicionaAresta("a24","Administração de Sistemas","Administração de Serviços")
telematica.adicionaAresta("a25","Interconexão de Redes","Redes de Longa Distância")
telematica.adicionaAresta("a26","Interconexão de Redes","Segurança de Redes de Computadores")
telematica.adicionaAresta("a27","Sistemas de Comunicações","Comunicações Sem Fio")
telematica.adicionaAresta("a28","Sistemas de Comunicações","Comunicações Ópticas")
telematica.adicionaAresta("a29","Metodologia da Pesquisa Científica","Projeto em Telemática")
telematica.adicionaAresta("a30","Interconexão de Redes","Projeto em Telemática")
telematica.adicionaAresta("a31","Sistemas de Comunicações","Projeto em Telemática")
telematica.adicionaAresta("a32","Cabeamento Estruturado","Projeto de Redes de Computadores")
telematica.adicionaAresta("a33","Redes de Longa Distância","Projeto de Redes de Computadores")
telematica.adicionaAresta("a34","Comunicações Sem Fio","Sistemas Telefônicos")
telematica.adicionaAresta("a35","Projeto em Telemática","Trabalho de Conclusão de Curso (Obrigatória)")
telematica.adicionaAresta("a36","Metodologia da Pesquisa Científica","Estágio Supervisionado (Optativa)")
telematica.adicionaAresta("a37","Interconexão de Redes","Estágio Supervisionado (Optativa)")
telematica.adicionaAresta("a38","Sistemas de Comunicações","Estágio Supervisionado (Optativa)")
print(telematica.topologicalSort())

unittest.main()
