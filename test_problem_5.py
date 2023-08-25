# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 4
# Description:

import os.path
import sys

from problem_5 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_4():
    if not os.path.exists("problem_5.py"):
        sys.exit("Error: problem_5.py not found")

    expected_output = [
        "Digite um valor para X (ou 0 para sair): ",
        "A sequência até 5 é 1 2 3 4 5",
        "Digite um valor para X (ou 0 para sair): ",
        "A sequência até 3 é 1 2 3",
        "Digite um valor para X (ou 0 para sair): ",
        "A sequência até 10 é 1 2 3 4 5 6 7 8 9 10",
        "Digite um valor para X (ou 0 para sair): "

    ]

    set_keyboard_input([5, 3, 10, 0])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
