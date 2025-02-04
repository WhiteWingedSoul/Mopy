import random
from seed.seed import Seed

class RandIntSeed(Seed):

    def __init__(self, min, max):
        self.min = min
        self.max = max
        super().__init__()

    def generate(self):
        return random.randint(self.min, self.max)


if __name__ == "__main__":
    pass