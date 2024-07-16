import app

def test_hello():
    response = app.app.test_client().get('/')
    assert response.data == b'Hello, World! This is my Python web application.'
