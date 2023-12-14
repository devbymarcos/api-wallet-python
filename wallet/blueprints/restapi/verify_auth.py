from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    'secrete-token-1': 'john',
    'secrete-token-2': 'susan'
}


@auth.verify_token
def verify_token(token):
    pass
# TODO aqui vai a lógica para verificar o token
