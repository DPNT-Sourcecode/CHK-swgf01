import re
import itertools
from collections import defaultdict, Counter
# noinspection PyUnusedLocal
# skus = unicode string

price_string = """| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |"""


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
    def __init__(self, skus, offer_price):
        self.skus = skus
        self.price = offer_price
        # Calculate discount
        total_price = 0
        for s, cnt in skus.items():
            total_price += price_table[s] * cnt
        self.discount = total_price - offer_price

    def apply(self, sku_basket):
        # Calculate how many times offer can be applied
        n_times = min([sku_basket[sku] // cnt for sku, cnt in self.skus.items()])
        for sku, cnt in self.skus.items():
            sku_basket[sku] -= cnt * n_times
        return sku_basket, self.price * n_times

    def __eq__(self, other):
        return self.skus == other.skus and\
               self.price == other.price and\
               self.discount == other.discount

    @classmethod
    def make_multiplicative(cls, sku, cnt, offer_price):
        return cls({sku: cnt}, offer_price)

    @classmethod
    def make_buy_x_get_y(cls, sku_x, x_cnt, sku_y, y_cnt):
        offer_price = price_table[sku_x] * x_cnt
        if sku_x == sku_y:
            return cls({sku_x: x_cnt + y_cnt}, offer_price)
        else:
            return cls({sku_x: x_cnt, sku_y: y_cnt}, offer_price)


def make_combination_offer(sku_list, n_comb, offer_price):
    """
    Returns list of offers
    """
    combinations = itertools.combinations_with_replacement(sku_list, n_comb)
    sku_counters = [Counter(combination) for combination in combinations]
    return [Offer(counter, offer_price) for counter in sku_counters ]


def make_special_offers(price_string):
    patternm = re.compile(r"(\d+)(.) for (\d+)")
    patternb = re.compile(r"(\d+)(.) get one (.) free")
    patternc = re.compile(r"buy any (\d+) of \((.(,.)*)\) for (\d+)")

    groupsm = patternm.findall(price_string)
    offers = [Offer.make_multiplicative(group[1], int(group[0]), int(group[2]))
              for group in groupsm]
    groupsb = patternb.findall(price_string)
    for group in groupsb:
        offers.append(Offer.make_buy_x_get_y(group[1], int(group[0]), group[2], 1))
    groupsc = patternc.findall(price_string)
    for group in set(groupsc):
        offers.extend(make_combination_offer(
            group[1].split(','),
            int(group[0]),
            int(group[3])))
    return offers


offers = make_special_offers(price_string)

for k, v in price_table.items():
    offers.append(Offer.make_multiplicative(k, 1, v))


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








