# import the os module
import os

# import functions file
import functions


# our book's class
class Book:
    # constructor method
    def __init__(
        self, ISBN: int, book_name: str, author: str, category: str, availabilty: bool
    ):
        # initialise attributes
        self.ISBN = ISBN
        self.book_name = book_name
        self.author = author
        self.category = category
        self.availability = availabilty

    # method to view all book(s) present in library system
    def view_all_books(self):
        # exception handling
        try:
            # open the `book.txt` file for read
            with open(functions.book_data, "r") as book_file:
                # start reading each line in the 'book.txt' file
                for line in book_file:
                    # place each record into a list
                    record = line.strip().split(",")

                    # output the details for that book
                    print(
                        f"\t{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}"
                    )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to view all available book ==> book's availability = True
    def view_available_books(self):
        # exception handling
        try:
            # create a status flag for that book's availabilty
            book_found = False

            # open the `book.txt` file for read
            with open(functions.book_data, "r") as book_file:
                # skip the header line found in 'borrower.txt' file
                next(book_file)

                # output header to the screen
                print("\tISBN | Book Name | Author | Category")

                # start reading each line in the 'book.txt' file
                for line in book_file:
                    # place each record into a list
                    record = line.strip().split(",")

                    # check book's availability
                    if record[4] == "True":
                        # meaning that the book is available ==> change status flag
                        book_found = True

                        # output the details for that book
                        print(
                            f"\t{record[0]} | {record[1]} | {record[2]} | {record[3]}"
                        )

            # if the book availability was `False`
            if not book_found:
                functions.print_dashed_lines()

                # output appropriate message
                print("\t<< Warning: There Are NO Books Available!!! >>")

                # return the staff to the book sub-functions screen
                functions.book_options()

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to add books ==> save book to data file `book.txt`
    def add_book(self):
        # ask the staff to enter details about new book
        book_name = input("\t--> Please Enter Book Name: ")
        book_author = input("\t--> Please Enter Author: ")
        book_category = input("\t--> Please Enter Book Category: ")

        # by default if book recently added ==> availability = `True`
        book_status = True

        # call function to get the last book ID
        book_id = functions.last_book_id() + 1

        # open the `book.txt` file in append mode
        with open(functions.book_data, "a") as book_file:
            # write the details for new book
            book_file.write(
                f"{book_id},{book_name},{book_author},{book_category},{book_status}\n"
            )

        # output appropriate message
        print("\n\t<< Book Successfully Added >>")

    # method to remove books ==> delete book data from file `book.txt`
    def delete_book(self):
        # exception handling
        try:
            # open the `book.txt` file for read
            with open(functions.book_data, "r") as book_file:
                # open a temporary `temporary_file.txt` file in the same directory
                with open(
                    os.path.join(
                        functions.dir_path + "temporary_file.txt",
                    ),
                    "w",
                ) as temp_file:
                    # write the header to the temporary file
                    temp_file.write("ISBN,Book Name,Author,Category,Availability\n")

                    # skip the header line found in 'book.txt' file
                    next(book_file)

                    # ask the staff to enter book ID to delete
                    staff_book_id_input = input("\t--> Please Enter Book ID: ")

                    # create a status flag for that book ID
                    book_found = False

                    # start reading each line in the 'book.txt' file
                    for line in book_file:
                        # place record into a list
                        record = line.strip().split(",")

                        # find the correct book ID from file
                        if staff_book_id_input == record[0]:
                            # change the statuses flag to `True`
                            book_found = True
                            # skip the current line to write ==> delete record needed
                            continue

                        # continue to write other "un-removed" records to `temporary_file.txt`
                        temp_file.write(line)

                    # if the book ID was found
                    if book_found:
                        # call the function to print horizontal rule
                        functions.print_dashed_lines()

                        # output appropriate message
                        print("\t<< Book Successfully Removed >>")

                    # if the book ID was not found
                    if not book_found:
                        # call the function to print horizontal rule
                        functions.print_dashed_lines()

                        # output appropriate message
                        print(
                            f"\t<< Book ID '{staff_book_id_input}' Has NOT Been Found!!! >>"
                        )

            # delete the original book data file
            os.remove(functions.book_data)
            # rename the temporary file to 'book.txt'
            os.rename(
                os.path.join(functions.dir_path + "temporary_file.txt"),
                functions.book_data,
            )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to allow staff to search book by book's name
    def search_book_by_name(self):
        # exception handling
        try:
            # open the `book.txt` file for read
            with open(functions.book_data, "r") as book_file:
                # skip the header line found in 'book.txt' file
                next(book_file)

                # ask the staff to enter book name to search
                staff_book_name_input = input("\t--> Please Enter Book Name: ")

                # create a status flag for book name
                book_found = False

                # start reading each line in the 'book.txt' file
                for line in book_file:
                    # place record into a list
                    record = line.strip().split(",")

                    # find the correct book name in file
                    if staff_book_name_input.lower() == record[1].lower():
                        # change the status flag to `True`
                        book_found = True

                        functions.print_dashed_lines()

                        # output appropriate message
                        print(f"\t<< Book '{record[1]}' Has Been Found >>")

                        # output the details for that book
                        print(f"\n\tISBN: {record[0]}")
                        print(f"\tAuthor : {record[2]}")
                        print(f"\tCategory: {record[3]}")
                        print(f"\tAvailability: {record[4]}")

                # if the book ID was not found
                if not book_found:
                    # call the function to print horizontal rule
                    functions.print_dashed_lines()

                    # output appropriate message
                    print(
                        f"\t<< Book '{staff_book_name_input}' Has NOT Been Found!!! >>"
                    )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")
