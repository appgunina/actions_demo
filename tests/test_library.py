from src.library import Library, Book, User, Librarian


def test_library_add_and_find_book():
    lib = Library()
    b = Book("T", "A", 2000)
    lib.add_book(b)

    found = lib.find_book("T")
    assert found == b


def test_library_remove_book():
    lib = Library()
    b = Book("T", "A", 2000)
    lib.add_book(b)

    lib.remove_book("T")
    assert lib.find_book("T") is None


def test_library_remove_book_not_exists():
    lib = Library()
    lib.remove_book("Нет книги")   # должно вывести print, но ошибок быть не должно


def test_library_add_user_and_lend_book():
    lib = Library()
    user = User("Ира")
    book = Book("T", "A", 2000)

    lib.add_book(book)
    lib.add_user(user)

    lib.lend_book("T", "Ира")

    assert book in user.get_borrowed_books()
    assert book.is_available() is False


def test_library_lend_book_user_not_found():
    lib = Library()
    book = Book("T", "A", 2000)
    lib.add_book(book)

    lib.lend_book("T", "Неизвестный")  # просто проверяем отсутствие ошибки

    assert book.is_available() is True


def test_library_lend_book_not_found():
    lib = Library()
    user = User("Ира")
    lib.add_user(user)

    lib.lend_book("Нет книги", "Ира")  # просто проверяем отсутствие ошибки


def test_library_return_book():
    lib = Library()
    user = User("Ира")
    book = Book("T", "A", 2000)

    lib.add_book(book)
    lib.add_user(user)

    lib.lend_book("T", "Ира")
    lib.return_book("T", "Ира")

    assert book.is_available() is True
    assert book not in user.get_borrowed_books()
