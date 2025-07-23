Implementação do Algoritmo A* para Futebol de Robôs Autônomos*
Este repositório contém uma implementação do algoritmo A* (A-star) para navegação autônoma de robôs em um ambiente de Soccer Cup, onde o robô deve desviar de adversários e marcar gols de forma eficiente.

📌 Visão Geral
O A* é um algoritmo de busca em grafos amplamente utilizado em jogos e robótica para encontrar o caminho mais curto entre dois pontos, considerando obstáculos e custos de movimento. Nesta implementação, o robô:
✅ Calcula rotas ótimas usando heurística de Manhattan
✅ Evita obstáculos (adversários, barreiras)
✅ Considera custos de rotação (curvas de 45°, 90° e 180°)
✅ Ajusta estratégia quando está com a posse de bola

⚙️ Como Funciona?

📊 Estruturas Principais

•PriorityQueue: Gerencia os nós abertos, priorizando os de menor custo total (f(n) = g(n) + h(n)).

•custo_g: Armazena o custo real do caminho desde o início.

•custo_f: Armazena o custo total (real + heurística).

•veio_de: Usado para reconstruir o caminho final.

🔍 Heurística (h(n))

Distância de Manhattan:

heurística = (|x1 - x2| + |y1 - y2|) * 10

🔄 Custo de Movimento

•Movimento reto (↑↓→←): Custo = 10

•Movimento diagonal (↖↗↙↘): Custo = 14 (aproximação de 10√2)

Custo de rotação:
  •Curva de 45°: +5
  
  •Curva de 90°: +10
  
  •Inversão de 180°: +40

• Com a bola: O custo de rotação dobra para movimentos mais cuidadosos.

🚀 Como Usar?

📋 Parâmetros da Função

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):

pos_inicial: Tupla (x, y) da posição inicial.

• pos_objetivo: Tupla (x, y) do destino (ex.: gol).

• obstaculos: Lista de tuplas [(x1, y1), (x2, y2), ...] representando adversários/barreiras.

• largura_grid e altura_grid: Dimensões do campo.

• tem_bola: Se True, aplica penalidade maior em curvas.

📤 Saída

Retorna uma lista de tuplas representando o caminho ótimo do início ao objetivo (ou lista vazia se não houver solução).

📚 Referências
- **MARTINS, R. F.** et al. *"Implementação do Algoritmo A* em Futebol de Robôs"*. In: SICFEI 2018, Centro Universitário FEI. Disponível em: [https://fei.edu.br/sites/sicfei/2018/cc/SICFEI_2018_paper_61.pdf](https://fei.edu.br/sites/sicfei/2018/cc/SICFEI_2018_paper_61.pdf)
- Silva, A. G. *"A* Pathfinding para Iniciantes"*. Universidade Federal de Santa Catarina (UFSC), 2014. Disponível em: [https://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf](https://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf)
- [Algoritmo A* no Python - Melhor Caminho - A Estrela - Hashtag Programação](https://www.youtube.com/watch?v=fTtYzHfGlyk)
- [Criando Labirintos com Python- Hashtag Programação](https://www.youtube.com/watch?v=mk0576JDh4w&t=908s)
- [Explicação do Algoritmo A* (A Star) - Carlos Mingoto] (https://www.youtube.com/watch?v=o5_mqZKhTvw)
