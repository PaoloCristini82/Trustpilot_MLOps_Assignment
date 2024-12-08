import pytest
import json
import os
import sys
sys.path.append("../app")
from main import app

@pytest.fixture(autouse=True)
def set_test_env():

    # Set the environment variable to 'test' before the test runs
    os.environ['RUNNING_AS_TEST'] = 'true'
    yield
    
    # Reset the environment variable after the test
    del os.environ['RUNNING_AS_TEST']

@pytest.fixture
def client():

    with app.test_client() as client:
        yield client

def test_predict(client):

    # Example review for testing
    review = {
        "title": "Fantastic Book!",
        "text": "I really enjoyed the depth of the characters."
    }
    
    response = client.post('/predict', json=review)
    response_data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'score' in response_data
    assert 'sentiment' in response_data
    assert isinstance(response_data['score'], float)
    assert isinstance(response_data['sentiment'], str)
