

Universidade Federal do Tocantins
Campus Universitário de Palmas
Programa de Graduação em Ciência da Computação


DAVID XAVIER BRITO
PROBLEMA DO CAVALO OU PASSEIO DE CAVALO




Universidade Federal do Tocantins
Campus Universitário de Palmas
Programa de Graduação em Ciência da Computação


DAVID XAVIER BRITO
PROBLEMA DO CAVALO OU PASSEIO DE CAVALO
Problema do cavalo é um problema matemático envolvendo o movimento da peça do cavalo no tabuleiro de xadrez. O cavalo é colocado no tabuleiro vazio e, seguindo as regras do jogo, precisa passar por todas as casas exatamente uma vez em movimentos consecutivos, neste artigo é apresentado uma solução simples de tal situação.

Orientador: Prof. Glenda Michele Botelho








RESUMO

Algoritmos Genéticos são inspirados no princípio Darwiniano da evolução das espécies e na genética, São algoritmos probabilísticos que fornecem um mecanismo de busca paralela e adaptativa baseado no princípio de sobrevivência dos mais aptos e na reprodução. Este artigo introduz a técnica computacional inteligente, aplicando o conceito dos Algoritmos Genéticos no  problema do cavalo, ou passeio do cavalo, é um problema matemático envolvendo o movimento da peça do cavalo no tabuleiro de xadrez. O cavalo é colocado no tabuleiro vazio e, seguindo as regras do jogo, precisa passar por todas as casas exatamente uma vez em movimentos consecutivos.

Palavras-chave: Algoritmos Genéticos, cavalo,problema do cavalo, ou passeio do cavalo.
ABSTRACT

Genetic Algorithms are inspired by the Darwinian domain of evolution and genetics. They are probabilistic algorithms that are a parallel and adaptive search mechanism based on the survival principle of the fittest and reproduction. This article introduces an intelligent computational technique, applying the concept of Genetic Algorithms in the problem, or horse horse, is a mathematical problem. The game is placed on the empty board, following the rules of the game, must pass through all the houses exactly once in consecutive movement.
.

Keywords: Genetic Algorithms, horse, horse problem, or horse ride.

SUMÁRIO
1	INTRODUÇÃO	6
2	MÉTODOS	8
3	RESULTADOS	13
3.1	Melhores e piores  indivíduos	13
3.2	Tabelas	13
3.3	Outros Resultados	15
4	CONCLUSÕES	16
5	Referências	17
	





1 INTRODUÇÃO
Um passeio do cavalo é uma sequência formada pelas casas de um tabuleiro de xadrez onde cada casa aparece exatamente uma vez, e em que duas casas consecutivas, na sequência, estão afastadas uma da outra, no tabuleiro, duas unidades em uma dimensão e uma unidade na outra dimensão. Em outras palavras, trata-se de um percurso que poderia fazer o cavalo do jogo de xadrez, com seu movimento típico em forma de L, passando por todas as casas do tabuleiro, sem jamais passar duas vezes pela mesma casa. 
O problema de se decidir a existência de um passeio do cavalo é caso particular do problema do caminho hamiltoniano que é NP-completo para grafos gerais  em um grafo cujos vértices são as casas do tabuleiro, e cujas arestas ligam casas separadas por um movimento válido do cavalo. Leonhard Euler foi um dos primeiros  e certamente o mais proeminente estudiosos a investigar o problema do passeio do cavalo (Euler, 1759).
 Diversas variantes do problema foram consideradas desde então. Na versão fechada, exige-se que a primeira e a última casa do passeio também estejam separadas por um movimento do cavalo, isto é, que o cavalo consiga retornar a sua casa inicial em um único movimento após visitar todas as demais casas do tabuleiro. 
Na versão aberta, inexiste tal exigência. Embora a formulação inicial do problema tenha provavelmente empregado um tabuleiro de xadrez tradicional, de tamanho 8 × 8, há muito que outros tipos de tabuleiro foram considerados: tabuleiros n × n (íntegros ou com casas removidas) para valores arbitrários de n (Parberry, 1997), retangulares n× m (Cull and DeCurtins, 1978), tabuleiros tridimensionais e multidimensionais (Erde et al., 2012; Kumar, 2012), tabuleiros imersos em superficies esféricas (Cairns,2002), tóricas (Watkins, 1997) etc.
Passeio do Cavalo consiste em codificar um algoritmo que encontre um caminho em um tabuleiro de xadrez pelo qual a peça do Cavalo passe por todas as suas casas, passando apenas uma única vez por cada uma delas. No xadrez, o Cavalo faz um movimento em L a partir de sua posição inicial, pulando sobre quaisquer outras pessoas até o final do movimento.Uma das maneira recorrente para a solução do problema do Cavalo é a utilização de algoritmos de força bruta. Existem aproximadamente 4x1051 sequências de movimentos possíveis em um tabuleiro 8x8, porém esses algoritmos tornam-se ineficientes à medida que o tamanho do tabuleiro aumenta.
Para tentar resolver o problema, foi implementado um Algoritmo Genético contemplando as operações de seleção, pareamento, crossover e mutação através de uma Função Objetivo a fim de gerar populações até encontrar uma solução adequada. Execuções do algoritmo foram realizadas para diversos tamanhos de tabuleiros, cujos resultados foram posteriormente analisados e serão apresentados a seguir.











