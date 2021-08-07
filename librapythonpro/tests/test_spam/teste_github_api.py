from unittest.mock import Mock

import pytest

from librapythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/77992564?v=4'
    resp_mock.json.return_value = {
        'login': 'Ioboss', 'id': 779925,
        'avatar_url': url,
    }
    get_mock = mocker.patch('librapythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_usuario('Ioboss')
    assert avatar_url == url


def teste_buscar_avatar_integracao():
    url = github_api.buscar_usuario('ioboss')
    assert 'https://avatars.githubusercontent.com/u/77992564?v=4' == url
