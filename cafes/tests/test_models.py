import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from cafes.models import Barrio, Cafe, Review, Reviewer


@pytest.mark.django_db
def test_create_barrio():
    name = "Saavedra"
    expected_slug = "saavedra"
    # ACT: Create a Barrio with name="Palermo", slug="palermo"
    barrio = Barrio.objects.create(name=name, comuna=1, slug=expected_slug)
    # ASSERT: Check obj.name has the expected value
    #    Hint: use an assert statement, and == to compare
    assert barrio.name == name
    # ASSERT: Check obj.slug has the expected value
    assert barrio.slug == expected_slug
    # ASSERT: Check obj.id is not None
    assert barrio.id is not None


# Task 2: Barrio uniqueness


@pytest.mark.django_db
def test_create_duplicate_barrio_errors():
    # ARRANGE: Create Barrio(name="Belgrano", slug="belgrano")
    Barrio.objects.create(name="Belgrano", comuna=12, slug="belgrano")
    # ACT & ASSERT:
    # Open context (hint: with pytest.raises) expecting IntegrityError:
    with pytest.raises(IntegrityError):
        Barrio.objects.create(name="Belgrano", comuna=12, slug="belgrano")
        # Try to create ANOTHER Barrio with exact same name/slug


@pytest.mark.django_db
def test_create_review_raises_validation_error():
    # ARRANGE: A review needs a Cafe, which needs a Barrio:
    #          Create a Barrio -> Create a Cafe

    barrio_name = "Palermo"
    expected_slug = "palermo"
    barrio = Barrio.objects.create(name=barrio_name, comuna=1, slug=expected_slug)
    cafe = Cafe.objects.create(name="Cafe name", address="123 Street", barrio=barrio)

    reviewer = Reviewer.objects.create(name="Jack")

    with pytest.raises(ValidationError):
        review = Review.objects.create(
            cafe=cafe, reviewer=reviewer, rating=6, comment="good cafe"
        )
        review.full_clean()

    # ACT & ASSERT:
    # Open context expecting ValidationError:
    # Try to create Review(cafe=cafe, rating=6)


# Remember to use .full_clean() to validate the inputs
