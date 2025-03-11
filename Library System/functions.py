# import the os module
import os

# import the `datetime()` and `now()` functions from the 'datetime' module
from datetime import datetime

# import the borrower class file
import borrower

# import the book class file
import book

# import the `sleep` function from the 'time' module
from time import sleep

# import the `getpass` function from the 'getpass' module
from getpass import getpass

# variable that holds the directory where files are stored
dir_path = os.path.expanduser("~/Desktop/Library System/data_files/")

# get the full path with the file name of each data file
book_data = os.path.join(dir_path + "book.txt")
borrower_data = os.path.join(dir_path + "borrower.txt")
book_borrower_data = os.path.join(dir_path + "book_borrower.txt")

# create a fake borrower object
fake_borrower_object = borrower.Borrower(1, "fake", "fake", "fake", "1234")
# create a fake book object
fake_book_object = book.Book(1, "fake", "fake", "fake", True)


# function to display '-' in a line
def print_dashed_lines(char_count: int = 70):
    print()
    print("-" * char_count)
    print()


# function to return borrower ID and book ID
def return_borrower_book_id(returning_date: str):
    try:
        # open 'book_borrower.txt' file for read
        with open(book_borrower_data, "r") as book_borrower_file:
            # skip the header line found in 'book.txt' file
            next(book_borrower_file)

            # create a status flag for that book-borrower
            book_borrower_found = False

            # split the returning date into a list
            returning_date_split = returning_date.split("/")

            # get the individual data
            day = int(returning_date_split[0])
            month = int(returning_date_split[1])
            year = int(returning_date_split[2])

            print_dashed_lines()

            # output appropriate message
            print("\t--<< Borrower ID and Book ID >>--\n")

            # start reading each line in the 'book-borrower.txt'
            for line in book_borrower_file:
                # place record into a list
                record = line.strip().split(",")

                # find the correct borrower ID and book ID for that end date
                if record[3] == returning_date:
                    # change the status flag to `True`
                    book_borrower_found = True

                    # ouput the data / record
                    print(f"\tBorrower ID: {record[0]} | Book ID: {record[1]}")

                    # if any borrower needs to return book(s) on `returning_date`
                    if returning_date == datetime.now().strftime("%d/%m/%Y"):
                        # output appropriate message
                        print(
                            f"\t<< Borrower '{record[0]}' Need to Return Book '{record[1]}' Today!!! >>"
                        )

                    # if any borrower has exceed the deadline for the returning date
                    elif datetime(year, month, day) < datetime.now():
                        # calculate the number of days ( difference between 2 dates )
                        num_of_days = (datetime.now() - datetime(year, month, day)).days

                        print_dashed_lines()

                        # output appropriate message
                        print(
                            f"\t<< '{num_of_days}' Day(s) Has Passed Since Borrower '{record[0]}' Has Not Returned Book '{record[1]}' >>"
                        )

            # if the book ID was not found
            if not book_borrower_found:
                print_dashed_lines()

                # output appropriate message
                print(f"\t<< End Date '{returning_date}' Has NOT Been Found!!! >> \t")

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

        print_dashed_lines()


# function to change a specific book's availabilty to `True`
def change_return_book_availability(book_id: str):
    # exception handling
    try:
        # open 'book.txt' file for read
        with open(book_data, "r") as book_file:
            # open a temporary `temporary_file.txt` file in the same directory
            with open(
                os.path.join(
                    dir_path + "temporary_file.txt",
                ),
                "w",
            ) as temp_file:
                # write the header to the temporary file
                temp_file.write("ISBN,Book Name,Author,Category,Availability\n")

                # skip the header line found in 'book.txt' file
                next(book_file)

                # create a status flag for that book ID
                book_found = False

                # start reading each line in the 'book.txt'
                for line in book_file:
                    # place record into a list
                    record = line.strip().split(",")

                    # find the correct book ID in file `book.txt`
                    if book_id == record[0]:
                        # change the status flag to `True`
                        book_found = True

                        # change the availability of the specified book to `True`
                        record[4] = "True"

                    # write the new data to the temporary file
                    temp_file.write(
                        f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}\n"
                    )

                # if the book ID was not found
                if not book_found:
                    print_dashed_lines()

                    # output appropriate message
                    print(f"\t<< Book ID '{book_id}' Has NOT Been Found!!! >> \t")

        # delete the original book data file
        os.remove(book_data)
        # rename the temporary file to 'book.txt'
        os.rename(
            os.path.join(dir_path + "temporary_file.txt"),
            book_data,
        )

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

        print_dashed_lines()


