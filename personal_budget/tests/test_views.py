import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index_returns_status_code_200(client):
    # WHEN
    response = client.get(reverse('index'))

    # THEN
    assert response.status_code == 200
