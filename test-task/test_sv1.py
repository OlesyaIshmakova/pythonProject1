import pytest
@pytest.fixture(scope='session')
def run_rest_service():
    print('Start rest service1')
    yield
    print ('Stop rest service')

@pytest.fixture()
def cleanup():
    yield
    print('Cleanup')

def test_one(run_rest_service, cleanup):
    print('Test execution')
    assert 1 == 1

def test_two(run_rest_service, cleanup):
        print('Test execution')

def test_three(run_rest_service, cleanup):
    print('Test execution')