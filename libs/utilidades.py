from typing import List
from objetos.entidades.jogador import Jogador

def inserir_ordenado(lista_posicao: List[Jogador], novo_jogador: Jogador):
    """
    Insere o objeto Jogador na lista, mantendo a ordem decrescente de habilidade.
    """
    if not lista_posicao:
        lista_posicao.append(novo_jogador)
        return

    # Percorre a lista para encontrar o local correto
    for i, jogador_atual in enumerate(lista_posicao):
        # Compara a habilidade (Decrescente: Maior habilidade primeiro)
        if novo_jogador.get_habilidade() >= jogador_atual.get_habilidade():
            lista_posicao.insert(i, novo_jogador)
            return

    # Se a habilidade for a menor de todos, adiciona ao final
    lista_posicao.append(novo_jogador)