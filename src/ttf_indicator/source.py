
from datetime import datetime
from pathlib import Path
from frcm import WeatherData, WeatherDataPoint

def _read_data(data: Path) -> WeatherData:
        with open(data, "r") as f:
            header = f.readline()
            header = header.strip().split(",")
            data_points = []
            for line in f:
                line = line.strip().split(",")
                if len(line) != len(header):
                    continue
                timestamp_str = line[0]
                if (timestamp_str[0] == '"' and timestamp_str[-1] == '"') or (timestamp_str[0] == "'" and timestamp_str[-1] == "'"):
                    timestamp_str = timestamp_str[1:-1]
                try:
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
                except ValueError:
                    continue
                temperature = float(line[1])
                humidity = float(line[2])
                wind_speed = float(line[3])
                data_points.append(WeatherDataPoint(timestamp=timestamp, temperature=temperature, humidity=humidity, wind_speed=wind_speed))
            return WeatherData(data=data_points)

class Source:

    def __init__(self, location: str, data: Path):
        self.location = location
        self.data = _read_data(data)


    def get_latest_update(self) -> datetime:
        return max([dp.timestamp for dp in self.data.data])
    
    def get_data(self) ->  WeatherData:
        return self.data