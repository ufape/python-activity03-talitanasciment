# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 3
# Description:

import os.path
import sys

from problem_3 import main
from tud_tests import set_keyboard_input, get_display_output


def test_problem_3():
    if not os.path.exists("problem_3.py"):
        sys.exit("Error: problem_3.py not found")

    expected_output = [
        "Quantas amostras: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Tipo: ",
        "Quantidade: ",
        "Total: 92 amostras.",
        "Total de cenouras: 29.",
        "Total de rabanetes: 40.",
        "Total de salmões: 23.",
        "Percentual de cenouras: 31.52%",
        "Percentual de rabanetes: 43.48%",
        "Percentual de salmões: 25.00%"
    ]

    set_keyboard_input([10, "C", 10, "R", 6, "S", 15, "C",
                       5, "R", 14, "C", 9, "R", 6, "S", 8, "C", 5, "R", 14])
    main()
    output = get_display_output()

    assert output == expected_output, \
        f"Expected {expected_output}, but got {output}"
