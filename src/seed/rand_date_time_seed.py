import datetime
import random
from seed.seed import Seed

class RandDateTimeSeed(Seed):

    def __init__(self, format=None):
        self.format = format
        super().__init__()

    def generate(self):
        year = random.randint(1900, 2100)
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        if self.format is None:
            return datetime.datetime(year, month, day, hour, minute, second)
        else:
            return datetime.datetime(year, month, day, hour, minute, second).strftime(self.format)


if __name__ == "__main__":
    pass