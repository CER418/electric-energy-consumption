from samplebase import SampleBase
from nordpool import elspot
import schedule
import time
import datetime
from .location import location

# Attempts to find the current location depending on IP, if not default to Kristiandsand.
try:
    location = location()
except Exception or ValueError:
    location = "Kr.sand"

# Instance of Prices class for fetching Nord Pool elspot prices.
spot_price = elspot.Prices()
data = spot_price.hourly(end_date=datetime.date.today(), areas=[location])

# Lowest and highest prices in the selected area throughout the current day.
min_price = data['areas'][location]['Min']
max_price = data['areas'][location]['Max']


# Iterates through each hour in the fetched data, if it is equal to the current hour return the price.
def current_value():
    for _ in data['areas'][location]['values']:
        if _['start'].hour == datetime.datetime.now(_['start'].tzinfo).hour:
            return _['value']


current_price = current_value()


# Sets up the five categories of price by dividing the result of minimum and maximum by 5.
# Then lists these values.
def list_of_values(min_value, max_value):
    step = (min_value - max_value) / 5
    return list(range(round(min_value), round(max_value), abs(round(step))))


num = list_of_values(min_value=min_price, max_value=max_price)


class Matrix(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Matrix, self).__init__(*args, **kwargs)

# Fills the LED board with colors depending on if the current price is between two dividers, defined earlier.
    def run(self):
        while True:
            if num is None:
                self.matrix.Clear()
            elif num[0] <= current_price <= num[1]:
                self.matrix.Fill(11, 110, 153)
            elif num[1] <= current_price <= num[2]:
                self.matrix.Fill(15, 123, 108)
            elif num[2] <= current_price <= num[3]:
                self.matrix.Fill(223, 171, 1)
            elif num[3] <= current_price <= num[4]:
                self.matrix.Fill(217, 115, 13)
            elif num[4] <= current_price <= num[5]:
                self.matrix.Fill(255, 0, 0)
                self.usleep(20 * 1000)


def scheduled_task():
    """Function to be scheduled"""
    matrix = Matrix()
    if not matrix.process():
        matrix.print_help()


if __name__ == "__main__":
    # Nord Pool publish data every day at 13:00 UTC
    print(current_price)
    print(num)
    scheduled_task()
    schedule.every().hour.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(1)
