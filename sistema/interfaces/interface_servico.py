from abc import ABC, abstractmethod
from typing import List, Dict
from objetos.entidades.jogador import Jogador

class InterfaceServico(ABC):
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