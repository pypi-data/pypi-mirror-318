import json

class MarketData:
    def zero_rate_curve(self, currency, asof_date):
        return []

class SimpleResponse:
    def __init__(self):
        self.value = None
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(message)

    def warning(self, message):
        self.warnings.append(message)
    
    def __str__(self):
        # Using json.dumps to format the output
        return json.dumps(self.__dict__, indent=4)

class InstrumentPricer:
    def __init__(self, model):
        self.model = model

    async def async_price(self, quotation_request, quote):
        quote.error("Not implemented")
        return quote

class MissingDataException(Exception):
    pass

class CalculationError(Exception):
    pass
