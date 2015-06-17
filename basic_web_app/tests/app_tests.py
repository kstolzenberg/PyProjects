from nose.tools import * 
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check for the 404 assert_response
    resp = app.request("/")
    assert_response(resp, status="404")

    # test first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # check default values for the form
    resp = app.request('/hello', method="POST")
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'name': "kron", 'greet':'hola'}
    resp = app.request('/hello', method="POST", data=data)
    assert_response(resp, contains='kron')