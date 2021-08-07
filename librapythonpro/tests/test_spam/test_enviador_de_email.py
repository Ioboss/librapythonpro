import pytest


from librapythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['vtloboss@hotmail.com', 'foo@bar.com.br']

                         )
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'vitor____@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'vitor']
                         )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'vitor____@hotmail.com',
            'Estudos Python',
            'Chegando na primeira vaga'
        )
