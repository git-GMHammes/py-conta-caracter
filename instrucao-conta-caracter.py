#  '12345'.isdigit() verdadeiro para numero
#  '1234.5'.isdigit() falso para numero
#  '12345abc'.isdigit() falso para numero
#  '12345abc'.isalnum() verdadeiro para alphanumerico

def informa1():
    print(f'\n Digite o seu primeiro nome, sem espaço, numeros serão aceitos')
    var1: str = input("\n Com a primeira letra Maiúscula: ")
    verificaNome1(var1)
    return var1


def verificaNome1(var2):
    if var2.istitle():
        print(f'\n O Valor digitado: {var2}, atende ao que lhe foi solicitado')
        if len(var2) <= 4:
            print(f'\n Seu nome {var2} é muito curto')
        elif 5 <= len(var2) <= 6:
            print(f'\n O Seu nome {var2} é normal')
        elif len(var2) > 6:
            print(f'\n Seu nome {var2} é muito grande')
        else:
            print(f'\n Algo inesperado aconteceu')
    else:
        print(
            f'\n O Valor digitado: {var2}, NÃO atende ao que lhe foi solicitado')
        informa1()
    exit('\n Fim do Programa')


informa1()