2  Métodos 
O Algoritmo construído para representação representação e solução do problema, possui três parâmetro,  número de gerações "NUM GENERATIONS"(determina a quantidade de vezes que o algoritmo será executado), o tamanho da população "POPULATION SIZE" (número de indivíduos a cada população) e o tamanho do tabuleiro "TABLE_SIZE", que são constituídos por:

Cada indivíduo possui os seguintes atributos:
	moves: a quantidade de movimentos realizada até o momento;
	path: o caminho do indivíduo pelo tabuleiro;
	table: cria um tabuleiro de prioridade de movimentos;
	position: sua posição inicial;
	table[x][y]: sua tabela de posições visitadas no tabuleiro.




Um dos principais atributos do indivíduo é seu tabuleiro de prioridade de movimentos. Cada indivíduo possui um tabuleiro com tamanho equivalente ao tabuleiro do problema, onde cada casa possui um valor de prioridade randômico definido entre 0 e 10.

 Para escolher qual será sua próxima casa a ser visitada, o indivíduo seleciona primeiramente aquelas cujo movimento é válido (ou seja, correspondem ao L do Cavalo), e posteriormente a casa de maior prioridade analisada primeiro. Ambas decisões são realizadas através dos métodos nextMoves e getBestMove, respectivamente.

nextMoves: responsável por gerar melhor caminho.

getBestMove: analisar qual a casa de maior prioridade dentre as selecionadas previamente.


Após getBestMove ser selecionada, e a quantidade de movimentos moves é incrementada em 1.



o método play, e executado até o indivíduo caso não for  obtido nenhum movimento possível em sua lista de nextMoves, para a incrementar moves. Entretanto, esse processo é influenciado pelas operações inerentes aos Algoritmos Genéticos: seleção, pareamento, crossover e mutação.

Com o processo de decisão de movimentos codificado é definidos, é possível iniciar, a implementação do Algoritmo Genético para a resolução do problema do cavalo. Para exemplificar como foi realizada sua codificação, será descrito todo o processo de uma iteração do algoritmo para uma população de tamanho 30.


Inicialmente, 30 indivíduos são gerados, cada um com um tabuleiro de prioridades gerado de maneira aleatória. Cada indivíduo executa um jogo através do método play, e, ao final de cada jogo, o número de movimentos alcançados é armazenado na variável moves de cada um deles, como foi mostrado anteriormente.
A operação de seleção é implementada no método getBestGame e verificará qual indivíduo possui o maior valor de moves dentre os 30. Ou seja, a Função Objetivo desse algoritmo é baseada em qual indivíduo consegue realizar o maior caminho pelo tabuleiro sem repetir posições. Para análise de resultados, há também um método que, diferentemente do anterior, armazena o pior jogo.
getBestGame:verificará qual indivíduo possui o maior valor de moves dentre os 30.


getWorstGame:armazena qual possui o pior jogo .
	

em seguida esse processo é aplicado à população, de modo que o indivíduo 1 é pareado com o 15, o 2 com 16, o 3 com 17, e assim por diante até parear o indivíduo 14 com o 30. Agora pareados, ocorre a operação de crossover, mostrada na figura a seguir.

O processo de crossover dos indivíduos a direita gera outros dois indivíduos filhos a esquerda, ambos possuindo características mescladas dos seus pais. A operação de crossover se dá mesclando o tabuleiro de prioridades de ambos indivíduos, gerando assim dois novos indivíduos com dois novos tabuleiros de prioridade. Ao final dessa etapa, a população será dobrada.
A mutação tem uma chance aleatória de ocorrer sobre os indivíduos da população. O indivíduo afetado por ela tem algum valor de seu tabuleiro de prioridade alterado dinamicamente, conforme mostrado na figura abaixo.



a posição (4,4) do tabuleiro de prioridades de um indivíduo é selecionada aleatoriamente, e tem seu valor alterado de 7 para 1 também de forma aleatória.

Após todas as operações anteriores, dos 60 indivíduos da população, 30 são selecionados de forma aleatória, formando uma nova população. Entretanto, foi decidido aplicar o elitismo e garantiu-se que o melhor jogo da população anterior esteja presente na nova população. Portanto, o indivíduo oriundo do método getBestGame estará presente na próxima iteração do algoritmo.
O algoritmo vai iterar até um número de gerações previamente determinado. Em sua última geração, o problema pode ou não ter sido resolvido, mostrando o melhor e pior indivíduo de cada população.


 3 RESULTADOS

O algoritmo pode ser executado com diferentes números de gerações, tamanhos de tabuleiros e populações. para analisar o resultado foi gerado uma população igual a 30, tamanho do tabuleiro 8x8 e a geração igual a 30 e o resultados obtidos.

