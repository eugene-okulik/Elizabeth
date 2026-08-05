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


def format_book(book):
    str_line = f'Название: {book.title}, Автор: {book.author}, страниц: {book.page_count}'
    if isinstance(book, SchoolBook):
        str_line = str_line + f', предмет: {book.subject}, класс: {book.grade}'
    elif isinstance(book, Book):
        str_line = str_line + f', материал: {book.page_material}'
    if book.reservation:
        str_line = str_line + f', зарезервирована'
    return str_line


print(format_book(book_1))
print(format_book(book_2))
print(format_book(book_3))
print(format_book(book_4))
print(format_book(book_5))
print(format_book(sch_book_1))
print(format_book(sch_book_2))
print(format_book(sch_book_3))
