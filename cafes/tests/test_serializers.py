import pytest
from cafes.serializers import CafeSerializer, ReviewSerializer
from cafes.models import Review, Reviewer, Tag
from unittest.mock import Mock

@pytest.mark.django_db
def test_cafe_serializer_correctly_formats_tagline(make_cafe):
    # ARRANGE
    # Use your fixture to create a cafe (no reviews yet)
    cafe = make_cafe()
    # ACT
    serializer = CafeSerializer(instance=cafe)
    # Instantiate the serializer with 'instance=your_cafe_object'
    # Extract the data using '.data'
    data = serializer.data

    # ASSERT
    # Check that data['name'] matches the name you gave the factory
    assert data['name'] == 'Default Cafe'
    # Check that data['tagline'] equals the expected string for 0 reviews
    assert data['tagline'] == 'Be the first to visit!'



@pytest.mark.django_db
def test_review_serializer_rejects_invalid_rating(make_cafe):
    # ARRANGE
    # 1. Create a cafe using your fixture (we need a valid ID)
    cafe = make_cafe()

    # 2. Prepare a payload dictionary with:
    #    - cafe: The ID of the cafe you just created
    #    - comment: "Some string"
    #    - rating: 10 (This is the invalid part we want to test)
    payload = {'cafe':1, 'comment': 'great', 'rating': 2}

    # ACT
    # Instantiate the serializer with 'data=payload'
    serializer = ReviewSerializer(data=payload)
    # ASSERT
    # Check that serializer.is_valid() is strictly False
    assert serializer.is_valid() == False
   
@pytest.mark.django_db
def test_tagline_is_hidden_gem_for_one_review(make_cafe):
    # ARRANGE
    # 1. Use your fixture to create a cafe
    cafe = make_cafe()

# 2. Manually create ONE review linked to that cafe
    reviewer = Reviewer.objects.create(name="Joaco")
    Review.objects.create(cafe=cafe, reviewer=reviewer, rating = 5, comment = 'good')

    # ACT
    # 3. Serialize the cafe instance to get the data dictionary
    data = CafeSerializer(instance=cafe).data
    # ASSERT
    # 4. Check the 'tagline' field equals "Hidden gem"
    assert data['tagline'] == 'Hidden gem!'


@pytest.mark.django_db
def test_tagline_is_local_favorite_for_six_reviews(make_cafe):
    # ARRANGE
    # 1. Use your fixture to create a cafe
    cafe = make_cafe()
    # 2. Create SIX reviews linked to that cafe
    #    (Hint: Use a python 'for' loop to repeat the creation step)
    for _ in range(6):
        reviewer = Reviewer.objects.create(name='Jacobo')
        review = Review.objects.create(cafe = cafe, reviewer=reviewer,comment='good', rating=4)
        
    # ACT
    # 3. Serialize the cafe instance
    data = CafeSerializer(instance=cafe).data
    # ASSERT
    # 4. Check the 'tagline' field equals "Local favorite!"
    assert data['tagline'] == 'Local favourite!'



@pytest.mark.django_db
def test_cafe_serializer_reuses_existing_tags(make_barrio, make_cafe):
    # ARRANGE
    # 1. Create a Barrio (dependency)
    barrio = make_barrio()
    # 2. Manually create a Tag object named "Cozy"
    Tag.objects.create(name='Cozy')
    # 3. Create a dictionary payload for a new Cafe
    #    IMPORTANT: Include "Cozy" inside the "tag_names" list
    payload = {'name':'New Cafe','barrio_name':barrio.name, 'address': '123 street', 'tag_names':['Cozy']}
    # ACT
    # 1. Instantiate serializer with data=payload
    serializer = CafeSerializer(data=payload)
    # 2. Call .is_valid()
    assert serializer.is_valid() == True
    # 3. Call .save() to write to the DB
    serializer.save()
    # ASSERT
    # 1. Check that the total count of Tags in the DB is still 1
    #    (If logic failed, it would be 2)
    assert Tag.objects.count() == 1
    assert serializer.instance.tag.first().name == "Cozy"


def test_tagline_logic_with_mocked_cafe():
    # ARRANGE
    # 1. Create a Mock object, and assign it to a variable (e.g. mock_cafe)
    #    Check out the unittest documentation for examples
    mock_cafe = Mock()
    # 2. Configure ONLY the attribute the method needs
    mock_cafe.review_count = 100
    
    # ACT
    # 3. Instantiate the serializer (it won’t need any data yet!)
    serializer = CafeSerializer()
    # ACT
    # 4. Call the method on the serializer we want to test directly, passing our mock object
    #    (get_tagline with our mock_cafe as the argument)
    response = serializer.get_tagline(mock_cafe)
    # ASSERT
    # 4. Check the return value is the expected string
    assert response == 'Local favourite!'