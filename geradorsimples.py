#das bibliotecas random e string vamos importar somente o que vai nos ser util
#isso evita carregamentos desnecessarios.
from random import choice

from string import ascii_letters , digits

def gerar_senha (tamanho=8):
    caracteres=ascii_letters + digits # Letras e números
    senha = "".join (choice(caracteres) for _ in range(tamanho))
    return senha
# Solicita o tamanho da senha ao usuário
tamanho = int(input("qual o tamanho da senha?(exemplo :8):"))
# Gera e exibe a senha
senha_gerada = gerar_senha(tamanho)
print(f"sua senha gerada é : {senha_gerada}")
