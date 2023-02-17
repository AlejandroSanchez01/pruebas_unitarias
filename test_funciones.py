"""
Your module description
"""
from funciones import sumar,primo

def test_sumar():
    assert sumar(2,4) == 6
    assert sumar(-2,2) == 0
    assert sumar(2,2) == 4


def test_primo():
    assert primo(2) is True
    assert primo(5) is True
    assert primo(11) is True