3.1  Melhores e piores  indivíduos.
Após aplicar o algoritmo chegamos aos seguintes resultados, em azul apresenta o melhor resultado, em vermelho o pior resultado.

Notamos que o resultado de piores indivíduos possui uma grande variação de resultados, já no melhores valores notamos que é constante, ou seja, existe pouca variação. 
3.2 Tabelas 
Em seguida, é possível conferir o tabuleiro de prioridade do melhor jogo, bem como as posições visitadas por ele. A posição inicial do Cavalo é codificada para ser sempre a (0,0), que na tabela de visitados tem valor 1. É possível refazer o caminho seguindo apenas seguindo a ordem das visitas: 1, 2, 3, etc, para testar visualmente o resultadado do algoritmo acesse http://www.ojogos.com.br/jogo/passeio-do-cavalo e preencha os passos conforme esta apresentado na tabela de resultante.


Para essa execução do algoritmo, ele não consegue encontrar uma solução para o problema, porém chega próximo a uma com um indivíduo com 57 movimentos (sendo 64 a solução).
Apesar de não encontrar a solução perfeita, é perceptível que a população tende a melhorar a cada geração.
Pode-se relacionar ainda o tamanho da população com o comportamento dos piores jogos: a medida que a população aumenta, a variação dos piores jogos também aumenta. Isso ocorre porque uma maior população implica em maior randomicidade do algoritmo, dando espaço para que os piores jogos sejam substituídos aleatoriamente por jogos piores ou melhores que ele próprio.
A melhora dos melhores indivíduos ocorre de maneira quase exponencial: no começo do algoritmo há uma taxa de melhoria mais rápida do valor de bestGame, que vai diminuindo até a última geração.

3 .3 Outros Resultados:
Outras execuções do algoritmo foram realizadas, considerando agora diferentes tamanhos de tabuleiros, com o número de gerações e o tamanho da população fixados em 30. Foram realizadas 5 execuções do algoritmo e o tempo computacional e os melhores valores da Função Objetivo para cada tamanho de tabuleiro são mostrados a seguir.
Tabuleiro
Solução
Função Objetivo
Tempo Execução


A medida que o tamanho do tabuleiro aumenta, o tempo de solução aumenta exponencialmente, enquanto os melhores valores da Função Objetivo para as cinco execuções caem drasticamente. Uma maneira de aumentar esses valores, é aumentar o número de gerações de acordo com o tamanho do tabuleiro. 


4 CONCLUSÕES
 O Algoritmo Genético nessa situação não seria o ideal , foi verificado que sua otimização é um ponto a ser fortemente visível e poderia ser levado em consideração, apesar de não ter apresentado um resultado perfeito em alguns casos neste artigo, sempre  os resultados foram aproximados isso levando em conta o tempo que execução que como foi notado é consideravelmente baixo, coisa que outra aplicações levariam dias ou horas, precisando de máquinas com  desempenho bastante elevado, no problema do Passeio do Cavalo. a sua alto influência  randômica afeta diretamente no resultado, ou seja , a uma grande dependência nas operações de crossover e mutação para encontrar uma solução, é o principal fator pelo qual não é uma fonte confiável para a solução do problema, embora algoritmos de força bruta possam gastar mais tempo computacional na solução, eles possuem uma maior confiabilidade.



5 Referências
TONINI, Lindomar . Algoritmos genéticos - Problema do Cavalo de Xadrez: Lindomar Tonini. Disponível em: <https://www.youtube.com/watch?v=A-QRenxrFjc>. Acesso em: 20 mar. 2018

.KNIGHT'S tour. Disponível em: <https://en.wikipedia.org/wiki/Knight%27s_tour>. Acesso em: 20 mar. 2018.

AL-GHARAIBEH , Jafar; QAWAGNEH , Zakariya ; AL-ZAHAWI, Hiba. Genetic Algorithms with Heuristic Knight’s Tour Problem. Disponível em: <http://citeseerx.ist.psu.edu/viewdoc/download?rep=rep1&type=pdf&doi=10.1.1.115.3709>. Acesso em: 20 mar. 2018.

PROBLEMA do cavalo. Disponível em: <https://pt.wikipedia.org/wiki/Problema_do_cavalo>. Acesso em: 20 mar. 2018.

TAMBERLINI ALVES, Fernando ; DUARTE PINTO, Paulo Eustaquio. Aplicação de Algoritmos Geneticos ao Problema do Percurso do Cavalo. Disponível em: <http://www.e-publicacoes.uerj.br/index.php/cadinf/article/viewFile/6556/4674>. Acesso em: 20 mar. 2018.

AURÉLIO CAVALCANTI PACHECO , Marco . ALGORITMOS GENÉTICOS: PRINCÍPIOS E APLICAÇÕES . Disponível em: <http://www2.ica.ele.puc-rio.br/Downloads/38/CE-Apostila-Comp-Evol.pdf>. Acesso em: 20 mar. 2018

