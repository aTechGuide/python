from typing import List, Dict, Union

from database_connection import DatabaseConnection

"""
Concerned with storing and retrieving books from a database
"""

Book = Dict[str, Union[str, int]]

def create_book_table() -> None: # " -> None" is called Type Hints
  with DatabaseConnection('resources/database/data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_book(name: str, author: str) -> None:
  with DatabaseConnection('resources/database/data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
  

def get_all_books() -> List[Book]:
  with DatabaseConnection('resources/database/data.db') as connection:
    cursor = connection.cursor()
    
    cursor.execute('SELECT * from books')
    # cursor.fetchall() => [(name, author, read), (name, author, read)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

  return books

def mark_book_as_read(name: str) -> None:
  with DatabaseConnection('resources/database/data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 where name=?', (name,))


def delete_book(name: str) -> None:
  with DatabaseConnection('resources/database/data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('DELETE from books where name=?', (name,))
