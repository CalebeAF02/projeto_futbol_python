from sistema.interface_servico import IServico, IPersistencia
from sistema.persistencia import PersistenciaEmMemoria # Construtor Persistência
from objetos.jogador import Jogador
from typing import List, Dict

class ServicoTime(IServico):
    def __init__(self, persistencia: IPersistencia = None):
        # Injeção de dependência: Permite trocar a persistência (ex: para testes)
        self._persistencia = persistencia if persistencia is not None else PersistenciaEmMemoria()


    def contratar_jogador(self, nome: str, posicao: str, habilidade: int) -> Jogador:
        # 💡 CORREÇÃO: Usar argumentos nomeados para garantir o mapeamento.
        novo_jogador = Jogador(nome, posicao, habilidade)
        self._persistencia.adicionar_jogador(novo_jogador)
        return novo_jogador

    def definir_esquema_tatico(self, defensores: int, meias: int, atacantes: int):
        # Validação do Esquema Tático (Regra de Negócio)
        if not ((2 <= defensores <= 4) and (2 <= meias <= 4) and (2 <= atacantes <= 4)):
            raise ValueError('Cada posição deve conter entre 2 e 4 jogadores.')
        if (defensores + meias + atacantes) != 10:
            raise ValueError('A soma das posições deve totalizar 10 jogadores.')
        
        self._persistencia.set_esquema_tatico([defensores, meias, atacantes])

    def apresentar_elenco_ordenado(self) -> Dict[str, List[Jogador]]:
        return self._persistencia.buscar_todos()
    
    def montar_time_titular(self) -> Dict[str, List[Jogador]]:
        esquema = self._persistencia.get_esquema_tatico()
        if len(esquema) != 3:
            raise Exception("Esquema Tático não definido.")

        qtd_defensores, qtd_meias, qtd_atacantes = esquema
        elenco = self._persistencia.buscar_todos()
        time_titular = {}
        
        configuracao = {
            'goleiro': 1,
            'defensor': qtd_defensores,
            'meia': qtd_meias,
            'atacante': qtd_atacantes
        }

        for posicao, quantidade_necessaria in configuracao.items():
            # Seleciona os N melhores (já estão ordenados na persistência)
            selecionados = elenco.get(posicao, [])[:quantidade_necessaria] 
            
            if len(selecionados) < quantidade_necessaria:
                raise Exception(f"Faltam jogadores na posição {posicao.capitalize()} para montar o time.")
                
            time_titular[posicao] = selecionados
            
        return time_titular

    def realizar_troca(self, posicao: str, indice_sai: int, nome_entra: str, habilidade_entra: int):
        lista_posicao = self._persistencia.buscar_por_posicao(posicao)

        if not (0 <= indice_sai < len(lista_posicao)):
            raise IndexError("Índice do jogador a ser trocado fora do limite.")
            
        # 1. Remove o jogador que sai
        jogador_sai = lista_posicao.pop(indice_sai)
        
        # 2. Adiciona o novo jogador (a Persistência se encarrega de reinserir ordenado)
        novo_jogador = Jogador(nome_entra, posicao, habilidade_entra)
        self._persistencia.adicionar_jogador(novo_jogador)

        return jogador_sai, novo_jogador