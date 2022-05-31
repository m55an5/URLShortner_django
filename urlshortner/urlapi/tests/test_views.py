from django.contrib.auth.models import User
import pytest
from django.urls import reverse
from urlapi.models import URLShortner
from urlapi.serializers import URLShortnerSerializer

MAX_CODE_LENGTH=6

def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"


# POST ENDPOINT

@pytest.mark.django_db
def test_create_short_url_valid_input(client):

    url = reverse('create-short-url')
    original_url = 'http://www.abc.com.au'
    data = {'original_url' : original_url}
    response = client.post( url, 
                            data=data, 
                            content_type='application/json'
                        )
    
    assert response.status_code == 200
    assert response.data['data']['original_url'] == original_url
    assert len(response.data['data']['short_url']) == MAX_CODE_LENGTH
    

@pytest.mark.django_db
def test_create_short_url_valid_encoded_input(client):

    url = reverse('create-short-url')
    original_url = 'https://twitter.com/crackfang%2Fstatus%2F1402494889682632716'
    expected_url = 'https://twitter.com/crackfang/status/1402494889682632716'
    data = {'original_url' : original_url}
    response = client.post( url, 
                            data=data, 
                            content_type='application/json'
                        )
    
    assert response.status_code == 200
    assert response.data['data']['original_url'] == expected_url


@pytest.mark.django_db
def test_create_short_url_invalid_input(client):

    url = reverse('create-short-url')
    original_url = 'abc'
    data = {'original_url' : original_url}
    response = client.post( url, 
                            data=data, 
                            content_type='application/json'
                        )

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_short_url_multiple_same_url_request(client):

    url = reverse('create-short-url')
    original_url = 'http://www.abc.com.au'
    data = {'original_url' : original_url}
    response_1 = client.post( url, 
                            data=data, 
                            content_type='application/json'
                        )

    response_2 = client.post( url, 
                            data=data, 
                            content_type='application/json'
                        )
    
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_2.data['data']['short_url'] != response_1.data['data']['short_url']
    


# GET ENDPOINT

@pytest.mark.django_db
def test_get_short_url_valid_input(client):

    post_url = reverse('create-short-url')
    original_url = 'http://www.abc.com.au'
    data = {'original_url' : original_url}
    response = client.post( post_url, 
                            data=data, 
                            content_type='application/json'
                        )
    
    short_url = response.data['data']['short_url'] 
    get_url = reverse('get-short-url', kwargs={'short_url':short_url})
    response = client.get(get_url)
    
    assert response.status_code == 302
    assert response.url == original_url


@pytest.mark.django_db
def test_get_short_url_invalid_input(client):

    post_url = reverse('create-short-url')
    original_url = 'http://www.abc.com.au'
    data = {'original_url' : original_url}
    response = client.post( post_url, 
                            data=data, 
                            content_type='application/json'
                        )
    
    short_url = "0fake1"
    get_url = reverse('get-short-url', kwargs={'short_url':short_url})
    response = client.get(get_url)
    
    assert response.status_code == 404


    
