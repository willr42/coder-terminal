import requests
import orjson
from Book import Book
from rich.table import Table

from exceptions import NetworkConnectivityError


class SearchHandler:

    API_URL = "http://openlibrary.org/search.json"

    def __init__(self, search_term: str):
        self.search_term = search_term

    def run_search(self):
        """Method responsible for running the search from start to finish."""
        try:
            self.search_response = self._perform_search()
            self.results_list = self._process_results()
            self._search_results = self._create_result_table()
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            raise NetworkConnectivityError

    @property
    def search_results(self):
        return self._search_results

    def _perform_search(self):
        search_term = self.search_term
        split_by_plus = search_term.replace(" ", "+")
        response = requests.get(
            SearchHandler.API_URL, params={"q": split_by_plus, "limit": 10}
        )
        return response.content

    def _process_results(self):
        search_response = self.search_response
        results = []
        processed = orjson.loads(search_response)
        for book_entry in processed["docs"]:
            new_book = Book(
                {
                    "title": book_entry.get("title"),
                    "author": book_entry.get("author_name", [""])[0],
                    "first_publish_year": book_entry.get("first_publish_year"),
                }
            )
            results.append(new_book)
        return results

    def _create_result_table(self):
        to_print = self.results_list
        table = Table(title="Search Results", show_lines=True)
        table.add_column("Choice Number", style="green")
        table.add_column("Title")
        table.add_column("Author")
        table.add_column("First Published")
        for index, book in enumerate(to_print, start=1):
            table.add_row(str(index), book.title, book.author, book.publication_year)
        return table

    def make_user_choice(self, user_index):
        return self.results_list[user_index - 1]
