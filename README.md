# t2_projeto_otimizicao_algoritmos
Trabalho 2 da disciplina Projeto e Otimização de Algoritmos, Professor: Joao Batista Souza de Oliveira - PUCRS

O tobogã do parque
Você foi contratado pelo parque do Beto Carneiro pra ajudar em umas contas complicadas. Eles estão negociando a compra de um sofisticado tobogã que tem uma rampa enorme e pode ser regulado de várias formas, gerando desde descidas suaves ("modo baby") até o "modo ninja suicida".
Eles ainda precisam escolher o modelo de tobogã para compra, e já sabem que os tobogãs oferecidos no mercado não podem produzir todas as posições intermediárias, algumas são bloqueadas por razões de segurança.

Agora a direção do parque quer saber o número exato de rampas que são possíveis, dadas estas condições:
*A rampa tem altura m metros e comprimento de n metros;
*Para cada metro, a rampa pode ser regulada para estar na horizontal mantendo sua altura ou na diagonal, descendo um metro;
*O cliente inicia no ponto mais alto do lado esquerdo e deve terminar sua viagem no ponto mais baixo do lado direito;
*O manual informa que algumas posições não podem ser usadas. Elas estão marcadas com e as posições possíveis são marcadas com 0.

Sua missão é ajudar a direção do parque a descobrir quantos caminhos são possíveis para vários tamanhos de tobogã, para que eles possam escolher melhor qual modelo vão comprar. 
Você deve fazer isto de três maneiras diferentes:
Usando uma recursão simples e sem nenhuma memorização;
Usando memorização na sua recursão;
Sem usar recursão e preenchendo uma matriz de resultados.

Eles esperam receber um programa que recebe o nome do arquivo de tobogã pela linha de comando
e apresenta o número correto de caminhos.

Exemplo de arquivo e execução
12 18  
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0  
0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0  
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0  
0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 0  
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0  
0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0  
0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0  
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0  
0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0  

O manual fornece um exemplo pequeno, representado para um tobogã de altura 12 metros por 18 metros de comprimento. Os tobogás oferecidos são geralmente bem maiores do que isso!
