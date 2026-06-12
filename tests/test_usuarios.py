import requests

BASE_URL = "https://compassuol.serverest.dev"

# --- CENÁRIOS DE LISTAGEM ---

def test_listar_todos_os_usuarios_com_sucesso():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    
    assert resposta.status_code == 200
    dados = resposta.json()
    assert "quantidade" in dados
    assert "usuarios" in dados
    assert isinstance(dados["usuarios"], list)


# --- CENÁRIOS DE CADASTRO ---

def test_cadastrar_usuario_com_dados_validos(usuario_dinamico):
    resposta = requests.post(f"{BASE_URL}/usuarios", json=usuario_dinamico)
    
    assert resposta.status_code == 201
    assert resposta.json()["message"] == "Cadastro realizado com sucesso"
    assert "_id" in resposta.json()


def test_impedir_cadastro_de_usuario_com_email_duplicado(usuario_cadastrado):
    # Tenta usar o mesmo e-mail do usuário que já foi cadastrado pela fixture
    payload_duplicado = {
        "nome": "Outro Nome",
        "email": usuario_cadastrado["email"],
        "password": "password123",
        "administrador": "true"
    }
    
    resposta = requests.post(f"{BASE_URL}/usuarios", json=payload_duplicado)
    
    assert resposta.status_code == 400
    assert resposta.json()["message"] == "Este email já está sendo usado"


def test_impedir_cadastro_sem_campo_nome(usuario_dinamico):
    del usuario_dinamico["nome"] # Remove o campo obrigatório
    
    resposta = requests.post(f"{BASE_URL}/usuarios", json=usuario_dinamico)
    
    assert resposta.status_code == 400
    assert "nome" in resposta.json() # ServeRest retorna validação do campo


# --- CENÁRIOS DE BUSCA POR ID ---

def test_buscar_usuario_por_id_valido(usuario_cadastrado):
    user_id = usuario_cadastrado["_id"]
    resposta = requests.get(f"{BASE_URL}/usuarios/{user_id}")
    
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["nome"] == usuario_cadastrado["nome"]
    assert dados["email"] == usuario_cadastrado["email"]


def test_buscar_usuario_por_id_inexistente():
    id_ficticio = "id_nao_existe_123"
    resposta = requests.get(f"{BASE_URL}/usuarios/{id_ficticio}")
    
    assert resposta.status_code == 400
    assert resposta.json()["message"] == "Usuário não encontrado"


# --- CENÁRIOS DE ATUALIZAÇÃO (PUT) ---

def test_atualizar_dados_de_usuario_existente(usuario_cadastrado, fake_data):
    user_id = usuario_cadastrado["_id"]
    payload_atualizado = {
        "nome": fake_data.name(),
        "email": fake_data.email(),
        "password": "nova_senha_123",
        "administrador": "false"
    }
    
    resposta = requests.put(f"{BASE_URL}/usuarios/{user_id}", json=payload_atualizado)
    
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro alterado com sucesso"


# --- CENÁRIOS DE EXCLUSÃO (DELETE) ---

def test_excluir_usuario_com_sucesso(usuario_cadastrado):
    user_id = usuario_cadastrado["_id"]
    resposta = requests.delete(f"{BASE_URL}/usuarios/{user_id}")
    
    assert resposta.status_code == 200
    assert resposta.json()["message"] == "Registro excluído com sucesso"