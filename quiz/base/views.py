from django.shortcuts import render
from quiz.base import facade


def home(request):
    return render(request, "base/index.html")


def perguntas(request, indice):
    contexto_pergunta = {"indice_da_questao": indice}
    return render(request, "base/game.html", context=contexto_pergunta)


def classificacao(request):
    jogador = facade.buscar_jogador()
    ranking = facade.listar_ranking()
    contexto_classificacao = {
        "jogador": jogador,
        "ranking": ranking,
    }
    return render(request, "base/classificacao.html", context=contexto_classificacao)
