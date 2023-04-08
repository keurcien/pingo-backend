class Converter:
    def __init__(self):
        self.table = {
            "volume": {"ml": 0.1, "cl": 1.0, "dl": 10.0, "l": 100.0},
            "weight": {"g": 1.0, "kg": 1000.0},
        }

    def _to_centiliters(self, value, unit):
        return value * self.table["volume"].get(unit)

    def _to_grams(self, value, unit):
        return value * self.table["weight"].get(unit)

    def convert(self, value, unit):
        if unit in self.table["volume"].keys():
            return self._to_centiliters(value, unit), "cl"
        elif unit in self.table["weight"].keys():
            return self._to_grams(value, unit), "g"
        else:
            return value, unit
