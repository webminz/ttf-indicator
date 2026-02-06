import unittest
from ttf_indicator.indicator import Indicator

class IndicatorTest(unittest.TestCase):

    def test_indicate_red(self):
        # 1. set up unit under test
        uut = Indicator()
        # 2. call unit under test
        result = uut.indicate(3.5)
        # 3. assertions
        self.assertEqual("red", result)



    def test_indicate_green(self):
        # 1. set up unit under test
        uut = Indicator()
        # 2. call unit under test
        result = uut.indicate(16.0)
        # 3. assertions
        self.assertEqual("green", result)

    

    def test_indicate_yellow(self):
        # 1. set up unit under test
        uut = Indicator()
        # 2. call unit under test
        result = uut.indicate(10.0)
        # 3. assertions
        self.assertEqual("yellow", result)

        # corner cases
        result = uut.indicate(5)
        self.assertEqual("yellow", result)
        result = uut.indicate(15)
        self.assertEqual("yellow", result)

    
    def test_invalid(self):
        # 1. set up unit under test
        uut = Indicator()
        # 2. call unit under test
        try:
            result = uut.indicate("halloooooo")
            self.fail()
        except:
            pass

    def test_negative(self):
        uut = Indicator()
        try:
            result = uut.indicate(-5)
            self.fail()
        except:
            pass







if __name__ == "__main__":
    unittest.main()