# function to change a specific book's availabilty to `False`
def change_borrow_book_availability(book_id: str):
    # exception handling
    try:
        # open 'book.txt' file for read
        with open(book_data, "r") as book_file:
            # open a temporary `temporary_file.txt` file in the same directory
            with open(
                os.path.join(
                    dir_path + "temporary_file.txt",
                ),
                "w",
            ) as temp_file:
                # write the header to the temporary file
                temp_file.write("ISBN,Book Name,Author,Category,Availability\n")

                # skip the header line found in 'book.txt' file
                next(book_file)

                # create a status flag for that book ID
                book_found = False

                # start reading each line in the 'book.txt'
                for line in book_file:
                    # place record into a list
                    record = line.strip().split(",")

                    # find the correct book ID in file `book.txt`
                    if book_id == record[0]:
                        # change the status flag to `True`
                        book_found = True

                        # change the availability of the specified book to `False`
                        record[4] = "False"

                    # write the new data to the temporary file
                    temp_file.write(
                        f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}\n"
                    )

                # if the book ID was not found
                if not book_found:
                    print_dashed_lines()

                    # output appropriate message
                    print(f"\t<< Book ID '{book_id}' Has NOT Been Found!!! >> \t")

        # delete the original book data file
        os.remove(book_data)
        # rename the temporary file to 'book.txt'
        os.rename(
            os.path.join(dir_path + "temporary_file.txt"),
            book_data,
        )

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

        print_dashed_lines()


# function to check if book is in library system ( book data file )
def check_book_by_id(book_id: str, file_path: str = book_data) -> bool:
    # exception handling
    try:
        # open 'book.txt' file for read
        with open(file_path, "r") as book_file:
            # skip the header line found in 'book.txt' file
            next(book_file)

            # create a status flag for book ID
            book_found = False

            # start reading each line in the 'book.txt' file
            for line in book_file:
                # place each record into a list
                record = line.strip().split(",")

                # find the correct book ID in file
                if book_id == record[0]:
                    # change the status flag to `True`
                    book_found = True

                    print_dashed_lines()

                    # output appropriate message
                    print(f"\t << Book Name {book_id} Has Been Found >>\t")

                    # return `True` as book ID is found
                    return True

            # if the book ID was not found
            if not book_found:
                print_dashed_lines()

                # output appropriate message
                print(f"\t<< Book '{book_id}' Has NOT Been Found!!! >> \t")

                # return `False` as book ID has not been found
                return False

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

        print_dashed_lines()

        # ==> book has not been found; return `False`
        return False


# function to check if borrower is in system ( return status only as tuple )
def check_borrower_by_id(file_path: str = borrower_data) -> (bool, str):
    # exception handling
    try:
        # open the `borrower.txt` file for read
        with open(file_path, "r") as borrower_file:
            # skip the header line found in 'borrower.txt' file
            next(borrower_file)

            # ask the staff to enter borrower ID to find
            staff_borrower_id_input = input("\t--> Please Enter Borrower ID: ")

            # create a status flag for borrower ID
            borrower_found = False

            # start reading each line in the 'borrower.txt' file
            for line in borrower_file:
                # place each record into a list
                record = line.strip().split(",")

                # find the correct borrower ID from file
                if staff_borrower_id_input == record[0]:
                    # change the status flag to `True`
                    borrower_found = True

                    print_dashed_lines()

                    # if check of borrower ID successful ==> output appropriate message
                    print(
                        f"\t<< Borrower '{staff_borrower_id_input}' Has Been Found! >>"
                    )

                    print_dashed_lines()

                    # return `True` as borrower ID is found
                    return True, staff_borrower_id_input

            # if the borrower was not found
            if not borrower_found:
                # call the function to print horizontal rule
                print_dashed_lines()

                # output appropriate message
                print(
                    f"\t<< Borrower ID '{staff_borrower_id_input}' Has NOT Been Found!!! >>"
                )

                # return the staff to the borrower sub-functions screen
                borrower_options()

                # return `False` as borrower ID has not been found
                return False

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: File Not Found... Please Check File Directory!!! >>")

        print_dashed_lines()

        # meaning that borrower ID has not been found
        return False


