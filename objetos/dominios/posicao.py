from ..interface_validacao import IValidacao

class Posicao(IValidacao):
    POSICOES_VALIDAS = ['goleiro', 'defensor', 'meia', 'atacante']

    def __init__(self, posicao: str): 
        self._posicao = self.validar(posicao)

    def get_posicao(self):
        return self._posicao

    def set_posicao(self, nova_posicao: str):
        self._posicao = self.validar(nova_posicao)

    def validar(self, posicao: str) -> str:
        """
        Validação da posição: Verifica se a posição existe.
        """
        posicao_lower = posicao.lower()
        if posicao_lower not in self.POSICOES_VALIDAS:
            raise ValueError(f"Posição inválida: {posicao}. Posições permitidas: {', '.join(self.POSICOES_VALIDAS)}")
        return posicao_lower