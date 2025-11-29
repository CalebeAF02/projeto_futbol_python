from abc import ABC, abstractmethod
from typing import List, Dict
from objetos.entidades.jogador import Jogador

class InterfacePersistencia(ABC):
    """Interface de Persistência (repositório) - Lidar com o armazenamento de dados."""
    @abstractmethod
    def adicionar_jogador(self, jogador: Jogador):
        pass

    @abstractmethod
    def remover_jogador(self, jogador: Jogador):
        pass
        
    @abstractmethod
    def buscar_todos(self) -> Dict[str, List[Jogador]]:
        pass
        
    @abstractmethod
    def buscar_por_posicao(self, posicao: str) -> List[Jogador]:
        pass
        
    @abstractmethod
    def get_esquema_tatico(self) -> List[int]:
        pass

    @abstractmethod
    def set_esquema_tatico(self, esquema: List[int]):
        pass
