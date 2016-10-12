Exercício problema 4: Boas práticas e evolução de arquitetura 
=============================================================

O objetivo desta etapa é implementar boas práticas de ESW, alguns conceitos mais
avançados de programação e evoluir o código do jogo nesta direção. Esta etapa
avaliará qualidade de código e metodologias.

## Apresentação
Não há.

## Entrega do código
A entrega é gradual contínua e será feita na forma de "bullet points" na medida
que o grupo atigir um determinado objetivo (o prazo para cada objeto será 
determinado em sala, normalmente 1 semana de diferença do dia em que o tema for
abordado em sala de aula). Os objetivos estão listados na seção de avaliação.

## Avaliação
Objetivos:

* Orientação a objetos (200 pts)
    - Organizar o código em classes e diminuir a macarronada de funções
    - Herdar corretamente de World e das classes de objeto físico como Circle, AABB, etc

* Testes (200 pts)
    - Criar uma suite de testes básica
    - Usar o mock em pelo menos 1 teste

* Empacotamento (200 pts)
    - Criar o pacote para jogo no PyPI

* State (100 pts)
    - Implementar o padrão "state" em algum objeto de jogo

* Sinais (100 pts)
    - Implementar e utilizar um sinal próprio para o jogo
    
* Física avançada (100 pts)
    - Utilizar impulsos e forças para obter algum efeito de jogabilidade

* Cython (100 pts)
    - Acelerando funções com o Cython
    - Profiling (cProfile, snakeviz, pstats)
    
