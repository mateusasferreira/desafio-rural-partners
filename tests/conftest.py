import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return User.objects.create(username="teste", password="teste")


@pytest.fixture
def test_user_token(test_user):
    return Token.objects.create(user=test_user)


@pytest.fixture
def api_client_authorized(api_client, test_user_token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + test_user_token.key)
    return api_client