# function to get last borrower ID from `borrower.txt` file
def last_borrower_id(file_path: str = borrower_data) -> int:
    # exception handling
    try:
        # open the `borrower.txt` file for read
        with open(file_path, "r") as borrower_file:
            # start reading each line in the file
            for line in borrower_file:
                # skip every record in the file
                pass

            # retrieve the last data / record in list
            last_record = line.split(",")

            # retrieve the last borrower ID only
            last_id = last_record[0]

            # finally return the ID as an integer number
            return int(last_id)

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: Please Check File Directory >>")

        print_dashed_lines()

        # if file not found ==> no books in file
        return 0


# function to get last book ID from `book.txt` file
def last_book_id(file_path: str = book_data) -> int:
    # exception handling
    try:
        # open the `book.txt` file for read
        with open(file_path, "r") as book_file:
            # start reading each line in the file
            for line in book_file:
                # skip every record in the file
                pass

            # retrieve the last data / record in list
            last_record = line.split(",")

            # retrieve the last book ID only
            last_id = last_record[0]

            # finally return the ID as an integer number
            return int(last_id)

    # if file has not been found
    except FileNotFoundError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Critical: Please Check File Directory >>")

        print_dashed_lines()

        # if file not found ==> no books in file
        return 0


# function to go to borrower sub-functions
def borrower_options():
    # exception handling
    try:
        # output the borrower's sub-options to staff
        print_dashed_lines()
        print("\t--<< Borrower Sub-Functions Menu >>--\n")

        print("\tOption[1]: Register Borrower")
        print("\tOption[2]: Deregister Borrower")
        print("\tOption[3]: Update Borrower Details")
        print("\tOption[4]: Borrow Book")
        print("\tOption[5]: Return Book")
        print("\tOption[X]: Back ( to Main Library Functions )")

        # ask the staff to select an option in borrower sub-function
        staff_user_option = input("\n\t--> Please Select an Option: ")

        print_dashed_lines()

        # evaluate the staff input depending on sub-option selected
        if staff_user_option == "1":
            # staff wants register borrower
            print("\t--<< Register Borrower >>--")

            # ask the staff how many borrowers to register
            register_amount = int(
                input("\n\t--> Please Enter Amount of Borrowers to Register: ")
            )

            # iterate through the amount of borrowers to register
            for i in range(register_amount):
                print_dashed_lines()

                print(f"\t<< Register Borrower #{i + 1} >>\n")

                # call the "method" `register_borrower` from the class of borrower
                fake_borrower_object.register_borrower()

            # return the staff to the borrower's sub-option screen ==> call itself
            borrower_options()

        elif staff_user_option == "2":
            # staff wants delete borrower from system
            print("\t--<< Deregister Borrower >>--")

            # ask the staff how many borrowers to deregister
            deregister_amount = int(
                input("\n\t--> Please Enter Amount of Borrowers to Deregister: ")
            )

            # loop through the amount of borrowers
            for i in range(deregister_amount):
                print_dashed_lines()

                print(f"\t<< Deregister Borrower #{i + 1} >>")

                # call the "method" `deregister_borrower` from the class of borrower
                fake_borrower_object.deregister_borrower()

            # return the staff to the borrower sub-functions screen
            borrower_options()

        elif staff_user_option == "3":
            # staff wants update borrower
            print("\t--<< Update Borrower Data >>--")

            # ask the staff how many borrowers to update
            update_amount = int(
                input("\n\t--> Please Enter Amount of Borrowers to Update: ")
            )

            # loop through the amount of borrowers
            for i in range(update_amount):
                print_dashed_lines()

                print(f"\t<< Update Borrower #{i + 1} >>\n>>")

                # call the "method" `update_borrower` from the class of borrower
                fake_borrower_object.update_borrower()

            # return the staff to the borrower sub-functions screen
            borrower_options()

        elif staff_user_option == "4":
            # borrower wants to borrow books
            print("\t--<< Borrow Book(s) >>--\n")

            # check if the borrower ID is present in the text file
            result_borrower_id, borrower_id = check_borrower_by_id()

            # if the borrower ID has not been found in `borrower.txt` file
            if not result_borrower_id:
                # call the function to go back to borrower's sub-functions
                borrower_options()

            # ask the staff to enter amount of books to borrow by borrower
            borrow_amount = int(input("\t--> Please Enter Amount of Books to Borrow: "))

            # loop through the amount of borrowers
            for i in range(borrow_amount):
                print_dashed_lines()

                print(f"\t<< Borrower ID '{borrower_id}' -  Book #{i + 1} >>\n")

                # call the "method" `borrow_book` from the class of borrower
                fake_borrower_object.borrow_book(borrower_id)

            # return the staff to the borrower sub-functions screen
            borrower_options()

        elif staff_user_option == "5":
            # borrower wants to return books
            print("\t--<< Return Book(s) >>--\n")

            # check if the borrower ID is present in the text file
            result_borrower_id, borrower_id = check_borrower_by_id()

            # if the borrower ID has not been found in `borrower.txt` file
            if not result_borrower_id:
                # call the function to go back to borrower's sub-functions
                borrower_options()

            # ask the staff to enter amount of books to return by borrower
            return_amount = int(input("\t--> Please Enter Amount of Books to Return: "))

            # loop through the amount of borrowers
            for i in range(return_amount):
                print_dashed_lines()

                print(f"\t<< Borrower ID '{borrower_id}' -  Book #{i + 1} >>")

                # call the "method" `return_book` from the class of borrower
                fake_borrower_object.return_book(borrower_id)

            # return the staff to the borrower sub-functions screen
            borrower_options()

        elif staff_user_option == "X" or staff_user_option == "exit":
            # staff wants to go back to library's main functions
            display_main_options()

        else:
            # staff does not enter correct option ==> output appropriate message
            print("\t<< Wrong Option Selected... Please Try Again! >>")

            # call this very function again
            borrower_options()

    # if the staff to does not enter integer values when needed
    except ValueError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Warning: Please Enter Integer Data Where Required!!! >>")

        # call this very function again
        borrower_options()


