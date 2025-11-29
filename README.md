# ⚽ Futebol_UNB_TP1

Projeto acadêmico em **Python**, desenvolvido na Universidade de Brasília (UnB), que demonstra uma evolução significativa de um código procedural básico para uma **Arquitetura Orientada a Objetos (POO) em Camadas**. O foco atual, no 7º Semestre, está em **Abstração**, **Desacoplamento** e **Boas Práticas de Design**.

O sistema simula um **Gerenciador de Elenco e Tática de Time de Futebol**, com ênfase na separação de responsabilidades.

---

## ✨ Evolução Arquitetural (1º/3º Semestre vs. 7º Semestre)

Esta reestruturação marca a transição de um projeto de **Introdução à Programação** para um projeto de **Engenharia de Software**, aplicando os conhecimentos adquiridos em disciplinas como POO e Tópicos de Programação.

| Característica | 1º/3º Semestre (Original - Procedural) | 7º Semestre (Atual - POO em Camadas) |
| :--- | :--- | :--- |
| **Arquitetura** | **Procedural e Monolítica.** Funções soltas manipulando listas globais. | **Orientada a Objetos (POO) e Camadas.** Separação em Domínio, Serviço e Persistência. |
| **Gerenciamento de Estado** | Uso extensivo de **Variáveis Globais**, dificultando a manutenção e testes. | **Encapsulamento Completo.** O estado é gerenciado pela classe `PersistenciaEmMemoria` e acessado via `Servico`. |
| **Modelagem de Dados** | Listas de strings ou dados crus. | **Entidades Ricas (Domínios).** Objetos `Jogador` que herdam características (`Nome`, `Posicao`, `Habilidade`). |
| **Validação de Dados** | **Lógica de Menu/Função.** Validação misturada com a entrada de usuário. | **Inerente ao Objeto (Design by Contract).** Validação forçada por Interfaces Abstratas (`IValidacao`) e executada na inicialização de classes (Herança). |
| **Modularidade** | Baixo acoplamento e reuso. | **Alta Coesão.** Uso de **Interfaces** (`IServico`, `IPersistencia`) permite injetar dependências e facilita testes. |

---

## 🚀 Arquitetura e Tecnologia

O projeto foi reestruturado para refletir uma **arquitetura limpa e modular**, aplicando os seguintes conceitos:

* **POO Avançada em Python:** Uso de classes abstratas (`abc`) e herança múltipla para construir o objeto `Jogador`.
* **Interfaces (Contratos):** Uso de `IServico` e `IPersistencia` para desacoplar a lógica de negócio do armazenamento de dados.
* **Validação por Herança:** Classes de domínio (`Nome`, `Posicao`, `Habilidade`) herdam de uma interface de validação, sendo responsáveis por garantir a integridade dos próprios dados.
* **Injeção de Dependência:** A camada de serviço (`ServicoTime`) recebe a persistência no construtor.
* **Persistência (Mock):** Uso de dicionários em memória para simular o armazenamento (`PersistenciaEmMemoria`), mantendo os dados ordenados por habilidade com uma função utilitária (`inserir_ordenado`).

---

## 🧭 Estrutura do Projeto

A arquitetura está dividida em três pacotes principais:

| Pasta | Responsabilidade | Conteúdo Principal | Conceitos Aplicados |
| :--- | :--- | :--- | :--- |
| **`objetos/`** | **Domínio** | `Jogador`, `Nome`, `Posicao`, `Habilidade`, `IValidacao` | Encapsulamento, Herança Múltipla, Abstração |
| **`sistema/`** | **Lógica e Controle** | `ControladorSistema`, `ServicoTime`, `PersistenciaEmMemoria` | Camada de Serviço, Persistência, Interfaces |
| **`libs/`** | **Utilitários/Apoio** | `Formatacao` (Apresentação CLI), `utilidades` (Função de Ordenação) | Separação de Preocupações, Componentes Reutilizáveis |
| **`main.py`** | **Entry Point** | Inicializa o `ControladorSistema` e o loop principal. | Início do Ciclo de Vida |

---

## 🚀 Funcionalidades Atuais

O sistema agora opera sobre uma arquitetura robusta, garantindo a integridade dos dados e a lógica de negócio:

* **Contratação de Jogadores:** Criação de novos jogadores com validação automática de:
    * **Nome:** Tratamento e corte para 8 caracteres, remoção de caracteres numéricos.
    * **Habilidade:** Restrição ao intervalo de 0 a 10.
* **Gerenciamento de Elenco:** O elenco é automaticamente mantido ordenado pela habilidade do jogador.
* **Definição Tática:** Permite definir o esquema com validação de regra de negócio (soma total deve ser 10, e cada linha deve ter entre 2 e 4 jogadores).
* **Montagem do Time Titular:** Seleciona automaticamente os melhores jogadores para o esquema tático definido.
* **Trocas:** Permite substituir um jogador existente por um novo, reordenando o elenco.
* **Interface de Terminal (CLI):** Uso da classe `Formatacao` para isolar a lógica de exibição, como o menu e o `esquema_tatico` ASCII.

---

## 🛠️ Como Executar

Este projeto requer apenas o **Python 3.x** e a estrutura de pastas correta (com os arquivos `__init__.py`).

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/CalebeAF02/Gerenciador-De-Hoteis---UNB.git](https://github.com/CalebeAF02/Gerenciador-De-Hoteis---UNB.git) # (Renomeie após clonar, se desejar)
    cd seu-novo-projeto-futebol
    ```

2.  **Instale os Pacotes Python (Se necessário):**
    O projeto usa apenas módulos padrão (como `abc` e `typing`), então nenhuma instalação externa é necessária.

3.  **Execute o Ponto de Entrada:**
    ```bash
    python main.py
    ```

---

## 📚 Exemplo de Uso (CLI)

O sistema irá iniciar o menu principal:

⚽ Sistema de Gerenciamento de Time - Iniciado! ⚽

=================================== --- MENU PRINCIPAL --- 1 (CONTRATAR_JOGADORES) 2 (TROCA_JOGADORES) 3 (Definir_Esquema_Tatico) 4 (Montar_o_Time) 5 (SAIR)
Entre com a opção:


---

## 🤝 Como Contribuir

**(Use a seção de Contribuição do seu modelo original do projeto C++, pois ela é genérica e aplica-se a qualquer projeto Git.)**

---

## 👤 Autor

Projeto desenvolvido por:

- [Calebe Alves](https://github.com/CalebeAF02) — Estudante do 7º Semestre de Ciência da Computação, Universidade de Brasília (UnB).

📎 Repositório: [Insira o Link do Repositório do Projeto de Futebol Aqui]
