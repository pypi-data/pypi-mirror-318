# metasbooks-client
Python client librairie for the MetasBooks api https://metasbooks.fr/

# Requirements

You need a valid account on [MetasBooks](https://metasbooks.fr) with a valid API Key.

# Installation

```bash
pip install metasbooks
```

# Usage

```python
from metasbooks import Book, MetasBooks

client = MetasBooks(api_key="My API Key")
book: Book = client.get_book(ean='9791032925430')
print(book)
```
