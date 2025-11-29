from ..interfaces.interface_persistencia import InterfacePersistencia
from typing import List, Dict
from objetos.entidades.jogador import Jogador
from libs.utilidades import inserir_ordenado # Vamos criar essa função na pasta 'libs'

class ControladoraPersistencia(InterfacePersistencia):
    def __init__(self):
        # A estrutura de dados principal (o elenco)
        self.elenco: Dict[str, List[Jogador]] = {
            'goleiro': [],
            'defensor': [],
            'meia': [],
            'atacante': []
        }
        # A estrutura do esquema tático
        self.esquema_tatico: List[int] = []

    def adicionar_jogador(self, jogador: Jogador):
        posicao = jogador.get_posicao()
        lista_posicao = self.elenco[posicao]
        # Adiciona de forma ORDENADA, usando utilidade da pasta libs
        inserir_ordenado(lista_posicao, jogador)

    def remover_jogador(self, jogador: Jogador):
        posicao = jogador.get_posicao()
        self.elenco[posicao].remove(jogador)

    def buscar_todos(self) -> Dict[str, List[Jogador]]:
        return self.elenco

    def buscar_por_posicao(self, posicao: str) -> List[Jogador]:
        return self.elenco.get(posicao, [])

    def get_esquema_tatico(self) -> List[int]:
        return self.esquema_tatico

    def set_esquema_tatico(self, esquema: List[int]):
        self.esquema_tatico = esquema # Substitui o esquema anterior