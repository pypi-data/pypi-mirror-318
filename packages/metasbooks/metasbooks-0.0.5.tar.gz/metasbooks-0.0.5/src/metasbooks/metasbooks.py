import json
import os
from typing import Optional

import requests

from .book import Book


class MetasBooks:
    def __init__(self, api_key: str, cache_dir: Optional[str] = None):
        self._api_key = api_key
        self._cache_dir = cache_dir

    def get_book(self, ean: str) -> Book:
        if self._cache_dir is not None:
            book_data = self._get_book_data_from_cache(ean, self._cache_dir)
            if book_data is not None:
                return Book(**book_data)
        book_data = self._fetch_book_data(ean)
        if book_data.get("code_reponse") != 1:
            raise Exception(f"MetasBooks API returned an error: {book_data['reponse']}")
        if self._cache_dir is not None:
            self._save_book_data_to_cache(ean, book_data, self._cache_dir)
        return Book(**book_data)

    def _fetch_book_data(self, ean: str) -> dict:
        response = requests.get(
            f"https://metasbooks.fr/api/lookup_metas.php?apikey={self._api_key}&format=json&ean={ean}"
        )
        return response.json()

    @staticmethod
    def _get_book_data_from_cache(ean: str, cache_dir: str):
        cache_file = os.path.join(cache_dir, f"{ean}.json")
        if os.path.exists(cache_file):
            with open(cache_file, "r") as file:
                return json.load(file)
        return None

    @staticmethod
    def _save_book_data_to_cache(ean: str, book_data: dict, cache_dir: str):
        cache_file = os.path.join(cache_dir, f"{ean}.json")
        os.makedirs(cache_dir, exist_ok=True)
        with open(cache_file, "w", encoding="utf-8") as file:
            json.dump(book_data, file, ensure_ascii=False, indent=4)
