from ..interface_validacao import IValidacao

class Nome(IValidacao):
    def __init__(self, nome: str): 
        self._nome = self.validar(nome)

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome: str):
        self._nome = self.validar(novo_nome)

    def validar(self, nome) -> str:
        """
        Validação do nome: 
        1. Garante que é string.
        2. Remove números.
        3. Converte para minúsculas.
        4. Limita a 8 caracteres.
        """
        
        # 🚨 CORREÇÃO PRINCIPAL: VERIFICAÇÃO DE TIPO
        if not isinstance(nome, str):
            # Se for um inteiro (habilidade), lança um erro claro.
            raise TypeError(f"Erro Crítico: 'Nome' deve ser string (str), mas recebeu '{type(nome).__name__}'.")

        # 1. Converte para minúsculas
        nome_limpo = nome.lower()
        
        # 2. Remove números (conforme sua lógica original)
        nome_sem_num = "".join(c for c in nome_limpo if not c.isdigit()) 
        
        # 3. Corta o nome para no máximo 8 caracteres (Subscrição segura)
        nome_final = nome_sem_num[:8] 
        
        if not nome_final:
            raise ValueError("Nome do jogador inválido ou vazio após a limpeza.")
            
        return nome_final