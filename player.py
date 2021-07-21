class Player():
    def __init__(self, name):
        self.name = name
        self.playTime = 0
        self.discovered_values = []

    def already_discover(self, value):
        return value in self.discovered_values

    def remember_value(self, value): self.discovered_values.append(value)

    def has_all_values(self, total_number): return len(self.discovered_values) == total_number