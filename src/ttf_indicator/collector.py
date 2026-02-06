import frcm 
from datetime import datetime
from ttf_indicator.indicator import Indicator
from ttf_indicator.sensor import Sensor


class Collector:

    def collect(self, temp: Sensor, humid: Sensor, wind_speed: Sensor, ind: Indicator):
        temperature = temp.read()
        humidity = humid.read()
        ws = wind_speed.read()

        ts = datetime.now()

        wd = frcm.WeatherData([
            frcm.WeatherDataPoint(temperature=temperature, humidity=humidity, wind_speed=ws, timestamp=ts)
        ])

        fire_risk = frcm.compute(wd)
        first_risk = fire_risk.firerisks[0]

        ttf = first_risk.ttf

        return ind.indicate(ttf)
