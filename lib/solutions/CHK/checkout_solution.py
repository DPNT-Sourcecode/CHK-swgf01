import re

from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string

price_string = """| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |"""


def make_pricetable(price_string):
    price_table = {}
    for line in price_string.splitlines():
        columns = line.split('|')
        sku = columns[1].strip()
        price = int(columns[2].strip())
        price_table[sku] = price
    return price_table

price_table = make_pricetable(price_string=price_string)

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
        q, r = divmod(cnt_sku[self.sku], self.multiplier)
        price_so_far = q * self.offer_price
        cnt_sku[self.sku] = r
        return cnt_sku, price_so_far

    def __eq__(self, other):
        return self.sku == other.sku and\
               self.multiplier == other.multiplier and\
               self.offer_price == other.offer_price


class BuyXgetY(Offer):
    def __init__(self, sku_x, multiplier, sku_y, y_cnt):
        self.sku = sku_x
        self.multiplier = multiplier
        self.sku_y = sku_y
        self.y_cnt = y_cnt
        self.discount = price_table[sku_y] * y_cnt

    def apply(self, cnt_sku):
        q, r = divmod(cnt_sku[self.sku], self.multiplier)
        applied_times = min(q, cnt_sku[self.sku_y])
        price_so_far = applied_times * self.multiplier * price_table[self.sku]
        cnt_sku[self.sku] -= applied_times * self.multiplier
        cnt_sku[self.sku_y] -= applied_times * self.y_cnt
        return cnt_sku, price_so_far

    def __eq__(self, other):
        return self.sku == other.sku and\
               self.multiplier == other.multiplier and\
               self.sku_y == other.sku_y and\
               self.y_cnt == other.y_cnt


class BuyXgetX(Multiplicative):
    def __init__(self, sku, multiplier, cnt):
        new_multiplier = multiplier + cnt
        offer_price = multiplier * price_table[sku]
        super(BuyXgetX, self).__init__(sku, new_multiplier, offer_price)


def make_special_offers(price_string):
    patternm = re.compile(r"(\d+)(.) for (\d+)")
    patternb = re.compile(r"(\d+)(.) get one (.) free")

    groupsm = patternm.findall(price_string)
    offers = [Multiplicative(group[1], int(group[0]), int(group[2]))
              for group in groupsm]
    groupsb = patternb.findall(price_string)
    for group in groupsb:
        if group[1] == group[2]:
            offers.append(BuyXgetX(group[1], int(group[0]), 1))
        else:
            offers.append(BuyXgetY(group[1], int(group[0]),group[2],1))
    return offers


offers = make_special_offers(price_string)

for k, v in price_table.items():
    offers.append(Multiplicative(k, 1, v))


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
        # Given number of individual items apply offers and calculate
        # items price
        for offer in sorted(offers, key=lambda o: o.discount, reverse=True):
            sku_cnt, price = offer.apply(sku_cnt)
            total_price += price
        return total_price
    except:
        # The skus must be iterable for valid input
        return -1
