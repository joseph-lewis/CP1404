MENU = "Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    book_info = []
    file_open = open("books.csv", 'r+')
    for line in file_open:
        book_info.append(line)
    book_info = refresh_book_list(file_open)
    count = len(book_info)
    print("Reading Tracker 1.0 - by Joseph Lewis\n{} books loaded from books.csv\n".format(count))
    print(MENU)
    menu_input = input(">>> ")
    while menu_input.lower() != "q":
        if menu_input.lower() == "l":
            book_info = refresh_book_list(file_open)
            list_books(book_info)
        elif menu_input.lower() == "a":
            book_title, book_author, book_pages, adding_book_list = add_book()
            book_info.append(adding_book_list)
            rewrite_book_file(file_open, book_info)
            print("{} by {}, ({} pages) added to Reading Tracker\n".format(book_title, book_author, book_pages))
        elif menu_input.lower() == "m":
            check = check_required_books(book_info)
            if check is True:
                list_books(book_info)
                print("Enter the number of the book to mark as completed")
                delete_number = int(input(">>> "))
                mark_book(book_info, delete_number, file_open)
                rewrite_book_file(file_open, book_info)
            else:
                print("No required books")
        print(MENU)
        menu_input = input(">>> ")

    file_open.close()

def rewrite_book_file(file_open, book_info):
    file_open.truncate(0)
    file_open.seek(0)
    file_open.writelines(book_info)
    file_open.flush()

def check_required_books(book_info):
    for line in book_info:
        if ",r" in line:
            return True


def mark_book(book_info, delete_number, file_open):
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
    book_author = input("Author: ")
    book_pages = input("Pages: ")
    adding_book_list.append(book_title)
    adding_book_list.append(book_author)
    adding_book_list.append(book_pages)
    adding_book_list.append("r\n")
    adding_book_list = ",".join(adding_book_list)
    return book_title, book_author, book_pages, adding_book_list


def refresh_book_list(file_open):
    file_open.seek(0)
    book_info = file_open.readlines()
    return book_info


def list_books(book_info):
    i = 0
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

        print("{:<1}{}. {:<40} by {:<20} {:>4} pages".format(book_completed, i, book_title, book_author, book_pages))
    print("{} books.".format(i))
    print("You need to read {} pages in {} books.\n".format(sum(pages_to_read), len(pages_to_read)))


main()
