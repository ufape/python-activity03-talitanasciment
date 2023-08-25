# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Description:

import os.path
import sys

from problem_1 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_1():
    if not os.path.exists("problem_1.py"):
        sys.exit("Error: problem_1.py not found")

    expected_output = [
        "Digite um valor inteiro para X: ",
        "Digite um valor inteiro para Y: ",
        "A soma dos números ímpares entre 12 e 15 é: 13"
    ]

    set_keyboard_input([15, 12])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"

    expected_output = [
        "Digite um valor inteiro para X: ",
        "Digite um valor inteiro para Y: ",
        "A soma dos números ímpares entre -5 e 6 é: 5"
    ]

    set_keyboard_input([6, -5])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
