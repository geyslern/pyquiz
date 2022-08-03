from django.urls import reverse
from pytest import fixture
from quiz.django_assertions import assert_contains


@fixture
def response(client):
    return client.get(reverse("base:home"))


def test_status_200(response):
    assert response.status_code == 200


def test_index_page_title(response):
    assert_contains(response, "Quiz - DevPro")
