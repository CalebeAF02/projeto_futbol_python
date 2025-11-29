# sistema/controlador_sistema.py

from sistema.controladoras.controladora_servico import ControladoraServico
from libs.formatacao import Formatacao
from typing import List, Dict

class ControladorSistema:
    """
    Classe responsável por iniciar o sistema, gerenciar o loop do menu 
    e orquestrar a interação entre o usuário e a camada de Serviço.
    """
    def __init__(self):
        # Inicializa a camada de serviço (e, consequentemente, a persistência)
        self._servico = ControladoraServico()
        self._executando = False

    def iniciar(self):
        """Inicia o loop principal do sistema."""
        self._executando = True
        print("⚽ Sistema de Gerenciamento de Time - Iniciado! ⚽")
        self._loop_principal()

    def _loop_principal(self):
        """Contém a lógica de repetição do menu."""
        while self._executando:
            try:
                print("\n" + "="*35)
                print(Formatacao.formatar_menu())
                print("="*35)
                
                escolha = input('Entre com a opção: ').strip()
                
                if not escolha.isdigit():
                    print("❌ Entrada inválida. Digite o número da opção.")
                    continue
                
                num = int(escolha)
                self._processar_opcao(num)
                
            except Exception as e:
                # Captura erros inesperados e mantém o sistema rodando (exceto se for sair)
                print(f"\n🚨 Ocorreu um erro no sistema: {e}")

    def _processar_opcao(self, num: int):
        """Executa a função correspondente à opção escolhida."""
        
        if num == 1: # CONTRATAR_JOGADORES
            self._contratar_jogadores()
            
        elif num == 2: # TROCA_JOGADORES
            self._troca_jogadores()

        elif num == 3: # Definir_Esquema_Tatico
            self._definir_esquema_tatico()

        elif num == 4: # Montar_o_Time
            self._apresentar_elenco()
            
        elif num == 5: # Montar_o_Time
            self._montar_time()
            
        elif num == 6: # SAIR
            self.terminar()
            
        else:
            print("Opção não reconhecida. Tente novamente.")

    def _contratar_jogadores(self):
        """Lógica da Opção 1."""
        print("\n--- 1. CONTRATAR JOGADORES ---")
        try:
            nome = str(input("Nome: "))
            posicao = str(input("Posição (goleiro/defensor/meia/atacante): "))
            habilidade = int(input("Habilidade (0-10): "))
            
            novo_jogador = self._servico.contratar_jogador(nome, posicao, habilidade)
            print(f"🎉 Contratado com sucesso: {novo_jogador}")
            
            elenco = self._servico._persistencia.buscar_todos() # Acesso ao elenco para exibição
            print(Formatacao.formatar_elenco_ordenado(elenco))
            
        except (ValueError, TypeError) as e:
            print(f"❌ Erro na contratação: {e}")

    def _troca_jogadores(self):
        """Lógica da Opção 2."""
        print("\n--- 2. TROCA DE JOGADORES ---")
        try:
            posicao = input("Posição da troca: ")
            
            # Exibe jogadores e solicita índice
            lista_posicao = self._servico._persistencia.buscar_por_posicao(posicao)
            if not lista_posicao:
                print(f"⚠️ Não há jogadores na posição {posicao.capitalize()} para realizar a troca.")
                return
                
            print(f"\nJogadores na posição {posicao.capitalize()}:")
            for i, jogador in enumerate(lista_posicao):
                print(f"[{i}] {jogador}")
            
            indice_sai = int(input(f"Índice do jogador que SAI (0 a {len(lista_posicao)-1}): "))
            
            print("\n[INFORMAÇÕES DO JOGADOR QUE ENTRA]")
            nome_entra = input("Nome do jogador que ENTRA: ")
            habilidade_entra = int(input(f"Habilidade de {nome_entra}: "))
            
            jogador_sai, jogador_entra = self._servico.realizar_troca(posicao, indice_sai, nome_entra, habilidade_entra)
            print(f"✅ Troca realizada: {jogador_sai.get_nome().capitalize()} SAI, {jogador_entra.get_nome().capitalize()} ENTRA.")
            
            elenco = self._servico._persistencia.buscar_todos()
            print(Formatacao.formatar_elenco_ordenado(elenco))
            
        except (ValueError, TypeError, IndexError) as e:
            print(f"❌ Erro na troca: {e}")
        except Exception as e:
            print(f"❌ Erro: {e}")
            
    def _definir_esquema_tatico(self):
        """Lógica da Opção 3."""
        print("\n--- 3. DEFINIR ESQUEMA TÁTICO ---")
        try:
            entrada = input("Digite o esquema (D M A, ex: 4 4 2): ").split()
            if len(entrada) != 3: 
                raise ValueError("Formato inválido. Use 3 números separados por espaço (Ex: 4 4 2).")
                
            defensores, meias, atacantes = map(int, entrada)
            
            self._servico.definir_esquema_tatico(defensores, meias, atacantes)
            print(f"✅ {Formatacao.formatar_esquema_tatico(self._servico._persistencia.get_esquema_tatico())}")
        except (ValueError, Exception) as e:
            print(f"❌ Erro no esquema: {e}")

    def _apresentar_elenco(self):
        print("\n--- ELENCO COMPLETO ---")
        
        # 1. Obter o elenco do serviço
        elenco = self._servico.apresentar_elenco_ordenado()
        
        # 2. Usar a formatação (da sua classe Formatacao)
        output = Formatacao.formatar_elenco_ordenado(elenco)
        print(output)
    
    def _montar_time(self):
        """Lógica da Opção 4."""
        print("\n--- 4. MONTAR O TIME ---")
        try:
            time_titular = self._servico.montar_time_titular()
            print(Formatacao.formatar_campo(time_titular))
        except Exception as e:
            print(f"❌ Não foi possível montar o time: {e}")

    def terminar(self):
        """Termina a execução do sistema."""
        self._executando = False
        print("\n👋 Saindo do sistema. Até mais, Cabo Calebe!")