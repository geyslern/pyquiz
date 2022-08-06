from django.urls import path
from quiz.base.views import home, perguntas, classificacao


app_name = "base"

urlpatterns = [
    path("", home, name="home"),
    path("perguntas/<int:indice>", perguntas, name="perguntas"),
    path("classificacao", classificacao, name="classificacao"),
]