# function to go to book sub-functions
def book_options():
    # exception handling
    try:
        # output the book's sub-options to staff
        print_dashed_lines()
        print("\t--<< Book Sub-Functions Menu >>--\n")

        print("\tOption[1]: View Available Books")
        print("\tOption[2]: Add Books")
        print("\tOption[3]: Delete Book")
        print("\tOption[X]: Back ( to Main Library Functions )")

        # ask the staff to select an option in book sub-function
        staff_book_option = input("\n\t--> Please Select an Option: ")

        print_dashed_lines()

        # evaluate the staff input depending on sub-option selected
        if staff_book_option == "1":
            # staff wants to view available books
            print("\t--<< View Available Books >>--\n")

            # call the "method" `view_available_books` from the class book
            fake_book_object.view_available_books()

            # return the staff to the book sub-functions screen
            book_options()

        elif staff_book_option == "2":
            # staff wants add book into the system
            print("\t--<< Add Book(s) >>--\n")

            # ask the staff how many books to add
            book_amount = int(input("\t--> Please Enter Amount of Books to Add: "))

            # iterate through the amount of books to add
            for i in range(book_amount):
                print_dashed_lines()

                print(f"\t<< Book #{i + 1} >>\n")

                # call the "method" `add_book` from the class book
                fake_book_object.add_book()

            # return the staff to the book sub-functions screen
            book_options()

        elif staff_book_option == "3":
            # staff wants delete book from the system
            print("\t--<< Delete Book(s) >>--\n")

            # ask the staff how many books to remove
            book_amount = int(input("\t--> Please Enter Amount of Books to Remove: "))

            # iterate through the amount of books to add
            for i in range(book_amount):
                print_dashed_lines()

                # call the "method" `delete_book` from the class book
                fake_book_object.delete_book()

            # return the staff to the book sub-functions screen
            book_options()

        elif staff_book_option == "X" or staff_book_option == "exit":
            # staff wants to go back to library's main functions
            display_main_options()

        else:
            # if staff does not enter correct option ==> output appropriate message
            print("\t<< Wrong Option Selected... Please Try Again! >>")

            # call this very function again
            book_options()

    # if the staff to does not enter integer values when needed
    except ValueError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Warning: Please Enter Integer Data Where Required!!! >>")

        # call this very function again
        book_options()


