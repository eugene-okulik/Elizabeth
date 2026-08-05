class Book:
    page_material = 'бумага'
    text_availability = True

    def __init__(self, title, author, page_count, publisher, reservation):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.publisher = publisher
        self.reservation = reservation

    def info(self):
        line = (f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, '
                f'материал: {self.page_material}')
        if self.reservation:
            line += ', зарезервирована'
        return line


class SchoolBook(Book):

    def __init__(self, title, author, page_count, publisher, reservation, subject, grade, has_tasks):
        super().__init__(title, author, page_count, publisher, reservation)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def info(self):
        line = f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}'
        line += f', предмет: {self.subject}, класс: {self.grade}'
        if self.reservation:
            line += ', зарезервирована'
        return line


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

print(book_1.info())
print(book_2.info())
print(book_3.info())
print(book_4.info())
print(book_5.info())
print(sch_book_1.info())
print(sch_book_2.info())
print(sch_book_3.info())
