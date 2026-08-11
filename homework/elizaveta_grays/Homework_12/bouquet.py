class Bouquet():
    def __init__(self, flowers=None):
        if flowers is None:
            self.flowers = []
        else:
            self.flowers = flowers

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        if len(self.flowers) > 0:
            return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)
        else:
            return 0

    def sort_by(self, key, reverse=False):
        return sorted(self.flowers, key=lambda f: getattr(f, key), reverse=reverse)

    def filter_by(self, **kwargs):
        return [flower for flower in self.flowers
                if all(getattr(flower, attr) == value for attr, value in kwargs.items())]

    def __str__(self):
        return (f'Букет из {len(self.flowers)} цветов, стоимость: {self.total_cost()}р, '
                f'среднее время жизни: {self.average_lifespan():.1f} дн.')
