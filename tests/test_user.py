from src.library import User, Book


def test_user_borrow_available_book():
    user = User("Ира")
    book = Book("T", "A", 2000)

    user.borrow(book)

    assert book in user.get_borrowed_books()
    assert book.is_available() is False


def test_user_borrow_unavailable_book():
    user1 = User("Ира")
    user2 = User("Антон")
    book = Book("T", "A", 2000)

    user1.borrow(book)
    user2.borrow(book)

    assert book in user1.get_borrowed_books()
    assert book not in user2.get_borrowed_books()


def test_user_return_book_success():
    user = User("Ира")
    book = Book("T", "A", 2000)

    user.borrow(book)
    user.return_book(book)

    assert book not in user.get_borrowed_books()
    assert book.is_available() is True


def test_user_return_book_not_owned():
    user = User("Ира")
    book = Book("T", "A", 2000)

    user.return_book(book)

    # книга должна остаться доступной
    assert book.is_available() is True
