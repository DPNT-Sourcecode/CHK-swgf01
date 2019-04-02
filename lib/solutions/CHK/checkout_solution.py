
"""
Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes:
 - For any illegal input return -1
"""

# noinspection PyUnusedLocal
# skus = unicode string

from collections import namedtuple

SKU = namedtuple('SKU', 'unit_price offer_multiplier offer_price')

price_table = {
    'A': {
        SKU(50, 3, 130),
        'unit_price': 50,
        'offer_multiplier': 3,
        'offer_price': 130
    },
    'B': {
        'unit_price': 30,
        'offer_multiplier': 2,
        'offer_price': 145
    },
    'C': {
        'price': 20,
        'offer_multiplier': 1,
        'offer_price': 145
    },
}


def checkout(skus):
    raise NotImplementedError()
