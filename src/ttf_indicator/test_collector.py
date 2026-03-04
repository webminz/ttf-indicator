import unittest
from unittest.mock import MagicMock
from ttf_indicator.indicator import Indicator
from ttf_indicator.collector import Collector
from frcm import WeatherDataPoint, WeatherData
from datetime import datetime, timedelta

class CollectorTest(unittest.TestCase):

    def test_happy_flow(self):
        collector = Collector()
        indicator = Indicator()
        src = MagicMock()
        get_data = MagicMock(return_value=WeatherData(data=[
            WeatherDataPoint(timestamp=datetime.now() - timedelta(minutes=1), temperature=-8.2, humidity=45.0, wind_speed=1.3),
            WeatherDataPoint(timestamp=datetime.now(), temperature=-8.2, humidity=45.0, wind_speed=1.3),
        ]))
        src.get_data = get_data

        result = collector.collect(src, indicator)

        self.assertEqual("yellow", result)

if __name__ == "__main__":
    unittest.main()

