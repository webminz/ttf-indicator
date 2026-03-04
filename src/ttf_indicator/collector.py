import frcm 
from ttf_indicator.indicator import Indicator
from ttf_indicator.source import Source


class Collector:

    def collect(self, src: Source, ind: Indicator):
        wd = src.get_data()
        fire_risk = frcm.compute(wd)
        latest_fire_risk = fire_risk.firerisks[0]
        ttf = latest_fire_risk.ttf
        return ind.indicate(ttf)
