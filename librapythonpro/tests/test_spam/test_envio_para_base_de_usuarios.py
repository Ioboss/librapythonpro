from unittest.mock import Mock

import pytest

from librapythonpro.spam.enviador_de_email import Enviador
from librapythonpro.spam.main import EnviadorDeSpam
from librapythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Vitor', email='vtloboss@hotmail.com'),
            Usuario(nome='Sa', email='vtloboss@hotmail.com')
        ],
        [
            Usuario(nome='Vitor', email='vtloboss@hotmail.com'),
        ]
     ]
)
def teste_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vtloboss@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )
    assert len(usuarios) == enviador.enviar.call_count


def teste_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vitor', email='vtloboss@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vitor____@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )
    enviador.enviar.assert_called_once_with == (
        'vitor____@hotmail.com',
        'vtloboss@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )