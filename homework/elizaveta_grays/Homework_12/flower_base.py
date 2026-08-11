class Flower():
    freshness = True

    def __init__(self, name, color, cost, stem_length, lifespan):
        self.name = name
        self.color = color
        self.cost = cost
        self.stem_length = stem_length
        self.lifespan = lifespan

    def __str__(self):
        return f'{self.name} ({self.color}), {self.stem_length} см, {self.cost} руб., живет {self.lifespan} дней'

    def __repr__(self):
        return f'{self.name} ({self.color}), {self.stem_length} см, {self.cost} руб., живет {self.lifespan} дней'
