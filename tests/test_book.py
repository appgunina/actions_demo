import pytest
from src.library import Book, PrintedBook, EBook


def test_book_creation():
    b = Book("Title", "Author", 2000)
    assert b.get_title() == "Title"
    assert b.get_author() == "Author"
    assert b.get_year() == 2000
    assert b.is_available() is True


def test_book_mark_as_taken_returned():
    b = Book("T", "A", 2000)
    b.mark_as_taken()
    assert b.is_available() is False

    b.mark_as_returned()
    assert b.is_available() is True


def test_printed_book_repair():
    pb = PrintedBook("T", "A", 2000, 100, "плохая")
    pb.repair()
    assert pb.condition == "хорошая"

    pb.repair()
    assert pb.condition == "новая"


def test_ebook_creation():
    eb = EBook("T", "A", 2000, 10, "pdf")
    assert eb.file_size == 10
    assert eb.form == "pdf"
