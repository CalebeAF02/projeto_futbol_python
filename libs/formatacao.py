from typing import List, Dict
from objetos.jogador import Jogador

class Formatacao:
    
    @staticmethod
    def formatar_menu():
        menu = (
            "--- MENU PRINCIPAL ---\n"
            "1 (CONTRATAR_JOGADORES)\n"
            "2 (TROCA_JOGADORES)\n"
            "3 (Definir_Esquema_Tatico)\n"
            "4 (Apresentar_Elenco)\n"
            "5 (Montar_o_Time)\n"
            "6 (SAIR)\n"
        )
        return menu

    @staticmethod
    def formatar_elenco_ordenado(elenco: Dict[str, List[Jogador]]):
        output = ["\n--- ELENCO ORGANIZADO POR HABILIDADE ---"]
        
        # Dicionário de mapeamento para pluralizar corretamente em português
        pos_map_plural = {
            'goleiro': 'GOLEIROS',
            'defensor': 'DEFENSORES', # CORREÇÃO APLICADA AQUI
            'meia': 'MEIAS',
            'atacante': 'ATACANTES'
        }
        
        # Ordem das posições
        ordem_posicoes = ['goleiro', 'defensor', 'meia', 'atacante']
        
        for pos_key in ordem_posicoes:
            lista_jogadores = elenco.get(pos_key, [])
            if lista_jogadores:
                # Usa o mapeamento para obter o nome no plural
                pos_nome = pos_map_plural.get(pos_key, pos_key.upper()) 
                
                output.append(f"\n## {pos_nome}") 
                for i, jogador in enumerate(lista_jogadores):
                    output.append(f"   [{i}] {jogador}") 
        return "\n".join(output)
    
    @staticmethod
    def formatar_esquema_tatico(esquema: List[int]):
        if len(esquema) == 3:
            return f"Esquema Tático Atual: {esquema[0]}-{esquema[1]}-{esquema[2]}"
        return "Esquema Tático não definido."
        
    @staticmethod
    def formatar_campo(time_titular: Dict[str, List[Jogador]]):
        output = ["\n--- FORMAÇÃO DO TIME TITULAR ---"]
        
        # --- Configurações de Largura ---
        WIDTH_CONTENT = 55      # Largura do conteúdo (57 - 2 bordas)
        NAME_WIDTH = 8          # Máxima largura do nome do jogador

        # --- Funções Auxiliares de Formatação e Desenho ---
        
        def format_name(jogador: Jogador) -> str:
            """Retorna o nome truncado e alinhado à esquerda para 8 caracteres."""
            return jogador.get_nome()[:NAME_WIDTH].ljust(NAME_WIDTH)

        def get_names(position_key: str) -> List[str]:
            """Extrai e formata os nomes dos jogadores para a largura fixa."""
            jogadores = time_titular.get(position_key, [])
            return [format_name(j) for j in jogadores]
        
        def draw_line(names: List[str], symbol: str):
            """Desenha duas linhas (nomes e símbolos) com espaçamento fixo para WIDTH_CONTENT=55."""
            
            num_players = len(names)
            names_line = ''
            symbol_line = ''
            
            # --- Regras de Espaçamento Fixo para 55 de conteúdo ---
            if num_players == 4:
                # Nomes: | 4s N 5s N 5s N 5s N 4s |
                names_line = ' ' * 4 + names[0] + ' ' * 5 + names[1] + ' ' * 5 + names[2] + ' ' * 5 + names[3] + ' ' * 4
                
                # Símbolos CORRIGIDO: Deslocado 1 espaço para a esquerda (7 -> 6, 8 -> 9)
                symbol_line = ' ' * 6 + symbol + ' ' * 12 + symbol + ' ' * 12 + symbol + ' ' * 12 + symbol + ' ' * 9
                
            elif num_players == 3:
                # Nomes: | 7s N 8s N 8s N 7s | 
                names_line = ' ' * 7 + names[0] + ' ' * 8 + names[1] + ' ' * 8 + names[2] + ' ' * 7 

                # Símbolos CORRIGIDO: Deslocado 1 espaço para a esquerda (11 -> 10, 11 -> 12)
                symbol_line = ' ' * 10 + symbol + ' ' * 15 + symbol + ' ' * 15 + symbol + ' ' * 12

            elif num_players == 2:
                # Nomes: | 10s N 19s N 10s |
                names_line = ' ' * 10 + names[0] + ' ' * 19 + names[1] + ' ' * 10
                
                # Símbolos CORRIGIDO: Deslocado 1 espaço para a esquerda (13 -> 12, 13 -> 14)
                symbol_line = ' ' * 12 + symbol + ' ' * 27 + symbol + ' ' * 14
            
            else:
                names_line = ' ' * WIDTH_CONTENT
                symbol_line = ' ' * WIDTH_CONTENT

            # Garante que as linhas tenham exatamente 55 caracteres de conteúdo
            return f"|{names_line.ljust(WIDTH_CONTENT)}|\n|{symbol_line.ljust(WIDTH_CONTENT)}|"


        # --- Geração do Campo ---
        
        goleiro_nome = get_names('goleiro')[0] if time_titular.get('goleiro') else NAME_WIDTH * ' '
        defensores_nomes = get_names('defensor')
        meias_nomes = get_names('meia')
        atacantes_nomes = get_names('atacante')
        
        
        output.append("+" + "-" * WIDTH_CONTENT + "+")
        
        # Linhas em branco
        output.append("|" + " " * WIDTH_CONTENT + "|")
        
        # ATACANTES
        output.append(draw_line(atacantes_nomes, 'A'))
        
        # Linhas em branco
        output.append("|" + " " * WIDTH_CONTENT + "|")
        
        # MEIAS
        output.append(draw_line(meias_nomes, 'M'))
        
        # Linhas em branco (2 linhas de espaço)
        output.append("|" + " " * WIDTH_CONTENT + "|")
        output.append("|" + " " * WIDTH_CONTENT + "|")
        
        # DEFENSORES
        output.append(draw_line(defensores_nomes, 'D'))
        
        # Linhas em branco
        output.append("|" + " " * WIDTH_CONTENT + "|")

        # GOLEIRO
        # Linha do Gol: | 22s [----o-----] 23s | (10 chars do gol)
        # CORREÇÃO APLICADA: Reduz o espaçamento final de 24 para 23 para totalizar 55 de conteúdo.
        gol_line = (22 * ' ') + (4 * '-') + ('o') + (5 * '-') + (23 * ' ') 
        output.append(f"|{gol_line}|")
        
        # Nome do Goleiro: Centralizado no gol (10 de largura)
        nome_goleiro_centralizado = goleiro_nome.center(8)
        output.append(f"|{(22 * ' ')}|{nome_goleiro_centralizado}|{(23 * ' ')}|")

        # Posição (G): Centralizado no gol
        pos_goleiro_centralizado = '(G)'.center(8)
        output.append(f"|{(22 * ' ')}|{pos_goleiro_centralizado}|{(23 * ' ')}|")
        
        output.append("+" + "-" * WIDTH_CONTENT + "+")
        
        return "\n".join(output)