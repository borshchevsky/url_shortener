from shortener import create_app

client = create_app().test_client()


def test_redirect():
    url = 'http://example.com'
    r = client.post('/', json={'url': url})
    short = r.json['short_url'].split('/')[-1]
    r = client.get(f'/{short}')
    assert (r.status_code == 302)


def test_new_url():
    for i in range(5):
        url = f'http://testurl{i}.com'
        r = client.post('/', json={'url': url})
        assert (r.status_code == 200)
        assert (len(r.json['short_url'].split('/')[-1]) == 5)


def test_empty_url():
    r = client.post('/', json={'url': ''})
    assert (r.status_code == 200)
    assert (r.json['url'][0] == 'Not a valid URL.')


def test_int_url():
    r = client.post('/', json={'url': 42})
    assert (r.status_code == 200)
    assert (r.json['url'][0] == 'Not a valid string.')
