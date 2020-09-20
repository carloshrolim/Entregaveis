import hashlib
import time

timestamp = int(time.time())
nounce = 0
mensagem = 'Toranja manda 32 eth para Carlos'
dificuldade = 5

while True:
    nounce = nounce + 1
    bloco = (str(timestamp), str(nounce), mensagem)
    bloco = '|'.join(bloco)
    hash = hashlib.sha256(bloco.encode('ascii')).hexdigest()
    qtd_zeros = len(hash) - len(hash.lstrip('0'))
    if(qtd_zeros == dificuldade):
        break
print('Bloco: {} \nHash: {} \nDificuldade: {}'.format(bloco, hash, dificuldade))

