from ..interface_validacao import IValidacao

class Habilidade(IValidacao):
    def __init__(self, habilidade: int): 
        self._habilidade = self.validar(habilidade)

    def get_habilidade(self):
        return self._habilidade

    def set_habilidade(self, nova_habilidade: int):
        self._habilidade = self.validar(nova_habilidade)

    def validar(self, habilidade: int) -> int:
        """
        Validação da habilidade: Deve estar entre 0 e 10.
        """
        if not isinstance(habilidade, int):
            raise TypeError("A habilidade deve ser um número inteiro.")
        if 0 <= habilidade <= 10:
            return habilidade
        else:
            raise ValueError("A habilidade deve estar entre 0 e 10.")