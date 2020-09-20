from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey

# Gerando as chaves
chave_privada = PrivateKey()
chave_publica = chave_privada.publicKey()

mensagem = "Segredo secreto :O"

# Gerando a assinatura
carloscabral = Ecdsa.sign(mensagem,chave_privada)

# Verificando
Resposta = Ecdsa.verify(mensagem,carloscabral,chave_publica)
print(Resposta)
