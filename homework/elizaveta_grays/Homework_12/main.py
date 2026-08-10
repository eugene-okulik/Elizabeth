import flower_types
import bouquet

roses1 = flower_types.Roses('Жемчужно-белый', 90, 500, 12, 'Роза Аваланж')
roses2 = flower_types.Roses('Персиково-желтый', 70, 1000, 13, 'Роза Олдувай')
roses3 = flower_types.Roses('Медно-кремовый', 100, 400, 20, 'Роза Каралуна')
print(roses1)
print(roses2)
print(roses3)
lilies1 = flower_types.Lilies('Нежно-лососевый', 120, 800, 10, 'Лилия Зельмира')
lilies2 = flower_types.Lilies('Желтая', 180, 600, 10, 'Лилия Монте Бьянко')
lilies3 = flower_types.Lilies('Белая', 140, 1000, 10, 'Лилия Уайт Айз')
print(lilies1)
print(lilies2)
print(lilies3)
peonies1 = flower_types.Peonies('Нежно-розовый', 900, 80, 10, 'Пион Сара Бернар')
peonies2 = flower_types.Peonies('Белый', 850, 90, 10, 'Пион Белая Грация')
peonies3 = flower_types.Peonies('Желтый', 750, 70, 10, 'Пион Бартзелла')
print(peonies1)
print(peonies2)
print(peonies3)
bouquet1 = bouquet.Bouquet([roses1, roses2, roses3])
bouquet2 = bouquet.Bouquet([lilies1, lilies2, lilies3])
bouquet3 = bouquet.Bouquet([peonies1, peonies2, peonies3])
print(bouquet1)
print(bouquet2)
print(bouquet3)

sorted_roses = bouquet1.sort_by('cost')  # или 'lifespan', 'stem_length'
for flower in sorted_roses:
    print(f'{flower.name} - {flower.cost}р.')

found = bouquet1.filter_by(lifespan=13)
for f in found:
    print(f.name)
