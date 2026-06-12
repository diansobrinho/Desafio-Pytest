# ServeRest API Automation - Usuários (Pytest)

Este projeto contém a automação de testes para o endpoint `/usuarios` da API ServeRest, utilizando Python e Pytest.

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* Python 3.10 ou superior
* Pip (Gerenciador de pacotes do Python)

## 🚀 Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone <url-do-seu-repositorio>
   cd serverest-pytest-automation

   # 🧪 ServeRest API Test Automation - Endpoint `/usuarios`

Este repositório contém uma suíte de testes automatizados robusta e resiliente desenvolvida para validar as regras de negócio, contratos e comportamentos do endpoint de Usuários da API ServeRest.

O foco principal do projeto foi aplicar padrões modernos de engenharia de testes, garantindo testes atômicos, independentes de estado e imunes a conflitos de concorrência através de geração de dados dinâmicos.

### 🎯 Diferenciais Técnicos Aplicados:
* **Massa de Dados 100% Dinâmica:** Integração com a biblioteca `Faker` para mitigar conflitos de e-mails duplicados em execuções paralelas.
* **Arquitetura Escalável (Fixtures):** Centralização de setups, cleanups e estados transitórios no arquivo `conftest.py`.
* **Isolamento Total:** Cada teste cria e gerencia seu próprio ciclo de vida, sem dependências lineares.
* **Asserts Granulares:** Validações rigorosas de HTTP Status Codes e estruturas/contratos de payloads JSON.
* **Cobertura Abrangente:** Mais de 10 cenários cobrindo fluxos felizes, exceções, validações de campos obrigatórios e comportamentos idempotentes (GET, POST, PUT, DELETE).
