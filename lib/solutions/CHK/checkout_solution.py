
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

from collections import namedtuple, defaultdict

SKU = namedtuple('SKU', 'unit_price offer_multiplier offer_price')

price_table = {
    'A': SKU(50, 3, 130),
    'B': SKU(30, 2, 45),
    'C': SKU(20, 1, 20),
    'D': SKU(15, 1, 15)
}


def checkout(skus):
    try:
        # check input SKUs are present in the price_table
        # and count occurrences of individual sku
        sku_cnt = defaultdict(int)
        for sku in skus:
            if sku not in price_table:
                return -1
            else:
                sku_cnt[sku] += 1
    except:
        # The skus must be iterable for valid input
        return -1

