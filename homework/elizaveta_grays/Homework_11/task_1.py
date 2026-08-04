class Book:
    page_material = 'бумага'
    text_availability = True

    def __init__(self, title, author, page_count, publisher, reservation):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.publisher = publisher
        self.reservation = reservation


class SchoolBook(Book):

    def __init__(self, title, author, page_count, publisher, reservation, subject, grade, has_tasks):
        super().__init__(title, author, page_count, publisher, reservation)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks


book_1 = Book('Идиот', 'Достоевский', 672, 'АСТ', True)
book_2 = Book('Анна Каренина', 'Толстой', 832, 'Азбука', False)
book_3 = Book('Обломов', 'Гончаров', 608, 'Эксмо', False)
book_4 = Book('Мертвые души', 'Гоголь', 420, 'Альпина', False)
book_5 = Book('Мастер и Маргарита', 'Булгаков', 412, 'Феникс', True)

sch_book_1 = SchoolBook('Учебник по Алгебре', 'Резанов', 320, 'Академкнига',
                        True, 'Алгебра', 8, False)
sch_book_2 = SchoolBook('Учебник по Геометрии', 'Семенов', 245, 'Просвещение',
                        False, 'Геометрия', 7, True)
sch_book_3 = SchoolBook('Учебник по Географии', 'Дроздов', 401, 'Академкнига',
                        False, 'География', 10, True)

sch_book_2.reservation = True

print(
    f'Название: {book_1.title}, Автор: {book_1.author}, страниц: {book_1.page_count}, '
    f'материал: {book_1.page_material}{", зарезервирована" if book_1.reservation else ""}'
)
print(
    f'Название: {book_2.title}, Автор: {book_2.author}, страниц: {book_2.page_count}, '
    f'материал: {book_2.page_material}{", зарезервирована" if book_2.reservation else ""}'
)
print(
    f'Название: {book_3.title}, Автор: {book_3.author}, страниц: {book_3.page_count}, '
    f'материал: {book_3.page_material}{", зарезервирована" if book_3.reservation else ""}'
)
print(
    f'Название: {book_4.title}, Автор: {book_4.author}, страниц: {book_4.page_count}, '
    f'материал: {book_4.page_material}{", зарезервирована" if book_4.reservation else ""}'
)
print(
    f'Название: {book_5.title}, Автор: {book_5.author}, страниц: {book_5.page_count}, '
    f'материал: {book_5.page_material}{", зарезервирована" if book_5.reservation else ""}'
)

print(
    f'Название: {sch_book_1.title}, Автор: {sch_book_1.author}, страниц: {sch_book_1.page_count}, '
    f'предмет: {sch_book_1.subject}, класс: {sch_book_1.grade}'
    f'{", зарезервирована" if sch_book_1.reservation else ""}'
)
print(
    f'Название: {sch_book_2.title}, Автор: {sch_book_2.author}, страниц: {sch_book_2.page_count}, '
    f'предмет: {sch_book_2.subject}, класс: {sch_book_2.grade}'
    f'{", зарезервирована" if sch_book_2.reservation else ""}'
)
print(
    f'Название: {sch_book_3.title}, Автор: {sch_book_3.author}, страниц: {sch_book_3.page_count}, '
    f'предмет: {sch_book_3.subject}, класс: {sch_book_3.grade}'
    f'{", зарезервирована" if sch_book_3.reservation else ""}'
)
