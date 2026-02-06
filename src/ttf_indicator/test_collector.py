import unittest
from unittest.mock import Mock
from ttf_indicator.indicator import Indicator
from ttf_indicator.collector import Collector

class CollectorTest(unittest.TestCase):

    def test_happy_flow(self):
        collector = Collector()
        indicator = Indicator()

        temp_sens = Mock()
        temp_sens.read = Mock(return_value=-8.2)
        hum_sens = Mock()
        temp_sens.read = Mock(return_value=45.0)
        ws_sens = Mock()
        ws_sens.read = Mock(return_value=1.3)

        result = collector.collect(temp_sens, hum_sens, ws_sens, indicator)

        self.assertEqual("medium", result)

if __name__ == "__main__":
    unittest.main()

