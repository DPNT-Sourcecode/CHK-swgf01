from solutions.CHK import checkout_solution


"""
Price table
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


class TestCHK:

    def test_invalid_input(self):
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout('E') == -1
        assert checkout_solution.checkout('a') == -1

    def test_individual_item(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15

    def test_special_offer_individual(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 130 + 50
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBBB') == 90
        assert checkout_solution.checkout("AAAAA") == 130 + 50*2


    def test_combined