# function to go to book sub-functions
def general_functions():
    # exception handling
    try:
        print_dashed_lines()
        # output the borrower's sub-options to staff
        print("\t--<< Library General Sub-Functions Menu >>--\n")

        print("\tOption[1]: View All Books")
        print("\tOption[2]: View All Borrowers")
        print("\tOption[3]: Search Borrower ( By ID )")
        print("\tOption[4]: Search Book ( By Name )")
        print("\tOption[5]: Return Borrower ID and Book ID ( Based On Returning Date )")
        print("\tOption[X]: Back ( to Main Library Functions )")

        # ask the staff to select an option in general sub-function
        staff_general_option = input("\n\t--> Please Select an Option: ")

        print_dashed_lines()

        # evaluate the staff input depending on sub-option selected
        if staff_general_option == "1":
            # staff wants view all books present in library system
            print("\t--<< View All Book(s) >>--\n")

            # call the "method" `view_all_books` from the class book
            fake_book_object.view_all_books()

            # return the staff to the general sub-functions screen
            general_functions()

        elif staff_general_option == "2":
            # staff wants view all borrower present in library system
            print("\t--<< View All Borrower(s) >>--\n")

            # call the "method" `view_all_borrowers` from the class borrower
            fake_borrower_object.view_all_borrowers()
            # call the "method" from the class of book

            # return the staff to the general sub-functions screen
            general_functions()

        elif staff_general_option == "3":
            # staff wants to search book by book's name
            print("\t--<< Search Borrower(s) >>--\n")

            # ask the staff how many books to search
            borrower_amount = int(
                input("\t--> Please Enter Amount of Borrowers to Search: ")
            )

            # iterate through the amount of borrowers to search
            for i in range(borrower_amount):
                print_dashed_lines()

                print(f"\t<< Borrower Search #{i + 1} >>\n")

                # call the "method" `search_borrower_by_id` from the class borrower
                fake_borrower_object.search_borrower_by_id()

            # return the staff to the general sub-functions screen
            general_functions()

        elif staff_general_option == "4":
            # staff wants search book from the system
            print("\t--<< Search Book(s) >>--\n")

            # ask the staff how many books to search
            book_amount = int(input("\t--> Please Enter Amount of Books to Search: "))

            # iterate through the amount of books to search
            for i in range(book_amount):
                print_dashed_lines()

                print(f"\t<< Book Search #{i + 1} >>\n")

                # call the "method" `search_book_by_name` from the class book
                fake_book_object.search_book_by_name()

            # return the staff to the general sub-functions screen
            general_functions()

        elif staff_general_option == "5":
            # staff wants to list all borrowers and book ID based on End Date
            print("\t--<< Search Borrower(s) ID and Book(s) ID >>--\n")

            # ask the staff how many different date to search / amount of dates
            date_amount = int(input("\t--> Please Enter Amount of End Dates: "))

            # iterate through the amount of date
            for i in range(date_amount):
                print_dashed_lines()

                print(f"\t<< Date Search #{i + 1} >>\n")

                # ask the staff to enter 'end date' to find
                staff_date_input = input(
                    "\t--> Please Enter Returning Date ( DD/MM/YYYY ) : "
                )

                # validate the date input ==> turn input into a list
                list_date = staff_date_input.split("/")

                while (
                    # if there are not 3 parts
                    len(list_date) != 3
                    # if the first part is not a number and its length is not 2
                    or (len(list_date[0]) != 2 or not list_date[0].isdigit())
                    # if the first part is not a number and its length is not 2
                    or (len(list_date[1]) != 2 or not list_date[1].isdigit())
                    # if the first part is not a number and its length is not 4
                    or (len(list_date[2]) != 4 or not list_date[2].isdigit())
                ):
                    print_dashed_lines()

                    print("\t<< Wrong Date Format... Please Try Again!!! >>")

                    print_dashed_lines()

                    # ask the staff to enter 'end date' to find again
                    staff_date_input = input("\t--> Please Enter Date ( Again ): ")

                    # validate the date input ==> turn input into a list ( again )
                    list_date = staff_date_input.split("/")

                # call the fucntion `return_borrower_book_id`
                return_borrower_book_id(staff_date_input)

            # return the staff to the general sub-functions screen
            general_functions()

        elif staff_general_option == "X" or staff_general_option == "exit":
            # staff wants to go back to library's main functions
            display_main_options()

        else:
            # if staff does not enter correct option ==> output appropriate message
            print("\t<< Wrong Option Selected... Please Try Again! >>")

            # return the staff to the general sub-functions screen
            general_functions()

    # if the staff to does not enter integer values when needed
    except ValueError:
        print_dashed_lines()

        # output appropriate message
        print("\t<< Warning: Please Enter Integer Data Where Required!!! >>")

        # call this very function again
        general_functions()


