import pytest

# This test doesn't need the DB, it's just checking the fixture works.
def test_client_fixture_exists(client):
    assert client is not None

@pytest.mark.django_db
def test_get_nonexistent_cafe_returns_404(client):
    # ARRANGE: Nothing needed. The DB is empty.
    
    # ACT: Make a GET request to a URL with a fake ID
    response = client.get("/cafes/999")
    # ASSERT: Check the response.status_code is 404
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_cafe_via_api(client, make_barrio):
    # ARRANGE
    # 1. Use your fixture to create a barrio (we need its ID)
    barrio = make_barrio()

    # 2. Define a valid payload dictionary (name, address, barrio.id)
    payload = {'name':'New Cafe','address': '123 street', 'barrio_name':barrio.name}
    # ACT
    # 3. Use the client to POST the payload to the "/cafes/" URL
    response = client.post(path="/api/cafes/", data=payload)

    # ASSERT
    # 4. Check the response.status_code is 201
    assert response.status_code == 201

    # 5. Check response.data["name"] is correct


    # 6. Check Cafe.objects.count() is 1 (proves DB write)
