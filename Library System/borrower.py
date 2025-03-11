# import the os module
import os

# import the `datetime.now()` and `timedelta()` functions from the 'datetime' module
from datetime import datetime, timedelta

# import functions file
import functions

# import the book class file
import book

# create a fake book object
fake_book_object = book.Book(1, "fake", "fake", "fake", True)


# our borrower's class
class Borrower:
    # constructor method
    def __init__(
        self, user_id: int, first_name: str, last_name: str, address: str, phone: str
    ):
        # initialise the attributes
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone

    # method to view all book(s) present in library system
    def view_all_borrowers(self):
        # exception handling
        try:
            # open the `borrower.txt` file for read
            with open(functions.borrower_data, "r") as borrower_file:
                # start reading each line in the 'book.txt' file
                for line in borrower_file:
                    # place each record into a list
                    record = line.strip().split(",")

                    # output the details for that borrower
                    print(
                        f"\t{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}"
                    )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to register borrower ==> save borrower to data file `borrower.txt`
    def register_borrower(self):
        # exception handling
        try:
            # ask the staff to enter details about new borrower
            borrower_fname = input("\t--> Please Enter Borrower First Name: ")
            borrower_lname = input("\t--> Please Enter Borrower Last Name: ")
            borrower_addr = input("\t--> Please Enter Borrower Address: ")
            borrower_phone = input("\t--> Please Enter Borrower Phone Number: ")

            # validate phone number ==> check if user input is a sequence of integer numbers
            while not (borrower_phone.isdigit() and len(borrower_phone) == 8):
                functions.print_dashed_lines()

                # output appropriate message
                print("\t<< Warning: 8 Integer Digits for Phone Number!!! >>")

                functions.print_dashed_lines()

                # ask the staff to enter phone number again
                borrower_phone = input(
                    "\t--> Please Enter Borrower Phone Number ( Again ): "
                )

            # call function to get the last borrower ID
            borrower_id = functions.last_borrower_id() + 1

            # open the `borrower.txt` file in append mode
            with open(functions.borrower_data, "a") as borrower_file:
                # write the details for new borrower
                borrower_file.write(
                    f"{borrower_id},{borrower_fname},{borrower_lname},{borrower_addr},{borrower_phone}\n"
                )

            functions.print_dashed_lines()

            # if registration of borrower successful ==> output appropriate message
            print("\t<< Borrower Successfully Added! >>")

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to deregister borrower ==> delete borrower data from file `borrower.txt`
    def deregister_borrower(self):
        # exception handling
        try:
            # open the `borrower.txt` file for read
            with open(functions.borrower_data, "r") as borrower_file:
                # open a temporary `temporary_file.txt` file in the same directory
                with open(
                    os.path.join(
                        functions.dir_path + "temporary_file.txt",
                    ),
                    "w",
                ) as temp_file:
                    # write the header to the temporary file
                    temp_file.write("Borrower ID,First Name,Last Name,Address,Phone\n")

                    # skip the header line found in 'borrower.txt' file
                    next(borrower_file)

                    # ask the staff to enter borrower ID to delete
                    staff_borrower_id_input = input(
                        "\n\t--> Please Enter Borrower ID: "
                    )

                    # create a status flag for that borrower ID
                    borrower_found = False

                    # start reading each line in the 'borrower.txt' file
                    for line in borrower_file:
                        # place each record into a list
                        record = line.strip().split(",")

                        # find the correct borrower ID from file
                        if staff_borrower_id_input == record[0]:
                            # change the status flag to `True`
                            borrower_found = True
                            # skip this current line to write ==> delete record needed
                            continue

                        # continue to write other "un-removed" records to `temporary_file.txt`
                        temp_file.write(line)

                    # if the borrower ID was not found
                    if not borrower_found:
                        functions.print_dashed_lines()

                        # output appropriate message
                        print(
                            f"\t<< Borrower ID '{staff_borrower_id_input}' Has NOT Been Found!!! >>"
                        )
                    else:
                        functions.print_dashed_lines()
                        # if deregistration of borrower successful ==> output appropriate message
                        print(
                            f"\t<< Borrower '{staff_borrower_id_input}' Successfully Deregistered! >>"
                        )

            # delete the original borrower data file
            os.remove(functions.borrower_data)
            # rename the temporary file to 'borrower.txt'
            os.rename(
                os.path.join(functions.dir_path + "temporary_file.txt"),
                functions.borrower_data,
            )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to update borrower ==> modify borrower data from file `borrower.txt`
    def update_borrower(self):
        # exception handling
        try:
            # open the `borrower.txt` file for read
            with open(functions.borrower_data, "r") as borrower_file:
                # open a temporary `temporary_file.txt` file in the same directory
                with open(
                    os.path.join(
                        functions.dir_path + "temporary_file.txt",
                    ),
                    "w",
                ) as temp_file:
                    # write the header to the temporary file
                    temp_file.write("Borrower ID,First Name,Last Name,Address,Phone\n")

                    # skip the header line found in 'borrower.txt' file
                    next(borrower_file)

                    # check if the borrower ID is present in the text file
                    result_borrower_id, borrower_id = functions.check_borrower_by_id()

                    # if the borrower ID has not been found in `borrower.txt` file
                    if not result_borrower_id:
                        # call the function to go back to borrower's sub-functions
                        functions.borrower_options()

                    # create a status flag for that borrower id
                    borrower_found = False

                    # start reading each line in the 'borrower.txt'
                    for line in borrower_file:
                        # place each record into a list
                        record = line.strip().split(",")

                        # find the correct borrower ID in file
                        if borrower_id == record[0]:
                            # change the status flag to `True`
                            borrower_found = True

                            # output appropriate message
                            print(
                                f"\t<< Enter New Credentials for Borrower '{borrower_id}' >>"
                            )

                            # ask the staff to enter new details for the borrower
                            record[1] = input("\n\t--> Enter New First Name: ")
                            record[2] = input("\t--> Enter New Last Name: ")
                            record[3] = input("\t--> Enter New Address: ")
                            record[4] = input("\t--> Enter New Phone Number: ")

                            # validate phone number ==> check if user input is a sequence of integer numbers
                            while not (record[4].isdigit()):
                                functions.print_dashed_lines()

                                # output appropriate message
                                print(
                                    "\t<< Warning: Integer Digits for Phone Number!!! >>"
                                )

                                # ask the staff to enter phone number again
                                record[4] = input(
                                    "\n\t--> Please Enter Borrower New Phone Number ( Again ): "
                                )

                        # write the new data to the temporary file
                        temp_file.write(
                            f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}\n"
                        )

                    # if the borrower ID was not found
                    if not borrower_found:
                        # call the function to print horizontal rule
                        functions.print_dashed_lines()

                        # output appropriate message
                        print(
                            f"\t<< Borrower ID '{borrower_id}' Has NOT Been Found!!! >>"
                        )
                    else:
                        functions.print_dashed_lines()
                        # if update of borrower details successful ==> output appropriate message
                        print(f"\t<< Borrower '{borrower_id}' Successfully Updated! >>")

            # delete the original borrower data file
            os.remove(functions.borrower_data)
            # rename the temporary file to 'borrower.txt'
            os.rename(
                os.path.join(functions.dir_path + "temporary_file.txt"),
                functions.borrower_data,
            )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to allow borrower to borrower books ==> save data to file `book_borrower.txt`
    def borrow_book(self, borrower_id: str):
        # exception handling
        try:
            # call function to list all available books
            fake_book_object.view_available_books()

            # ask the staff to enter book ID
            staff_book_id_input = input("\n\t--> Please Enter Book ID To Take: ")

            # call function to check if book ID entered is valid
            result_book_name = functions.check_book_by_id(staff_book_id_input)

            # if book ID has not been found
            if not result_book_name:
                # return the staff to the borrower's sub-option screen
                functions.borrower_options()

            # if book ID is valid ( present in system )

            # get the current date in the specified format
            start_date = datetime.now().strftime("%d/%m/%Y")
            # get the end data in the specified format
            end_date = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")

            # open 'book_borrower.txt' file for 'appending' records
            with open(functions.book_borrower_data, "a") as book_borrower_file:
                # write the data / record to the file
                book_borrower_file.write(
                    f"{borrower_id},{staff_book_id_input},{start_date},{end_date}\n"
                )

            # call function to change the book availability to `False`
            functions.change_borrow_book_availability(staff_book_id_input)

        # if file has not been found
        except FileNotFoundError:
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to allow borrower to return books ==> delete book-borrower data from file `book_borrower.txt`
    def return_book(self, borrower_id):
        # exception handling
        try:
            # ask the staff to enter book ID
            staff_book_id_input = input("\n\t--> Please Enter Book ID To Return: ")

            # call function to check if book ID entered is valid
            result_book_name = functions.check_book_by_id(staff_book_id_input)

            # if book ID has not been found
            if not result_book_name:
                # return the staff to the borrower's sub-option screen
                functions.borrower_options()

            # if book ID is valid ( present in system )

            # open 'book_borrower.txt' file for read
            with open(functions.book_borrower_data, "r") as book_borrower_file:
                # open a temporary `temporary_file.txt` file in the same directory
                with open(
                    os.path.join(
                        functions.dir_path + "temporary_file.txt",
                    ),
                    "w",
                ) as temp_file:
                    # write the header to the temporary file
                    temp_file.write("Borrower ID,ISBN,Start Date,End Date\n")

                    # skip the header line found in 'book_borrower.txt' file
                    next(book_borrower_file)

                    # create a status flag for book and borrower ID
                    book_borrower_found = False

                    # start reading each line in the 'book_borrower.txt'
                    for line in book_borrower_file:
                        # place record into a list
                        record = line.strip().split(",")

                        # find the correct borrower and book ID from file
                        if (
                            borrower_id == record[0]
                            and staff_book_id_input == record[1]
                        ):
                            # change the status flag to `True`
                            book_borrower_found = True
                            # skip the current line to write ==> delete record needed
                            continue

                        # continue to write other "un-removed" records to `temporary_file.txt`
                        temp_file.write(line)

                    functions.print_dashed_lines()

                    # output appropriate message
                    print("\n\t<< Book Successfully Returned >>")

                    # if the book and borrower ID was not found
                    if not book_borrower_found:
                        # call the function to print horizontal rule
                        functions.print_dashed_lines()

                        # output appropriate message
                        print(
                            f"\t<< Borrower ID '{borrower_id}' and Book ID '{staff_book_id_input}' Have NOT Been Found!!! >> \t"
                        )

            # delete the original book-borrower data file
            os.remove(functions.book_borrower_data)
            # rename the temporary file to 'book_borrower.txt'
            os.rename(
                os.path.join(functions.dir_path + "temporary_file.txt"),
                functions.book_borrower_data,
            )

            # call function to change the book availability to `False`
            functions.change_return_book_availability(staff_book_id_input)

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

    # method to allow staff to search borrower by borrower's ID
    def search_borrower_by_id(self):
        # exception handling
        try:
            # open the `borrower.txt` file for read
            with open(functions.borrower_data, "r") as borrower_file:
                # skip the header line found in 'borrower.txt' file
                next(borrower_file)

                # ask the staff to enter borrower ID to search
                staff_borrower_id_input = input("\t--> Please Enter Borrower ID: ")

                # create a status flag for borrower ID
                borrower_found = False

                # start reading each line in the 'borrower.txt' file
                for line in borrower_file:
                    # place contents of line in file
                    record = line.strip().split(",")

                    # find the correct borrower ID in file
                    if staff_borrower_id_input == record[0]:
                        # change the status flag to `True`
                        borrower_found = True

                        functions.print_dashed_lines()

                        # output appropriate message
                        print(f"\t<< Borrower '{record[0]}' Has Been Found >>\t")

                        # output the details for that borrower
                        print(f"\n\tFirst Name: {record[1]}")
                        print(f"\tLast Name : {record[2]}")
                        print(f"\tAddress: {record[3]}")
                        print(f"\tPhone: {record[4]}")

                # if the borrower was not found
                if not borrower_found:
                    # call the function to print horizontal rule
                    functions.print_dashed_lines()

                    # output appropriate message
                    print(
                        f"\t<< Borrower ID '{staff_borrower_id_input}' Has NOT Been Found!!! >> \t"
                    )

        # if file has not been found
        except FileNotFoundError:
            # output appropriate message
            print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")
