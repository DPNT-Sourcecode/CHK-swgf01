
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

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


class Offer:
    def __init__(self):
        self.discount = 0


class Multiplicative(Offer):
    def __init__(self, sku, multiplier, offer_price):
        self.sku = sku
        self.multiplier = multiplier
        self.offer_price = offer_price
        self.discount = price_table[sku] * multiplier - offer_price

    def apply(self, cnt_sku):
        pass


class BuyXgetY(Offer):
    def __init__(self, sku_x, multiplier, sku_y, y_cnt):
        self.sku = sku_x
        self.multiplier = multiplier
        self.sku_y = sku_y
        self.y_cnt = y_cnt
        self.discount = price_table[sku_y] * y_cnt

    def apply(self, cnt_sku):
        pass


offers = sorted([Multiplicative('A', 1, 50),
                 Multiplicative('A', 3, 130),
                 Multiplicative('A', 5, 200),
                 Multiplicative('B', 1, 30),
                 Multiplicative('B', 2, 45),
                 Multiplicative('C', 1, 20),
                 Multiplicative('D', 1, 15),
                 Multiplicative('A', 1, 40),
                 BuyXgetY('E', 2, 'B', 1)], key=lambda o: o.discount)

print(offers)

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
