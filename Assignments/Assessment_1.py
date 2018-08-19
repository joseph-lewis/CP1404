MENU = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    file_open = open("books.csv", 'a+')
    i = 0
    book_info = refresh_book_list(file_open)
    count = len(book_info)
    print("Reading Tracker 1.0 - by Joseph Lewis\n{} books loaded from books.csv\n".format(count))
    print(MENU)
    menu_input = input(">>> ")
    while menu_input.lower() != "q":
        if menu_input.lower() == "l":
            book_info = refresh_book_list(file_open)
            count = len(book_info)
            refresh_book_list(file_open)
            pages_to_read = list_books(book_info, i)
            print("{} books.".format(count))
            print("You need to read {} pages in {} books.\n".format(sum(pages_to_read), len(pages_to_read)))
        elif menu_input.lower() == "a":
            book_author, book_pages, book_title = add_book(file_open)
            print("{} by {}, ({} pages) added to Reading Tracker\n".format(book_title, book_author, book_pages))
        print(MENU)
        menu_input = input(">>> ")

    file_open.close()


def add_book(file_open):
    book_title = input("Title: ")
    file_open.write(book_title)
    file_open.write(",")
    book_author = input("Author: ")
    file_open.write(book_author)
    file_open.write(",")
    book_pages = input("Pages: ")
    file_open.write(book_pages)
    file_open.write(",r\n")
    file_open.flush()
    return book_author, book_pages, book_title


def refresh_book_list(file_open):
    file_open.seek(0)
    book_info = file_open.readlines()
    return book_info


def list_books(book_info, i):
    pages_to_read = []
    for line in book_info:
        i += 1
        book_title = line.split(",")[0]
        book_author = line.split(",")[1]
        book_pages = line.split(",")[2]
        if ",r" in line:
            book_completed = "*"
            pages_to_read.append(int(book_pages))
        else:
            book_completed = ""

        print("{:<1}{}. {:<40} by {:<20} {} pages".format(book_completed, i, book_title, book_author, book_pages))
    return pages_to_read


main()
