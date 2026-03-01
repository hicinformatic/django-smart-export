import pytest
import django
from django.conf import settings
from django.db import connection
from django.apps import apps


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    django.setup()


def test_django_starts():
    assert settings.configured
    assert apps.is_installed("django_smart_export")


def test_database():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        assert result[0] == 1
