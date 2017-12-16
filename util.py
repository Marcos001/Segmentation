
def _cor(cor):
    cores = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m',
        'ciano': '\033[36m',
        'magenta': '\033[35m',
        'amarelo': '\033[33m',
        'preto': '\033[30m',
        'branco': '\033[37m',
        'original': '\033[0;0m',
        'reverso': '0\33[2m',
        '': '\033[0;0m',
    }
    return cores[cor]

def porcentagem(_indice, n):
    por = (_indice*100)/n
    log = '\033[32m'+'(%i:%i) \033[0;0m<>\033[34m [ %.2f%s ] ''\033[0;0m' %(_indice,n,por,'%')
    #print(log)
    return log