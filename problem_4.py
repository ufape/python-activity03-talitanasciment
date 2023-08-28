# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 4
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
O valor inteiro da entrada deve estar N (0 < N < 46).
Exemplo:
Série de Fibonacci
=-=-=-=-=-=-=-=-=-

Digite o valor inteiro (0 < N < 46):

Processes:
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Output(s):
"A série de Fibonacci até 5 é: 0 1 1 2 3"
"""


def main():
    print("Série de Fibonacci")
    print('=-=-=-=-=-=-=-=-=-\n')
    n = int(input("Digite o valor inteiro (0 < N < 46): "))

    if n < 0 or n > 46:
        print("error")
    else:
        fibonacci = [0, 1]

        for i in range(2, n):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

        sequencia = ' '.join(str(num) for num in fibonacci)
        print(f"A série de Fibonacci até {n} é: {sequencia}")


if __name__ == '__main__':
    main()
