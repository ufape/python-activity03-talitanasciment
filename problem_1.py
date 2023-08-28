# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 1
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém dois valores inteiros.
Exemplo:
Digite um valor inteiro para X: 15
Digite um valor inteiro para Y: 12

Processes:
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Output(s):
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que deverá caber
em um inteiro.
Exemplo:
A soma dos números ímpares entre 15 e 12 é: 13

"""


def main():
  x = int(input("Digite um valor inteiro para X: "))
  y = int(input("Digite um valor inteiro para Y: "))

  if x > y:
    x,y = y,x

  soma = 0

  for i in range(x+1, y):
    if i % 2 == 1:
      soma += i

  print(f"A soma dos números ímpares entre {x} e {y} é: {soma}")

  


if __name__ == '__main__':
    main()
