import pytest
import requests
from faker import Faker

BASE_URL = "https://compassuol.serverest.dev"

@pytest.fixture(scope="function")
def fake_data():
    """Retorna uma instância do Faker configurada para PT-BR."""
    return Faker('pt_BR')

@pytest.fixture(scope="function")
def usuario_dinamico(fake_data):
    """Gera um dicionário com dados de usuário válidos, mas sem cadastrar."""
    return {
        "nome": fake_data.name(),
        "email": fake_data.email(),
        "password": fake_data.password(),
        "administrador": "true"
    }

@pytest.fixture(scope="function")
def usuario_cadastrado(usuario_dinamico):
    """
    Fixture de suporte: Cadastra um usuário na API e retorna os dados dele
    junto com o _id gerado pela ServeRest. Útil para GET por ID, PUT e DELETE.
    """
    url = f"{BASE_URL}/usuarios"
    resposta = requests.post(url, json=usuario_dinamico)
    
    assert resposta.status_code == 201, "Falha ao criar usuário de suporte na fixture"
    
    dados_usuario = usuario_dinamico.copy()
    dados_usuario["_id"] = resposta.json()["_id"]
    
    return dados_usuario