from librapythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'vtloboss@hotmail.com',
        'vitor____@hotmail.com',
        'Estudos Python',
        'Chegando na primeira vaga'
    )
    assert 'vtloboss@hotmail.com' in resultado
