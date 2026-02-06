import unittest
from unittest.mock import MagicMock
from ttf_indicator.indicator import Indicator
from ttf_indicator.collector import Collector

class CollectorTest(unittest.TestCase):

    def test_happy_flow(self):
        collector = Collector()
        indicator = Indicator()


        temp_sens = MagicMock()
        temp_sens.read = MagicMock(return_value=-8.2)
        hum_sens = MagicMock()
        hum_sens.read = MagicMock(return_value=45.0)
        ws_sens = MagicMock()
        ws_sens.read = MagicMock(return_value=1.3)

        result = collector.collect(temp_sens, hum_sens, ws_sens, indicator)

        self.assertEqual("yellow", result)

if __name__ == "__main__":
    unittest.main()

