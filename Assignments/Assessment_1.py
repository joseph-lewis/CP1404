MENU = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    file_open = open("books.csv", 'r')
    book_info = refresh_book_list(file_open)
    file_open.close()
    count = len(book_info)
    print("Reading Tracker 1.0 - by Joseph Lewis\n{} books loaded from books.csv".format(count))
    print(MENU)
    menu_input = input(">>> ")
    while menu_input.lower() != "q":
        if menu_input.lower() == "l":
            pages_to_read = list_books(book_info)
            print("{} books.".format(count))
            if check_required_books(book_info) is True:
                print("You need to read {} pages in {} books.".format(sum(pages_to_read), len(pages_to_read)))
            else:
                print("No books left to read. Why not add a new book?")

        elif menu_input.lower() == "a":
            book_title, book_author, book_pages, adding_book_list = add_book()
            book_info.append(adding_book_list)
            print("{} by {}, ({} pages) added to Reading Tracker".format(book_title, book_author, book_pages))
        elif menu_input.lower() == "m":
            check = check_required_books(book_info)
            if check is True:
                pages_to_read = list_books(book_info)
                print("{} books.".format(count))
                print("You need to read {} pages in {} books.".format(sum(pages_to_read), len(pages_to_read)))
                print("Enter the number of the book to mark as completed")
                while True:
                    try:
                        delete_number = int(input(">>> "))
                        while delete_number <= 0 or delete_number > count:
                            if delete_number <= 0:
                                print("Number must be > 0")
                            else:
                                print("Invalid book number")
                            delete_number = int(input(">>> "))
                        mark_book(book_info, delete_number)
                        break
                    except ValueError:
                        print("Invalid input: enter a valid number")
            else:
                print("No required books")
        else:
            print("Invalid menu choice")
        count = len(book_info)
        print(MENU)
        menu_input = input(">>> ")
    file_write = open("books.csv", 'w')
    rewrite_book_file(file_write, book_info)
    file_write.close()
    print("{} books saved to books.csv\nHave a nice day :)".format(count))


def rewrite_book_file(file_write, book_info):
    file_write.seek(0)
    file_write.writelines(book_info)


def check_required_books(book_info):
    for line in book_info:
        if ",r" in line:
            return True


def mark_book(book_info, delete_number):
    if ",r" in book_info[delete_number - 1]:
        book_info[delete_number - 1] = book_info[delete_number - 1].split(",")[:3]
        book_info[delete_number - 1].append("c\n")
        book_title = book_info[delete_number - 1][0]
        book_author = book_info[delete_number - 1][1]
        book_info[delete_number - 1] = (",".join(book_info[delete_number - 1]))
        print("{} by {} completed!".format(book_title, book_author))
    else:
        print("This book is already completed!")


def add_book():
    adding_book_list = []
    book_title = input("Title: ")
    while book_title == "":
        print("Input cannot be blank")
        book_title = input("Title: ")
    book_author = input("Author: ")
    while book_author == "":
        print("Input cannot be blank")
        book_author = input("Author: ")
    while True:
        try:
            book_pages = int(input("Pages: "))
            while book_pages <= 0:
                print("Number must be > 0")
                book_pages = int(input("Pages: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    adding_book_list.append(book_title)
    adding_book_list.append(book_author)
    adding_book_list.append(str(book_pages))
    adding_book_list.append("r\n")
    adding_book_list = ",".join(adding_book_list)
    return book_title, book_author, book_pages, adding_book_list


def refresh_book_list(file_open):
    file_open.seek(0)
    book_info = file_open.readlines()
    return book_info


def list_books(book_info):
    count = 0
    pages_to_read = []
    for line in book_info:
        count += 1
        book_title = line.split(",")[0]
        book_author = line.split(",")[1]
        book_pages = line.split(",")[2]
        if ",r" in line:
            book_completed = "*"
            pages_to_read.append(int(book_pages))
        else:
            book_completed = ""

        print(
            "{:<1}{}. {:<40} by {:<20} {:>4} pages".format(book_completed, count, book_title, book_author, book_pages))
    return pages_to_read


main()