# function to exit the program at login screen
def exit_in_login(staff_name: str, staff_passwd: str):
    # staff enters the "secret" combination ==> exit program
    if staff_name == "0" and staff_passwd == "0":
        # exit with style
        good_bye = "\t<< Good Bye! >>\n"

        # iterate through the sentence
        for ch in good_bye:
            # output each character in the sentence
            print(ch, end="", flush=True)
            # sleep the program for 0.09 seconds
            sleep(0.09)

        # call function to display horizontal rule
        print_dashed_lines()

        # exit the program without any "errors" ( exit status code = 0 )
        exit(0)


# function to login staff into system
def login_screen():
    # staff enter login screen
    print("\t--<< Login to Library System >>--")

    print_dashed_lines()

    # ask the staff to enter username
    staff_name = input("\tUsername: ")
    # ask the staff to enter password ( similar in Arch Linux --> password not shown )
    passwd = getpass("\tPassword: ")

    print_dashed_lines()

    # call the function `exit_in_login` to check if staff wants to exit program
    exit_in_login(staff_name, passwd)

    # check if staff username and password is correct; else continue to ask
    while staff_name != "Sunitilesh" or passwd != "1234":
        # output appropriate message
        print("\t<< Wrong Credentials >>")

        # ask the user to enter credentials again
        print_dashed_lines()
        staff_name = input("\tUsername: ")
        passwd = getpass("\tPassword: ")
        print_dashed_lines()

        # call the function `exit_in_login` to check if staff wants to exit program
        exit_in_login(staff_name, passwd)


# function to display the main options to staff
def display_main_options():
    # staff enter library's main functions screen
    print("\t--<< Library Main Functions >>--\t\n")

    # display library main options
    print("\tOption[1]: Borrower Functions")
    print("\tOption[2]: Book Functions")
    print("\tOption[3]: General Functions")
    print("\tOption[X]: Log Out")

    # ask the staff to select an option in library main function
    staff_main_option = input("\n\t--> Please Select an Option: ")

    # evaluate the staff input depending on option selected
    if staff_main_option == "1":
        # staff wants to go to borrower's sub-options
        borrower_options()

    elif staff_main_option == "2":
        # staff wants to go to book's sub-options
        book_options()

    elif staff_main_option == "3":
        # staff wants to go to general library sub-functions
        general_functions()

    # condition to check if staff wants to go back to login screen
    elif staff_main_option == "X" or staff_main_option == "exit":
        print_dashed_lines()

        # staff wants to go log out to "login" screen
        login_screen()
    # if staff does not enter correct option ==> output appropriate message

    else:
        print_dashed_lines()

        # if staff does not enter correct option ==> output appropriate message
        print("\t<< Wrong Option Selected... Please Try Again! >>")

        print_dashed_lines()

        # call this very function again
        display_main_options()
