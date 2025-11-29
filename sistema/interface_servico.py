from abc import ABC, abstractmethod
from typing import List, Dict
from objetos.jogador import Jogador

class IPersistencia(ABC):
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

class IServico(ABC):
    """Interface de Serviço (Business Logic) - Lidar com as regras de negócio."""
    @abstractmethod
    def contratar_jogador(self, nome: str, posicao: str, habilidade: int) -> Jogador:
        pass

    @abstractmethod
    def realizar_troca(self, posicao: str, indice_sai: int, nome_entra: str, habilidade_entra: int):
        pass

    @abstractmethod
    def definir_esquema_tatico(self, defensores: int, meias: int, atacantes: int):
        pass

    @abstractmethod
    def montar_time_titular(self) -> Dict[str, List[Jogador]]:
        pass