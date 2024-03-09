from math import pi
import sys
import errno

erro = '\033[91m'
normal = '\033[0m'

def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(erro, "O raio deve ser um valor numérico.", normal)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo:', area)

#python -u "c:\Users\higor\OneDrive\Área de Trabalho\VsCode Testese\__pycache__\estrura controle\circulo.py"