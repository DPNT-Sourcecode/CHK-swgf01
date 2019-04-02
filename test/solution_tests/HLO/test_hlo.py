from solutions.HLO import hello_solution

class TestHLO:
    def test_hello(self):
        assert hello_solution.hello('Volodymyr') == "Hello, Volodymyr!"