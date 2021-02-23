import pytest
from web import application
from cases.ping import *
from cases.avatar import *

@pytest.fixture
def app():
    return application
