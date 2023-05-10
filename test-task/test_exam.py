import pytest
from helpers import print_green, print_cyan, print_blue

@pytest.fixture(scope='session')
def run_rest_service():
    print_blue('Start rest service')
    yield
    print_blue('Stop rest service')

@pytest.fixture()
def cleanup():
    yield
    print_green('Cleanup')

def test_one(run_rest_service, cleanup):
    print_cyan('Test execution 1')


def test_two(run_rest_service, cleanup):
    print_cyan('Test execution2')

def test_three(run_rest_service, cleanup):
    print_green('Test execution3')