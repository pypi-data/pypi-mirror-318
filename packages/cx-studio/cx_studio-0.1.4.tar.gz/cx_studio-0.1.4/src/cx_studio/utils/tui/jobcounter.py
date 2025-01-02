class JobCounter:
    def __init__(self, current=1, max=100, zero="0"):
        self.max = max
        self.current = current
        self.zero = zero

    @property
    def number_digits(self):
        return len(str(self.max))

    def __str__(self):
        x = self.number_digits
        return f"{self.current:{self.zero}{x}}/{self.max}"

    def __int__(self):
        return self.current

    def __len__(self):
        return self.number_digits - 1

    @property
    def percentage(self):
        return self.current / self.max * 100

    def advance(self, n=1):
        self.current += n
        if self.current > self.max:
            self.current = self.max
        if self.current < 1:
            self.current = 1
        return self
