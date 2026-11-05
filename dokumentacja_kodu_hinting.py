"""Docstringi i podpowiedzi typów; plik wejściowy do generowania dokumentacji."""

import typing

# skąd uczyć się type hintów
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


def do_potegi(podstawa: float, wykladnik: float) -> float | complex:
    """
    This is a docstring with minimum syntax

    More info lore ipplsum lore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsum
    lore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsum
    lore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsum
    lore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsumlore ipplsum
    lore ipplsumlore ipplsumlore ipplsum
    """
    print(podstawa, wykladnik)
    return podstawa**wykladnik


# nie ma sposobu na ohintowanie listy jako rekordu
def zwracam_rekord_liste(n: int) -> list[str | int]:
    """
    first line

    more info more info more info more info more info more info more info more info more info
    more info more info more info more info more info more info more info more info more info
    more info more info more info more info more info more info more info more info more info
    more info more info more info more info more info

    Args:
        n: ile razy powtorzyc liste

    Returns: a list
    """

    return ["Ola", 44, "Warszawa"] * n


# it os possible to hint variables
# if we have an old package without hints

# def funkcja_bez_hintow():
#     i = 2
#     return ['', 22, 33.6][i]
#
# x: float = funkcja_bez_hintow()

# tools for automatic code generatoion
# - sphinx - DO NOT USE !!!
# - pdoc pdoc3 - first step
# - many others - some towards readthedocs

if __name__ == "__main__":
    do_potegi(3, 2)
    print(typing.get_type_hints(do_potegi))
