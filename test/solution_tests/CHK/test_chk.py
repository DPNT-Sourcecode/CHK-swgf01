from solutions.CHK import checkout_solution

"""
| A    | 50    | 3A for 130, 5A for 200          |
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
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
"""

price_string = """| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    | 2D get one D free      |
| E    | 40    | 2E get one B free      |
| F    | 17    | buy any 2 of (B,C,D) for 25 |"""


class TestCHK:

    def test_make_price_table(self):
        price_table = checkout_solution.make_pricetable(price_string)
        assert price_table == {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40
        }

    def test_offer_eq(self):
        mult1 = checkout_solution.Offer.make_multiplicative('A', 3, 130)
        mult2 = checkout_solution.Offer.make_multiplicative('A', 3, 130)
        assert mult1 == mult2

    def test_offer_discount(self):
        mult = checkout_solution.Offer.make_multiplicative('A', 3, 130)
        assert mult.discount == 20

    def test_offer_buy_x_get_y(self):
        xgety = checkout_solution.Offer.make_buy_x_get_y('E', 2, 'B', 1)
        assert xgety.discount == 30

    def test_offer_buy_x_get_x(self):
        xgety = checkout_solution.Offer.make_buy_x_get_y('F', 2, 'F', 1)
        assert xgety.discount == 10

    def test_offer_apply(self):
        mult = checkout_solution.Offer.make_multiplicative('A', 3, 130)
        basket = {
            'A': 3
        }
        new_basket, price = mult.apply(basket)
        assert new_basket['A'] == 0
        assert price == 130

    def test_combination_offer_maker(self):
        offers = checkout_solution.make_combination_offer(
            ['S', 'T', 'X', 'Y', 'Z'], 3, 45)
        assert checkout_solution.Offer({'S': 1, 'X': 1, 'Y': 1}, 45) in offers

    def test_make_simple_offer(self):
        offers = checkout_solution.make_simple_offers({'A': 10, 'B': 20})
        assert checkout_solution.Offer({'A': 1}, 10) in offers

    def test_make_special_offer(self):
        offers = checkout_solution.make_special_offers(price_string)
        assert checkout_solution.Offer({'B': 1, 'C': 1}, 25) in offers
        assert checkout_solution.Offer({'B': 2}, 45) in offers
        assert checkout_solution.Offer({'E': 2, 'B': 1}, 80) in offers
        assert checkout_solution.Offer({'D': 3}, 30) in offers

    def test_invalid_input(self):
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout('a') == -1

    def test_individual_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('E') == 40
        assert checkout_solution.checkout('F') == 10

    def test_special_offer_individual(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 130 + 50
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 200 + 50
        assert checkout_solution.checkout("AAAAAAA") == 200 + 50 * 2
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBB') == 45 + 30
        assert checkout_solution.checkout('BBBB') == 90
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20

    def test_combined_sku(self):
        assert checkout_solution.checkout("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout_solution.checkout("ABACDA") == 130 + 30 + 20 + 15
        assert checkout_solution.checkout("AABBCC") == 50*2 + 45 + 20*2

    def test_e_offer(self):
        assert checkout_solution.checkout("ABCDEE") == 50 + 30 + 20 + 15 + 40 * 2 - 30

    def test_any_3(self):
        assert checkout_solution.checkout("STX") == 45



