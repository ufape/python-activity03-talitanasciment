# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 2
# Description:

import os.path
import sys

from problem_2 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_2():
    if not os.path.exists("problem_2.py"):
        sys.exit("Error: problem_2.py not found")

    expected_output = [
        "Digite um número inteiro entre 2 e 1000: ",
        "5 x 1 = 5",
        "5 x 2 = 10",
        "5 x 3 = 15",
        "5 x 4 = 20",
        "5 x 5 = 25",
        "5 x 6 = 30",
        "5 x 7 = 35",
        "5 x 8 = 40",
        "5 x 9 = 45",
        "5 x 10 = 50"
    ]

    set_keyboard_input([5])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
