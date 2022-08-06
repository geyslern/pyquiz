from django.urls import reverse
import pytest
from quiz.django_assertions import assert_contains
from quiz.base import facade


@pytest.fixture
def response_without_param(client, request):
    marker = request.node.get_closest_marker("request_data")
    view_name = marker.args[0]
    return client.get(reverse(view_name))


@pytest.fixture
def perguntas_response(client, request):
    marker = request.node.get_closest_marker("request_data")
    view_name = marker.args[0]
    indice_pergunta = marker.args[1]
    return client.get(reverse(view_name, args=(indice_pergunta,)))


@pytest.mark.request_data("base:home")
def test_home_status_200(response_without_param):
    assert response_without_param.status_code == 200


@pytest.mark.request_data("base:home")
def test_index_page_title(response_without_param):
    assert_contains(response_without_param, "Quiz - DevPro")


@pytest.mark.request_data("base:perguntas", 1)
def test_perguntas_status_200(perguntas_response):
    assert perguntas_response.status_code == 200


@pytest.mark.request_data("base:perguntas", 2)
def test_pergunta_indice(perguntas_response):
    assert_contains(perguntas_response, "Questão 2")


@pytest.mark.request_data("base:classificacao")
def test_classificacao_status_200(response_without_param):
    assert response_without_param.status_code == 200


@pytest.mark.request_data("base:classificacao")
def test_classificacao_page_title(response_without_param):
    assert_contains(response_without_param, "Ranking")


@pytest.mark.request_data("base:classificacao")
def test_classificacao_ranking(response_without_param):
    jogador = facade.buscar_jogador()
    assert_contains(response_without_param, f'<h2 class="status-player">{jogador["classificacao"]}º</h2>')
