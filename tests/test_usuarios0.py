import requests

ENDPOINT = "https://compassuol.serverest.dev/"

def test_listar_todos_os_usuarios_com_sucesso():
    response = requests.get(ENDPOINT + "usuarios")
    assert response.status_code == 200
    assert response.json()["quantidade"] > 0

def test_cadastrar_usuario_com_dados_validos():
    payload = {
        "nome": "João Silva",
        "email": "joao.silva@example.com"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Cadastro realizado com sucesso"

def test_impedir_cadastro_de_usuario_com_email_duplicado():
    payload = {
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@example.com"
    }
    # Primeiro cadastro
    response1 = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response1.status_code == 201
    # Segundo cadastro com o mesmo email
    response2 = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response2.status_code == 400
    assert response2.json()["message"] == "Este email já está sendo usado"

def test_impedir_cadastro_sem_campo_nome():
    payload = {
        "email": "maria.oliveira@example.com"
    }
    response =  requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Nome é obrigatório"

def test_impedir_cadastro_sem_campo_email():
    payload = {
        "nome": "Maria Oliveira"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Email é obrigatório"

def test_impedir_cadastro_sem_campo_password():
    payload = {
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@example.com"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Password é obrigatório"

def test_impedir_cadastro_sem_campo_administrador():
    payload = {
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@example.com",
        "password": "senha123"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Administrador é obrigatório"


def test_buscar_usuario_por_id_valido():
    # Primeiro, cadastrar um usuário para obter um ID válido
    payload = {
        "nome": "Carlos Pereira",
        "email": "carlos.pereira@example.com",
        "password": "senha123",
        "administrador": "true"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 201
    user_id = response.json()["_id"]

    # Agora, buscar o usuário pelo ID
    response = requests.get(ENDPOINT + f"usuarios/{user_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Carlos Pereira"

def test_buscar_usuario_por_id_inexistente():
    response = requests.get(ENDPOINT + "usuarios/1234567890abcdef12345678")
    assert response.status_code == 404
    assert response.json()["message"] == "Nenhum resultado encontrado para esse id"

def test_atualizar_dados_de_usuario_existente():
    # Primeiro, cadastrar um usuário para obter um ID válido
    payload = {
        "nome": "Ana Souza",
        "email": "ana.souza@example.com"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 201
    user_id = response.json()["_id"]
    # Agora, atualizar os dados do usuário
    update_payload = {
        "nome": "Ana Souza Silva",
        "email": "ana.souza.silva@example.com"
    }
    response = requests.put(ENDPOINT + f"usuarios/{user_id}", json=update_payload)
    assert response.status_code ==  200
    assert response.json()["message"] == "Registro alterado com sucesso"

def test_cadastrar_usuario_via_put_quando_id_nao_existe():
    update_payload = {
        "nome:": "Pedro Lima",
        "email": "pedro.lima@example.com"
    }
    response =  requests.put(ENDPOINT + "usuarios/1234567890abcdef12345678", json=update_payload)
    assert response.status_code ==  404
    assert response.json()["message"] == "Nenhum resultado encontrado para esse id"

def test_excluir_usuario_com_sucesso():
    # Primeiro, cadastrar um usuário para obter um ID válido
    payload = {
        "nome": "Lucas Fernandes",
        "email": "lucas.fernandes@example.com"
    }
    response = requests.post(ENDPOINT + "usuarios", json=payload)
    assert response.status_code == 201
    user_id = response.json()["_id"]

    # Agora, excluir o usuário
    response = requests.delete(ENDPOINT + f"usuarios/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Registro excluído com sucesso"

def test_tentar_excluir_usuario_inexistente():
    response = requests.delete(ENDPOINT + "usuarios/1234567890abcdef12345678")
    assert response.status_code == 404
    assert response.json()["message"] == "Nenhum resultado encontrado para esse id"
