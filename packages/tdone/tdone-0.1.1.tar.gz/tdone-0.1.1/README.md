Installation

pip install tdone

Top level coding, reading from the standard input, responding in the stdout with `print()`
```python
from sys import stdin
from tdone.pricer import SimpleResponse

new_quote = SimpleResponse()

# Get quotation request details as json
request = stdin.read()
details = json.loads(request)

if details.legs is None or len(details.legs) == 0:
    new_quote.error("No legs found")
    print(new_quote)
    exit(1)

only_leg = details.legs[0]
if only_leg.notional is None:
    new_quote.error("No notional found")
    print(new_quote)
    exit(1)

notional = only_leg.notional

# Get market data
market_data = (1.0, 0.5, 0.25, 0.1, 0.05, 0.01)

# Calculate
if new_quote.value < 0:
    new_quote.error("Negative value")
else:
    new_quote.value = notional * avg(market_data)

print(new_quote)
```


One function for one model, reading the market data from real-time updates from RabbitMQ and returning values as a function
```python
from tdone.pricer import InstrumentPricer, MissingDataException, CalculationError

class InterestLinkedProductPricer(InstrumentPricer):
    async def async_price(self, quotation_request, quote):
        only_leg = quotation_request.legs[0]

        # Get market data
        curve = self.marketdata.zero_rate_curve(only_leg.currency, quotation_request.value_date)
        if len(curve) == 0:
            quote.warning(f"{only_leg.currency} curve is missing. Defaulting to USD zero curve")
            curve = self.marketdata.zero_rate_curve("USD", quotation_request.value_date)
            # To stop the calculation, use `throw MissingDataException()``
        
        subsequent_zero_rate = None
        for zero_rate in curve:
            if zero_rate.maturity > only_leg.maturity:
                subsequent_zero_rate = zero_rate.rate
                break

        if subsequent_zero_rate is None:
            quote.error(f"No subsequent zero rate found for {only_leg.maturity}")
            throw MissingDataException()

        if subsequent_zero_rate == 0.0 or subsequent_zero_rate is 1.0:
            quote.error(f"Subsequent zero rate is {subsequent_zero_rate}")
            throw CalculationError()

        quote.value = 100.0 * only_leg.notional (1 + subsequent_zero_rate)
        return quote
```


