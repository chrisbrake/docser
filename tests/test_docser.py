import pytest


@pytest.fixture()
def docser():
    """ Get docser for testing """
    import docser
    return docser


def test_import(docser):
    """ Test importable """
    assert docser
