# coder-terminal
Repository for my terminal app for Coder Academy, GreatReads. It is a CLI library management app (as in physical books) that enables the user to create a library, populate it with shelves, and populate those shelves with books.

# Source Code
Source code is provided [on Github](https://github.com/willr42/coder-terminal).

# Style Guide
This codebase follows the [PEP8 style](https://peps.python.org/pep-0008/) using [black](https://github.com/psf/black) for automatic code formatting. No more manual indenting!

# How to use this program
!TODO!
- installation steps
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

# Feature list
## Library Management
- A first-time user is able to create a new Library that will track their books.
- A returning user is greeted with their existing Library, loaded from JSON on disk.
- Upon exiting, the user's Library is serialized & saved as JSON.
## Shelf Management
- A user with no shelves is able to add a new shelf.
- A user with shelves is automatically shown the first shelf in the list. This shelf displays a summary of all the books within the shelf.
- A user can sort the shelf by book title, author name, publication date.
- A user can delete a shelf.
## Book Management
- A user can add a book to the active shelf.
- A user can delete a book from the active shelf.
- A user can add a book manually by inputting the book title, author name & publication date.
- A user can search for a book by ISBN (results provided by the OpenLibrary API).
- A user can search for a book by fuzzy strings (results provided by the OpenLibrary API).
- A user can edit the details of an existing book.

# Implementation plan
Implementation is formally tracked [on Trello](https://trello.com/b/8nrTX4Wp/greatreads).
1. Scaffold the views. Library view, Shelf view & Book view.
2. Develop the Book class.
3. Develop the Library class.
4. Develop the Shelf class.
5. Connect the views with the logic of the classes.
6. Develop the Add Book feature.
7. Develop the sorting of shelves.
8. Develop on-disk persistence.
