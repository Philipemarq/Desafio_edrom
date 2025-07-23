# NOME DO CANDIDATO: [Philipe Marques Costa]
# CURSO DO CANDIDATO: [Ciência da computação]
# AREAS DE INTERESSE: [Visão computacional e Behavior]

from queue import PriorityQueue


def calcular_heuristica(celula, destino):
    """Calcula a heurística h(n) entre duas células utilizando o método de Manhattan"""
    (x1, y1) = celula
    (x2, y2) = destino
    return (abs(x1 - x2) + abs(y1 - y2)) * 10


def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    obstaculos_set = set(obstaculos)

    # A 'lista_aberta' usa uma Fila de Prioridade
    # Ela armazena as células que ainda precisamos visitar, ordenadas pelo menor custo_f (f(n))
    lista_aberta = PriorityQueue()

    # 'custo_g': Dicionário que armazena o custo real para ir da célula inicial até qualquer outra célula
    # 'custo_f': Dicionário que armazena o custo total (g + heurística) para cada célula
    # 'veio_de': Dicionário que registra de qual célula viemos para chegar na atual
    custo_g = {pos_inicial: 0}  # O custo para chegar ao início é 0
    custo_f = {pos_inicial: calcular_heuristica(pos_inicial, pos_objetivo)}
    veio_de = {}  # Começa vazio, pois ainda não nos movemos.

    # Adiciona o ponto de partida na fila de prioridade
    # A fila ordena os itens pelo primeiro valor da tupla (neste caso, o custo_f)
    lista_aberta.put((custo_f[pos_inicial], pos_inicial))

    # O loop principal continua enquanto houver células para explorar na lista_aberta
    while not lista_aberta.empty():
        # Pega a célula da fila que tem o menor custo_f
        _, pos_atual = lista_aberta.get()

        # Condição de parada:
        if pos_atual == pos_objetivo:
            # Se a posição atual é o objetivo, encontramos o caminho. Agora, deve reconstruí-lo
            caminho = []
            pos_temp = pos_atual  # Começa a reconstrução a partir do final
            # O loop volta, usando o 'veio_de' para encontrar o "pai" de cada célula.
            while pos_temp in veio_de:
                caminho.append(pos_temp)  # Adiciona a célula ao caminho.
                pos_temp = veio_de[pos_temp]  # Move para a célula anterior.
            # O caminho foi construído de trás para frente, assim deve inverter antes de retornar.
            return caminho[::-1]

        # Explorar vizinhos:
        # Gera todos os 8 vizinhos possíveis (incluindo diagonais).
        for desloca_em_x in [-1, 0, 1]:  # Deslocamento em x: esquerda, nenhum, direita.
            for desloca_em_y in [-1, 0, 1]:  # Deslocamento em y: cima, nenhum, baixo.
                # Pula a própria célula atual (quando o deslocamento é (0,0)).
                if desloca_em_x == 0 and desloca_em_y == 0:
                    continue

                # Calcula a posição do vizinho.
                pos_vizinho = (pos_atual[0] + desloca_em_x, pos_atual[1] + desloca_em_y)

                # Verifica se o vizinho está dentro dos limites do campo.
                if not (0 <= pos_vizinho[0] < largura_grid and 0 <= pos_vizinho[1] < altura_grid):
                    continue  # Se estiver fora, ignora e vai para o próximo vizinho.
                # Verifica se o vizinho é um obstáculo.
                if pos_vizinho in obstaculos_set:
                    continue  # Se for obstáculo, ignora.

                # Cálculo do custo de movimento:
                # Custo base: 10 para movimentos retos (vertical/horizontal), 14 para diagonais (aproximação de 10 * sqrt(2) - é mais rápido pro computador!!)
                custo_base = 10 if desloca_em_x == 0 or desloca_em_y == 0 else 14

                # (Desafio -Nível 1) Custo de Rotação
                custo_rotacao = 0
                # Só podemos calcular a rotação se houver um "pai" (se não for o primeiro movimento).
                if pos_atual in veio_de:
                    pos_pai = veio_de[pos_atual]
                    # Vetor do movimento anterior (do pai para o atual).
                    vetor_anterior = (pos_atual[0] - pos_pai[0], pos_atual[1] - pos_pai[1])
                    # Vetor do novo movimento (do atual para o vizinho).
                    vetor_novo = (pos_vizinho[0] - pos_atual[0], pos_vizinho[1] - pos_atual[1])

                    # Se o vetor mudou, houve uma curva.
                    if vetor_novo != vetor_anterior:
                        # Inversão de 180 graus: ALTA PENALIDADE!!
                        if vetor_novo[0] == -vetor_anterior[0] and vetor_novo[1] == -vetor_anterior[1]:
                            custo_rotacao = 40
                        else:
                            # Curva de 90 graus: o produto escalar dos vetores é 0
                            dot_product = vetor_anterior[0] * vetor_novo[0] + vetor_anterior[1] * vetor_novo[1]
                            if dot_product == 0:
                                custo_rotacao = 10
                            # Curva de 45 graus:
                            else:
                                custo_rotacao = 5

                # (Desafio - Nível 2) Custo por Estado
                # Se o robô está com a bola, elu deve ser mais cuidadoso.
                if tem_bola:
                    custo_rotacao *= 2  # Dobra a penalidade de rotação.

                # O custo total do movimento é a soma do custo base e da penalidade de rotação.
                custo_movimento = custo_base + custo_rotacao

                # Calcula o custo 'g' para chegar a este vizinho através da célula atual.
                tentativa_custo_g = custo_g.get(pos_atual, float('inf')) + custo_movimento

                # Se o novo caminho para o vizinho for mais barato que qualquer outro já registrado, entao:
                if tentativa_custo_g < custo_g.get(pos_vizinho, float('inf')):
                    # então atualiza tudo sobre este vizinho.
                    veio_de[pos_vizinho] = pos_atual  # Registra que o melhor caminho para o vizinho vem do atual.
                    custo_g[pos_vizinho] = tentativa_custo_g  # Atualiza seu custo g.
                    custo_f[pos_vizinho] = tentativa_custo_g + calcular_heuristica(pos_vizinho,
                                                                                   pos_objetivo)  # Recalcula e atualiza seu custo f.
                    # Adiciona o vizinho (com sua nova prioridade) na fila para ser explorado.
                    lista_aberta.put((custo_f[pos_vizinho], pos_vizinho))

    # Se o loop terminar e não tivermos retornado, significa que não há caminho.
    return []