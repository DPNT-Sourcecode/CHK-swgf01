
"""
Our price table and offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+


Notes:
 - The policy of the supermarket is to always favor the customer when applying special offers.
 - All the offers are well balanced so that they can be safely combined.
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
        total_price = 0
        # Given number of individual items apply special offer and calculate
        # items price
        for sku, n in sku_cnt.items():
            q, r = divmod(n, price_table[sku].offer_multiplier)
            sku_total = q * price_table[sku].offer_price + \
                        r * price_table[sku].unit_price
            total_price += sku_total
        return total_price
    except:
        # The skus must be iterable for valid input
        return -1


