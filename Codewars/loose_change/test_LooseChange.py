from LooseChange import loose_change


def changes():
    assert loose_change(29) == {'Nickels': 0,
                                'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1,
                                'Pennies': 1, 'Dimes': 1, 'Quarters': 3}


def changes_menor_cero():
    assert loose_change(0) == {'Nickels': 0,
                               'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0,
                                'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


def changes_decimals():
    assert loose_change(3.9) == {'Nickels': 0,
                                 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
