import pytest


from librapythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['vtloboss@hotmail.com', 'foo@bar.com.br']

                         )
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['vtloboss@hotmail.com', 'foo@bar.com.br']
    resultado = enviador.enviar(
        destinatario,
        'vitor____@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )
    assert destinatario in resultado


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
    assert remetente in resultado
