from logging import makeLogRecord




def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    lst1_len = len(lst1)
    lst2_len = len(lst2)

    def func(len1, len2):

        if len1 < lst1_len and len2 == lst2_len:
            return [lst1[len1]] + func(len1 + 1, len2)
        elif len1 == lst1_len and len2 < lst2_len:
            return [lst2[len2]] + func(len1, len2 + 1)
        elif len1 >= lst1_len and len2 >= lst2_len:
            return []
        elif lst1[len1] <= lst2[len2]:
            return [lst1[len1]] + func(len1 + 1, len2)
        return [lst2[len2]] + func(len1, len2 + 1)

    return func(0, 0)

    if not lst1 or not lst2:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        return coin(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):

        return self.cents + max(Mint.present_year - self.year - 50, 0)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    number = 0
    change = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def vend(self):
        if self.number <= 0:
            return 'Nothing left to vend. Please restock.'
        else:
            if self.change < self.price:
                return 'You must add $' + str(
                    abs(self.change - self.price)) + ' more funds.'

            elif self.change > self.price:
                qian = abs(self.change - self.price)
                self.change = 0
                self.number -= 1
                return ("Here is your " + self.name + " and $" + str(qian) +
                        " change.")
            else:
                self.change = 0
                self.number -= 1
                return ("Here is your " + self.name + '.')

    def add_funds(self, fund):
        if self.number > 0:
            self.change += fund
            return ('Current balance: $' + str(self.change))
        else:
            return ("Nothing left to vend. Please restock. Here is your $" +
                    str(fund) + ".")

    def restock(self, number):
        self.number += number
        return ("Current " + self.name + " stock: " + str(self.number))
