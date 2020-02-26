import requests



def test_counter():
    requests.delete("http://localhost:8888/admin/storage")

    counter = requests.post('http://localhost:8000/http://api.com/counter').json()
    assert 1 == counter['count']

    counter = requests.post('http://localhost:8000/http://api.com/counter', json={'set': 10}).json()
    assert 10 == counter['count']

    counter = requests.post('http://localhost:8000/http://api.com/counter').json()
    assert 11 == counter['count']


def test_hello():
    requests.delete("http://localhost:8888/admin/storage")

    text = requests.get('http://localhost:8000/http://api.com/hello').text
    assert 'Hello, my friend' == text

    text = requests.get('http://localhost:8000/http://api.com/hello?name=Spock').text
    assert 'Hello, Spock' == text
