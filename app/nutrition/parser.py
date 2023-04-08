import re
from fractions import Fraction

UNITS = "|".join(["g", "kg", "ml", "cl", "dl", "cas", "cac", "sachet"])


class Parser:
    def __init__(self):
        self.unit_regexp = re.compile(f"(?P<qt>[0-9.,/ ]+)(?P<unit>{UNITS}+) ")
        self.no_unit_regexp = re.compile(f"(?P<qt>[0-9.,/ ]+) ")

    @staticmethod
    def _to_float(value):
        try:
            value_ = value.replace(",", ".")
            value_ = Fraction(value_)
            return float(value_)
        except:
            return 0.0

    def parse(self, ingredient):

        quantity = self.unit_regexp.search(ingredient)

        if quantity:

            value = quantity.group("qt")
            unit = quantity.group("unit")
            return self._to_float(value), unit

        else:

            quantity = self.no_unit_regexp.search(ingredient)

            if quantity:

                value = quantity.group("qt")
                return self._to_float(value), None

            else:

                return 0.0, None
