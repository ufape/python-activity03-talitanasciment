# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 2
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém um valor inteiro N (2 < N < 1000).

Processes:
Leia 1 valor inteiro N (2 < N < 1000).

A seguir, mostre a tabuada de N:
1 x N = N 
2 x N = 2N
...
10 x N = 10N

Output(s):
Imprima a tabuada de N, conforme o exemplo fornecido.

"""


def main():
    n = int(input("Digite um número inteiro entre 2 e 1000: "))

    for i in range(1, 11):
      print(f"{n} x {i} = {i*n}")



if __name__ == '__main__':
    main()
