# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 4
# Description:

import os.path
import sys

from problem_4 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_4():
    if not os.path.exists("problem_4.py"):
        sys.exit("Error: problem_4.py not found")

    expected_output = [
        "Série de Fibonacci",
        "=-=-=-=-=-=-=-=-=-\n",
        "Digite o valor inteiro (0 < N < 46): ",
        "A série de Fibonacci até 5 é: 0 1 1 2 3"

    ]

    set_keyboard_input([5])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
