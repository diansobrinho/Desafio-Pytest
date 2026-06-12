# 🧪 ServeRest API Test Automation - Endpoint `/usuarios`

Repositório dedicado à automação de testes end-to-end (E2E) para o gerenciamento de usuários da API pública **ServeRest**. O foco absoluto deste projeto é aplicar os padrões mais rigorosos de engenharia de software voltados para testes (QA/Automation), garantindo resiliência, alta granularidade e imunidade a falsos positivos/negativos.

---

## 🎯 Diferenciais Técnicos e Arquitetura

Para evitar os problemas mais comuns em automação de APIs (como testes flutuantes, concorrência de dados e acoplamento), o projeto foi desenhado sob os seguintes pilares:

* **Isolamento de Estado (Test Independence):** Nenhum teste depende do resultado ou da execução de outro. O sucesso ou falha de uma validação não gera efeito cascata na suíte.
* **Massa de Dados Volátil e Dinâmica:** Integração com o ecossistema `Faker (pt_BR)` para injeção de payloads em tempo de execução, garantindo que restrições de unicidade (como e-mails duplicados) nunca quebrem execuções paralelas.
* **Injeção de Dependências via Fixtures:** Gerenciamento centralizado do ciclo de vida dos dados (setup e transições de estado) através do `conftest.py`, otimizando a legibilidade dos scripts.
* **Verificação Multipartite (Asserts Granulares):** Cada caso de teste não se limita a checar o HTTP Status Code; ele inspeciona rigorosamente o contrato do JSON, tipos de dados e mensagens de propriedades específicas da API.

---

## 🏗️ Estrutura do Projeto

O projeto adota uma estrutura limpa e modular, separando configurações globais dos casos de teste:

📂 serverest-pytest-automation
├── 📂 tests
│   ├── conftest.py          # Fixtures globais, controle de escopo e geradores Faker
│   └── test_usuarios.py     # Suíte de testes automatizados (>10 cenários)
├── .gitignore               # Proteção contra artefatos locais (__pycache__, venv)
├── pytest.ini               # Sobrecarga de configurações globais do Pytest
├── README.md                # Documentação técnica descritiva do projeto
└── requirements.txt         # Manifesto de dependências com versões fixadas (pinning) 

## 📊 Matriz de Cenários Testados

A suíte cobre exaustivamente o ciclo CRUD do endpoint /usuarios, totalizando 13 cenários de teste independentes:

| ID | Operação | Cenário de Teste | Objetivo da Validação | Status Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **01** | `GET` | `test_listar_todos_os_usuarios_com_sucesso` | Valida integridade da listagem global, checando chaves primárias e tipos estruturais da resposta. | `200 OK` |
| **02** | `POST` | `test_cadastrar_usuario_com_dados_validos` | Valida fluxo principal de criação de usuário com payload dinâmico. | `201 Created` |
| **03** | `POST` | `test_impedir_cadastro_de_usuario_com_email_duplicado` | Garante a regra de negócio que impede colisões de chaves de e-mail no banco. | `400 Bad Request` |
| **04** | `POST` | `test_impedir_cadastro_sem_campo_nome` | Contrato: Valida payload rejeitado ao omitir campo obrigatório nome. | `400 Bad Request` |
| **05** | `POST` | `test_impedir_cadastro_sem_campo_email` | Contrato: Valida payload rejeitado ao omitir campo obrigatório email. | `400 Bad Request` |
| **06** | `POST` | `test_impedir_cadastro_sem_campo_password` | Contrato: Valida payload rejeitado ao omitir campo obrigatório password. | `400 Bad Request` |
| **07** | `POST` | `test_impedir_cadastro_sem_campo_administrador` | Contrato: Valida payload rejeitado ao omitir campo obrigatório administrador. | `400 Bad Request` |
| **08** | `GET` | `test_buscar_usuario_por_id_valido` | Garante a recuperação pontual de um registro usando o _id persistido dinamicamente. | `200 OK` |
| **09** | `GET` | `test_buscar_usuario_por_id_inexistente` | Valida o comportamento defensivo do sistema ao pesquisar hash inválido/inexistente. | `400 Bad Request` |
| **10** | `PUT` | `test_atualizar_dados_de_usuario_existente` | Valida a alteração completa dos dados cadastrais de um usuário ativo. | `200 OK` |
| **11** | `PUT` | `test_cadastrar_usuario_via_put_quando_id_nao_existe` | Valida a especificação HTTP do PUT (Upsert): se o ID não existe, cria um novo. | `201 Created` |
| **12** | `DELETE` | `test_excluir_usuario_com_sucesso` | Garante a remoção lógica/física do usuário e liberação dos seus dados. | `200 OK` |
| **13** | `DELETE` | `test_tentar_excluir_usuario_inexistente` | Valida idempotência do DELETE ao tentar remover um ID que não consta na base. | `200 OK` |

## 🛠️ Pré-requisitos Tecnológicos

Antes de inicializar a execução, certifique-se de possuir o ambiente configurado:

* Python 3.10 ou superior

* Pip (Gerenciador de pacotes nativo do Python)

* Virtualenv (Mecanismo de isolamento de dependências local)

## 🚀 Instalação e Configuração

Siga os passos abaixo no terminal para clonar o repositório e preparar o ambiente local de testes:

1. **Clonar o Repositório e Acessar a Pasta:**
   ```bash
   git clone <url-do-seu-repositorio>
   cd serverest-pytest-automation

2. **Provisionar o Ambiente Virtual (Venv):**
   ```bash
   python -m venv venv
   
3. **Ativar o Ambiente Virtual:**

    * No Linux/macOS:

       ```Bash
       source venv/bin/activate
       No Windows (Git Bash):
       
    * No Windows (Git Bash):
      
       ```Bash
       source venv/Scripts/activate

    * No Windows (PowerShell):

       ```Bash
       .\venv\Scripts\Activate.ps1
       
4. **Instalar Dependências Escrupulosamente Fixadas:**

   ```Bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

## 🧪 Estratégias de Execução dos Testes

O Pytest permite diferentes abordagens de execução a depender do seu objetivo no fluxo de Integração Contínua (CI):

Execução Padrão (Verborragia Ativada)
Varre o diretório, localiza os arquivos sob o padrão do pytest.ini e executa detalhando o nome de cada teste e seu respectivo resultado:

    ```Bash
    python -m pytest -v

Execução com Captura de Output (Debugging)
Evita que o Pytest mascare saídas padrões do console (stdout/stderr), ideal para visualizar prints ou logs adicionais em caso de falha:

    ```Bash
    python -m pytest -s -v

Execução Filtrada por Expressão Regular (Keyword Match)
Caso queira executar apenas os testes relacionados a uma operação específica, como testes de exclusão/deletar:

    ```Bash
    python -m pytest -v -k "excluir"

Execução Parando na Primeira Falha (Fail-Fast)
Ideal para rotinas de smoke testing rápidos, onde o primeiro erro detectado deve interromper o processo imediatamente:

    ```Bash
    python -m pytest -x
