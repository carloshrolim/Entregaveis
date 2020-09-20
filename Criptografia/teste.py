import starkbank

chave_privada, chave_publica = starkbank.key.create("sample/destination/path")

print(chave_privada)
print(chave_publica)