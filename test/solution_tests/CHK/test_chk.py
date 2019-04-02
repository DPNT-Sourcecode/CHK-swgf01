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
