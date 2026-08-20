import pytest
from rest_framework.test import APIClient

from cafes.models import Barrio, Cafe, Review, Reviewer

# Don't forget imports! (pytest, Barrio model)



@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def make_barrio():
    # 1. Define an inner function that accepts **kwargs
    def inner(**kwargs):
        # 2. Create a dictionary called 'defaults' with a valid
        #    'name' and 'slug'.
        defaults = {"name": "Defualt Barrio", "comuna": 1, "slug": "Default Slug"}
        # 3. Update 'defaults' with the contents of 'kwargs'
        #    (This allows the test to override the name if it wants)
        defaults.update(kwargs)
        return Barrio.objects.create(**defaults)

    # 5. Return the inner function (do not call it!)
    return inner


@pytest.fixture
def make_cafe(make_barrio):
    # 1. Define an inner function that accepts **kwargs
    def inner(**kwargs):
        # 2. Create a dictionary called 'defaults' with a valid
        #    'name' and 'barrio' (Cafe has no 'slug' field, only Barrio does)
        defaults = {
            "name": "Default Cafe",
            "barrio": make_barrio(),
        }
        # 3. Update 'defaults' with the contents of 'kwargs'
        #    (This allows the test to override the name if it wants)
        defaults.update(kwargs)
        return Cafe.objects.create(**defaults)

    # 5. Return the inner function (do not call it!)
    return inner
