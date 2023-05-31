def pegar_nome_sobrenome():
    nome = input('Digite seu nome:')
    sobrenome = input('Digite seu sobrenome:')
    nome_completo = [nome, sobrenome]
    return nome_completo

def pegar_idade():
    idade = int(input('Digite seu ano de nascimento: (formato aaaa)'))
    return (2023 - idade)

nome_completo = pegar_nome_sobrenome()
idade = pegar_idade()
pessoa = [nome_completo[0], nome_completo[1], idade]
print('Seu nome completo é', pessoa[0], pessoa[1], 'e sua idade é', pessoa[2], 'anos')