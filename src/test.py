import pytest
from web import application
from cases.ping import *

@pytest.fixture
def app():
    return application
