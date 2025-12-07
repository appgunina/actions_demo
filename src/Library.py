class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        return f"'{self.__title}' ({self.__author}, {self.__year}), доступна: {self.__available}"


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, страницы: {self.pages}, состояние: {self.condition}"


class EBook(Book):
    def __init__(self, title, author, year, file_size,
                 form):  # заменила format на form, тк в python есть такая встроенная функция
        super().__init__(title, author, year)
        self.file_size = file_size
        self.form = form

    def download(self):
        print(f"Книга {self.get_title()} загружается...")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, размер: {self.file_size} МБ, формат: {self.form}"


class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            print(f"Пользователь {self.name} взял книгу '{book.get_title()}'")
        else:
            print(f"!Книга '{book.get_title()}' недоступна")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            print(f"Пользователь {self.name} вернул книгу '{book.get_title()}'")
        else:
            print(f"Пользователь {self.name} не брал книгу '{book.get_title()}'")

    def show_books(self):
        if self.__borrowed_books:
            print(f"Книги, взятые пользователем {self.name}:")
            for book in self.__borrowed_books:
                print(f"- {book.get_title()}")
        else:
            print(f"Пользователь {self.name} не взял ни одной книги")

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        print(f"Библиотекарь {self.name} добавил книгу '{book.get_title()}'")

    def remove_book(self, library, title):
        library.remove_book(title)
        print(f"Библиотекарь {self.name} удалил книгу '{title}'")

    def register_user(self, library, user):
        library.add_user(user)
        print(f"Библиотекарь {self.name} зарегистрировал пользователя {user.name}")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                self.__books.remove(book)
                return
        print(f"!Книга '{title}' не найдена в библиотеке")

    def add_user(self, user):
        self.__users.append(user)

    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def show_all_books(self):
        if self.__books:
            print("Все книги в библиотеке:")
            for book in self.__books:
                print(book)
        else:
            print("В библиотеке нет книг")

    def show_available_books(self):
        available = [book for book in self.__books if book.is_available()]
        if available:
            print("Доступные книги:")
            for book in available:
                print(book)
        else:
            print("Нет доступных книг")

    # Приватный метод для поиска пользователя по имени
    def _find_user_by_name(self, user_name):
        return next((u for u in self.__users if u.name == user_name), None)

    # Проверяет наличие книги и пользователя, возвращает их или None при ошибке + выводит соответствующие сообщения об ошибках.
    def _validate_book_and_user(self, title, user_name):  #
        book = self.find_book(title)
        if not book:
            print(f"!Книга '{title}' не найдена")
            return None, None

        user = self._find_user_by_name(user_name)
        if not user:
            print(f"Пользователь {user_name} не зарегистрирован")
            return None, None

        return book, user

    def lend_book(self, title, user_name):
        book, user = self._validate_book_and_user(title, user_name)
        if book and user:
            user.borrow(book)

    def return_book(self, title, user_name):
        book, user = self._validate_book_and_user(title, user_name)
        if book and user:
            user.return_book(book)


# Пример использования
if __name__ == "__main__":
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)

    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    # --- пользователь смотрит свои книги ---
    user1.show_books()

    # --- возвращает книгу ---
    lib.return_book("Война и мир", "Анна")

    # --- электронная книга ---
    b2.download()

    # --- ремонт книги ---
    b3.repair()
    print(b3)