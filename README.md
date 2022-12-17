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

- [x] A first-time user is able to create a new Library that will track their books.
- [x] A returning user is greeted with their existing Library, loaded from JSON on disk.
- [ ] Upon exiting, the user's Library is serialized & saved as JSON.

## Shelf Management

- [x] A user with no shelves is able to add a new shelf.
- [x] A user with shelves selects the shelf they wish to be active. This shelf displays a summary of all the books within the shelf.
- [ ] A user can sort the shelf by book title, author name, publication date.
- [x] A user can delete a shelf.

## Book Management

- [x] A user can add a book to the active shelf.
- [x] A user can delete a book from the active shelf.
- [x] A user can add a book manually by inputting the book title, author name & publication date.
- [ ] A user can search for a book by fuzzy strings (results provided by the OpenLibrary API).
- [x] A user can edit the details of an existing book.

# Implementation plan

Implementation is formally tracked [on Trello](https://trello.com/b/8nrTX4Wp/greatreads). I have adopted an Agile-style methodology where I assign Story Points to specific tasks. These story points represent a rough guess at the amount of work required to implement a particular feature.

1. Scaffold the views. Library view, Shelf view & Book view.
2. Develop the Book class.
3. Develop the Library class.
4. Develop the Shelf class.
5. Connect the views with the logic of the classes.
6. Develop the Add Book feature.
7. Develop the sorting of shelves.
8. Develop on-disk persistence.

## Implementation progress

![First progress shot.](./docs/progress-00-overview.jpg)
Initial setup of the trello board.

![Overview after first sprint.](./docs/progress-01-overview.jpg)
Overview after first dev sprint. Some tasks completed.

![Library task card](./docs/progress-01-library.jpg)
Card of Library features.

![Persistence task card](./docs/progress-01-persistence.jpg)
Card of Persistence features.

![Shelf task card - unfinished](./docs/progress-02-shelves.jpg)
An in-progress task; building menus took longer than anticipated.

![Overview after second sprint.](./docs/progress-03-overview.jpg)
More progress after second sprint. Cards beginning to be ticked off, and updated with comments.

Some under-estimated story points, some over, so I had to also tweak those along the way.

![Shelf task card - finished](./docs/progress-03-shelves.jpg)
Shelf card is feature-complete.

![Book task card - to test](./docs/progress-03-books.jpg)
Books just need a unit test for editing functionality.