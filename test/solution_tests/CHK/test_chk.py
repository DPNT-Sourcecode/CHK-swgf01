from solutions.CHK import checkout_solution


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
| Z    | 50    |                        |
+------+-------+------------------------+


Notes: 
 - The policy of the supermarket is to always favor the customer when applying special offers.
 - All the offers are well balanced so that they can be safely combined.
 - For any illegal input return -1
"""


class TestCHK:

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
