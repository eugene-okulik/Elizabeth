import flower_base


class Roses(flower_base.Flower):
    freshness = True

    def __init__(self, color, stem_length, cost, lifespan, name='Roses'):
        super().__init__(name, color, cost, stem_length, lifespan)


class Lilies(flower_base.Flower):
    freshness = True

    def __init__(self, color, stem_length, cost, lifespan, name='Lily'):
        super().__init__(name, color, cost, stem_length, lifespan)


class Peonies(flower_base.Flower):
    freshness = True

    def __init__(self, color, cost, stem_length, lifespan, name='Peonies'):
        super().__init__(name, color, cost, stem_length, lifespan)
