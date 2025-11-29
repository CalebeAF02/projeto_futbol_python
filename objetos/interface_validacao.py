from abc import ABC, abstractmethod

class IValidacao(ABC):
    """Interface Abstrata para forçar a validação em classes filhas."""
    
    @abstractmethod
    def validar(self, valor):
        """Método de validação a ser implementado por cada classe."""
        pass