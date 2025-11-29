from ..dominios.nome import Nome
from ..dominios.posicao import Posicao
from ..dominios.habilidade import Habilidade

# Classe Jogador herda as características (atributos) e os métodos Set/Get
class Jogador(Nome, Posicao, Habilidade):
    def __init__(self, nome_str: str, posicao_str: str, habilidade_int: int):
        
        self._nome = Nome(nome_str)
        self._posicao = Posicao(posicao_str)
        self._habilidade = Habilidade(habilidade_int)
        
    # 💡 Métodos 'getter' para manter a compatibilidade com o resto do sistema
    def get_nome(self):
        return self._nome.get_nome()
    
    def get_posicao(self):
        return self._posicao.get_posicao()
    
    def get_habilidade(self):
        return self._habilidade.get_habilidade()
        
    def __str__(self):
        # Acessa os atributos através dos getters ou diretamente
        return (f"Nome: {self.get_nome().capitalize()} | Posição: {self.get_posicao().capitalize()} "
                f"| Habilidade: {self.get_habilidade()}/10")
        