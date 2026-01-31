# import pytest

import requests_mock

from potterapi_hook import PotterApiHook


def test_get_books_en():

    hook = PotterApiHook(base_url="https://test.com")

    expected_books = [
        {
            "number": 1,
            "title": "Test Title 1",
            "originalTitle": "Harry Potter and the Sorcerer's Stone",
            "pages": 223,
            "index": 0,
        },
        {
            "number": 2,
            "title": "Test Title 2",
            "originalTitle": "Harry Potter and the Chamber of Secrets",
            "pages": 251,
            "index": 1,
        },
    ]

    with requests_mock.mock() as m:

        m.get(
            url="https://test.com/en/books",
            json=expected_books,
        )

        actual_books = hook.get_books()

        assert m.last_request.hostname == "test.com"
        assert m.last_request.path == "/en/books"
        assert actual_books == expected_books


# test called uk endpoint
def test_get_books_uk():

    hook = PotterApiHook(base_url="https://test.com", default_lang="uk")

    expected_books = [
        {
            "number": 1,
            "title": "Тестовий Том 1",
            "originalTitle": "Harry Potter and the Sorcerer's Stone",
            "pages": 223,
            "index": 0,
        },
        {
            "number": 2,
            "title": "Тестовий Том 2",
            "originalTitle": "Harry Potter and the Chamber of Secrets",
            "pages": 251,
            "index": 1,
        },
    ]

    with requests_mock.mock() as m:

        m.get(
            url="https://test.com/uk/books",
            json=expected_books,
        )

        actual_books = hook.get_books()

        assert m.last_request.hostname == "test.com"
        assert m.last_request.path == "/uk/books"
        assert actual_books == expected_books
