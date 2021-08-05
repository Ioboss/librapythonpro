from librapythonpro.spam.modelos import Usuario


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome='Vitor', email='vtloboss@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def teste_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Vitor', email='vtloboss@hotmail.com'),
        Usuario(nome='Sa', email='vtloboss@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

