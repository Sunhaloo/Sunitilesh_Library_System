---
id: Programming Assignment ( L1S2 ) - OOP With Text Files
aliases: Object Oriented Programming with Text Files Assignment ( Level 1 Semester 2 )
tags:
  - uni
  - uom
  - theory
  - python
module: ICDT 1201Y
author: S.Sunhaloo
date: 2025-03-11
status: In-Progress
---

## List of Contents

- [[#Introduction]]
- [[#Definition of the Problem]]
- [[#Proposed Solution]]
- [[#Scope]]
	- [[#Functionalities]]
	- [[#Limitations]]
- [[#Distribution of Work]]
- [[#Solution Design - Unified Modelling Language (Case Diagram)]]
- [[#Implementation and Testing]]
	- [[#System Requirements]]
	- [[#Implementation of Main Components]]
	- [[#Testing with Screenshots]]
- [[#Conclusion]]
	- [[#Achievements]]
	- [[#Challenges - Problems Encountered]]
	- [[#Future Work]]
- [[#References]]
- [[#Appendix]]
	- [[#Full Code]]

---

>[!INFO] Tools Used
>- Programming Language: [Python](https://python.org)
>- Markdown with [Obsidian](https://obsidian.md/) for Report Writing
>
>>[!TIP] METHILESH Ramsahye's (2413415) Coding Setup
>>- Text Editor: [Visual Studio Code](https://code.visualstudio.com/)
>>	- Plugins:
>>		- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
>>- Terminal Emulator: [Windows Terminal](https://github.com/microsoft/terminal)
>>- Shell: [Powershell](https://github.com/PowerShell/PowerShell)
>
>>[!TIP] SUNHALOO Shehzaad's (2412274) Coding Setup
>>- Text Editor: Neovim
>>	- Plugins:
>>		- Please visit [dotfiles]() GitHub Repository for more information
>>		- Language Servers: [pyright](https://github.com/microsoft/pyright)
>>		- Code Formatter: [black](https://pypi.org/project/black/)
>>		- Linter: [ruff](https://github.com/astral-sh/ruff/)
>>- Terminal Emulator: [kitty](https://github.com/kovidgoyal/kitty)
>>- Shell: [zsh](https://sourceforge.net/projects/zsh/)
>
>>[!NOTE] Bold and Italic Colours in Report
>>We are currently using the theme [OneNice](https://gitub.com/Sunhaloo/OneNice). This is the reason why '**bolds**' are <span style="color: green;">green</span> and *italics* are <span style="color: red;">red</span>!
>
>>[!TIP] GitHub Link
>>Please visit the 'https://github.com/Sunhaloo/Sunitilesh_Library_System' for all the codes and also and data files.
>>
>>>[Methilesh Ramsahye (2413415)](https://github.com/methileshramsahye) is a **collaborator** in this repository.
>>

---

# Introduction

"*Sunitilesh's Books*" is a small library where individuals can register to borrow books for up to **30 days**. The library is managed solely by Mr. Sunitilesh, the owner. Located in the heart of Port Louis, his business has recently experienced a surge in visitors due to extensive online promotion. However, managing borrower and book records has become increasingly challenging, as all data is currently recorded manually using pen and paper. This outdated method makes it difficult to keep track of books and borrower details efficiently, leading to potential errors and delays.

# Definition of the Problem

The library currently relies on manual record-keeping using pen and paper to store all data related to books and borrowers. This method presents several disadvantages:

- Time Wastage
	- Rewriting existing information (manually) $\rightarrow$ Duplication
	- Difficulty in correcting unintended changes to records
- Inefficient Search Process
	- Finding specific borrower or book details is slow and cumbersome
- Error Prone
	- Increased risk of human errors such as incorrect phone numbers written

# Proposed Solution

To help Mr. Sunitilesh manage a growing number of borrowers more efficiently, we propose a **computerised library management system**. This system will be developed using **Python** and will store and manipulate data using **text files**.

Our solution aims to **minimise the challenges** the library owner faces in managing the business, specifically:

1. Efficient Data Storage $\Rightarrow$ Systematically storing information on books and borrowers
2. Data Management $\Rightarrow$ Allowing easy manipulation and updating of records
3. Automated Alerts $\Rightarrow$ Displays warning messages for missing records, invalid inputs, overdue books, and other errors to ensure data integrity and user guidance.

---

# Scope

## Functionalities

### Borrower Functionalities

- **Register New Borrowers**  
  - Stores borrower details, including `Borrower ID`, `First Name`, `Last Name`, `Address`, and `Phone Number`.  

- **Remove Inactive Borrowers**  
  - De-registers borrowers who are no longer using the library.  

- **Update Borrower Information**  
  - Allows modifications to existing borrower details.  

- **Borrowing Limit Enforcement**  
  - Restricts each borrower to a maximum of **three books** at a time.  

- **Book Return Management**  
  - Enables borrowers to return borrowed books and updates the system accordingly.

### Book Functionalities

- **View Available Books**  
  - Displays a list of books that are currently available for borrowing.  

- **Add New Books**  
  - Stores book details, including `ISBN`, `Book Name`, `Author`, `Category`, and `Availability`.  

- **Remove Old Books**  
  - Deletes outdated or unavailable books from the system.  

### General Library Functionalities

- View all books present in the system.
- View all borrowers present in the system.
- Search for a borrower using the `Borrower ID`.
- Search for a book using the `Book Name`.
- Input end date $\rightarrow$ Return Borrower ID and Book ID.
    - Outputs a warning message if the borrower needs to return the book today.
    - If the end date has passed, outputs the number of days that have passed since the return date.

## Limitations

1. **No Graphical User Interface (GUI)**, only a Terminal User Interface (TUI)
    - People with no knowledge of terminal emulators, consoles, or shells might have trouble using the program.
    
2. **Security**: Data in the file can be changed outside of the program
    - Anyone with physical access to the computer can use text editors like Sumblime or Notepad to modify the data in the file.

3. **No backup or rollback functionality for text files** (if the user has not set up automatic backups or does not perform regular backups).

4. **All data for a borrower must be re-entered**, even if only one detail for that borrower is changed.

5. **Only warning messages are displayed to the staff (Mr. Sunitilesh)**
    - No emails or other notifications are sent automatically to the borrower.

6. **Files must already be created and initialised** with the respective headers in the directory `~/Desktop/Library System/date_files`.
	- This is because Mr. Sunitilesh will be using Notepad to rewrite all existing data from his notebook
7. All IDs ( *for `book.txt` and `borrower.txt`* ) should start will `1`.


# Distribution of Work

Below is a table outlining the tasks completed by each of us:

| **SUNHALOO Shehzaad** (2412274) | **METHILESH Ramsahye** (2413415) |
| ----------------------------- | ------------------------------ |
| View All Borrower | View All Books |
| Register Borrowers | View Available Books |
| Deregister Borrowers | Add Books |
| Update Borrowers | Delete Books |
| Borrow Books | Search Book By Name |
| Return Books | Change Return Book Availability |
| Search Borrower By ID | Change Borrow Book Availability |
| Return Borrower Book ID | Last Borrower ID |
| Check Book ID | Last Book ID |
| Check Borrower ID | Book Option |
| Borrower Option | Display Main Option |
| General Option | Exit In Login |
| Login Screen | Main Function |
| Report Writing | UML Design |

---

# Solution Design - Unified Modelling Language (Case Diagram)

Here is our [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) Case Diagram $\downarrow$

![[Programming Assignment - UML Diagram.png | 575]]

---

# Implementation and Testing

## System Requirements

- **Operating System**:
	- Linux, MacOS or Windows
- **Programming Language**:
	- Python 3.10 and above
- **Text Files**:
	- `book.txt`, `borrower.txt`, and `book_borrower.txt` located in the directory `~/Desktop/Library System/date_files`
	- The files should be correctly formatted with headers and appropriate data fields for proper functioning.

>[!NOTE]
>Mr. Sunitilesh did not specify whether he is knowledgeable with computers.
>
>As a result, we decided not to use Python libraries that require installation via package managers such as `pip` or `uv`. 
>Instead, we have only utilised the built-in libraries that come with the default Python installation when installed through your system's package manager (e.g., `pacman`, `apt`, `winget`).


## Implementation of Main Components

The image below $\downarrow$ shows the '*flow*' of our program.

![[Programming Assignment Functions.png | 900]]

>[!WARNING]
>Given that we have a total of **28** functions and/or methods, 
>we will **not** be detailing the implementation of **all** of them. 
>Instead, we will focus on showing how we implemented the main/core functions and methods.
>
>>For the full code, please refer to the [[#Appendix]].
>

---

### Before We Start

Here is what we imported and created in each of our 4 files.

>[!INFO] Our Main File
>We only have 1 `import` in our `main.py` file.
>
>```python
># import functions file
>import functions
>```
>

>[!INFO] Our Functions File
>This is everything that we imported and created (*objects and variables*) in our `functions.py` file.
>
>```python
># import the os module
>import os
>
># import the `datetime()` and `now()` functions from the 'datetime' module
>from datetime import datetime
>
># import the borrower class file
>import borrower
>
># import the book class file
>import book
>
># import the `sleep` function from the 'time' module
>from time import sleep
>
># import the `getpass` function from the 'getpass' module
>from getpass import getpass
>
># variable that holds the directory where files are stored
>dir_path = os.path.expanduser("~/Desktop/Library System/data_files/")
>
># get the full path with the file name of each data file
>book_data = os.path.join(dir_path + "book.txt")
>borrower_data = os.path.join(dir_path + "borrower.txt")
>book_borrower_data = os.path.join(dir_path + "book_borrower.txt")
>
># create a fake borrower object
>fake_borrower_object = borrower.Borrower(1, "fake", "fake", "fake", "1234")
># create a fake book object
>fake_book_object = book.Book(1, "fake", "fake", "fake", True)
>```

>[!INFO] Our Book File
>This is everything that we imported in our `book.py` file.
>
>```python
># import the os module
>import os
>
># import functions file
>import functions
>```
>

>[!INFO] Our Borrower File
>This is everything that we imported and created (*objects and variables*) in our `borrower.py` file.
>
>

### Data In Files

As mentioned in the [[#Limitations]] (*check number 6*), all the files will already contain some data. Hence, we have also provided the data that is currently in all of the files.  

#### Book File

Here is the current contents of the `book.txt` file

```console
ISBN,Book Name,Author,Category,Availability
1,To Kill a Mockingbird,Harper Lee,Classic Literature,True
2,1984,George Orwell,Dystopian,False
3,The Great Gatsby,F. Scott Fitzgerald,Classic Literature,True
4,Moby-Dick,Herman Melville,Adventure,True
5,The Catcher in the Rye,J.D. Salinger,Fiction,True
6,War and Peace,Leo Tolstoy,Historical Fiction,False
7,Pride and Prejudice,Jane Austen,Classic Literature,True
8,Brave New World,Aldous Huxley,Dystopian,True
9,The Lord of the Rings,J.R.R. Tolkien,Fantasy,True
10,The Hobbit,J.R.R. Tolkien,Fantasy,True
```

#### Borrower File

```console
Borrower ID,First Name,Last Name,Address,Phone
1,Emma,Johnson,123 Maple Street,55512345
2,Liam,Smith,456 Oak Avenue,55567890
3,Olivia,Brown,789 Pine Road,55591012
4,Noah,Williams,321 Birch Lane,55511223
5,Ava,Jones,654 Cedar Drive,55533445
6,William,Miller,987 Spruce Court,55555667
7,Sophia,Davis,741 Elm Street,55577889
8,James,Garcia,852 Walnut Avenue,55599001
9,Isabella,Martinez,369 Chestnut Blvd,55522334  
10,Benjamin,Anderson,159 Redwood Terrace,55544556  
```

#### Book-Borrower File

```console
Borrower ID,ISBN,Start Date,End Date
```

---

### METHILESH Ramsahye (2413415)

#### Class Book

Below are some of the most important **methods** pertaining to the `Book` class.

##### `add_book()` Method

```python
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
```

In this case, this method allows the staff to enter details about the book that needs to be added.  
We then have a function, `last_book_id()`, which opens the file in read mode and extracts the 'Book ID' of the last record.  
This allows us to increment the 'Book ID' by 1 for the new book being added.  

Additionally, the status of the new book will **always** have a default value of `True`.  

All of this data is then written to the `book.txt` file, whose full path is stored in the variable `book_data` (*defined in `functions.py`*), which holds the string value `~/Desktop/Library System/data_files/book.txt`.  

Finally, a message is displayed to the staff confirming that the book has been successfully added.

---

###### `last_book_id()` Function

Here is how this function works.

```python
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
```

The function expects the full file path (*again, `~/Desktop/Library System/data_files/book.txt`*) as a parameter. It then opens the file in read mode and **skips** all the records in the file.  

This means that the variable `line` will still contain the last actual line/record in the file.  
Therefore, we store that record in a list, but first, we need to split it using the `,` character.  

Hence, we can easily find the last 'Book ID', as the first/$0^{th}$ index will **always** contain the 'Book ID'.  
Finally, the function returns that number as an integer.  

However, if the specified file path does not exist, an appropriate message will be displayed, and the function will return `0`.  

> Referring to the [[#Limitations]], we can see that all IDs should start at 1.  

---

##### `delete_book()` Method

```python
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
```

As we are deleting or modifying a value in a text file, we need to follow these steps:

1. Open the existing file in read mode.
2. Create a temporary file.
3. Modify the required data.
4. Write all the updated data to the temporary file.
5. Delete the original text file.
6. Rename the temporary text file to the original filename.

>The above steps $\uparrow$ describe how operating systems handle file modifications; this is not specific to any programming language!

Similarly, this method creates the status flag `book_found`. If the 'Book ID' matches an entry in `book.txt`, that line is skipped using the `continue` keyword, while all other records are written to the temporary file `temporary_file.txt`.

Finally, if the status flag is set to `True` $\Rightarrow$ A message confirming that the book has been removed will be displayed.

At this point, the original `book.txt` file is deleted, and `temporary_file.txt` is renamed to `book.txt`.

If `book_found` remains `False`, an appropriate message will be displayed accordingly.

#### General Functions

##### `change_borrow_availability()` Function

```python
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
```

This function, which is found in the `functions.py` file, is a function that will change the 'Availability' of a book from `True` to `False`.  

The function requires `book_id` to be passed as a parameter so that it can find the correct 'Book ID' in order to change the availability of that specific book.  

Again, as we are modifying an *attribute* in our `book.txt` file, the steps mentioned above $\uparrow$ for the previous method `delete_book()` still apply here.

>This function is used in the `borrow_books()` method, where the availability of a book changes when...

##### `change_return_availability()` Function

This is essentially the same function as the one above, but instead of changing the 'Availability' of a book from `True` to `False`, it does the complete opposite.  

> This function is used together with the `return_book()` method!  

Here is the code snippet showing where `change_return_availability()` differs from `change_borrow_availability()` $\downarrow$:  


```python
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
```

### SUNHALOO Shehzaad (2412274)

#### Borrower Class

##### `borrow()` Method

```python
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
```

This method first calls the `view_available_books()` function so that the staff or borrower can see all the currently available books (*where 'Availability' is `True`*).  

The program then prompts the staff to enter the 'Book ID' of the book the borrower wants to take. It then calls another function, `check_book_by_id()`, from `functions.py`, which expects a 'Book ID' as a parameter. Hence, it verifies whether the entered 'Book ID' is valid.  

If the entered 'Book ID' is invalid or not present in the `book.txt` file, an appropriate message is displayed on the screen.  

> Note that the `print()` statement for this message is located within that function itself.  

However, if all checks pass, the program calculates the current/today’s date and the due date (30 days from today).  

After that, the program opens the `book_borrower.txt` file in append mode and adds the correct data.  

Finally, the function [[#`change_borrow_availability()` Function | `change_borrow_availability()`]] is called to update the 'Availability' attribute to `False` for that specific book.  


##### `return_book()` Method

```python
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
```

This function is, in principle, similar to the `borrow_book()` method but does the complete opposite.  

Again, as we are updating or modifying a text file, we need to follow the same steps mentioned above $\uparrow$.  

Here as well, the program prompts the staff to enter the 'Book ID' of the book the borrower wants to return. It then calls the same `check_book_by_id()` function to verify whether the 'Book ID' is valid or present in the `book.txt` file.  

Finally, after removing the correct record from the `book_borrower.txt` file, the function `change_return_book_availability()` from `functions.py` is called to update the book's 'Availability' attribute from `False` to `True`.  

> Please refer to [[#`change_return_availability()` Function | `change_return_availability()` function]] for more information.  

#### General Functions

##### `return_borrower_book_id()` Method

```python
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
```

This function, which is found in the `functions.py` file itself, allows the staff to enter a "*due date*" and then returns the 'Borrower ID' along with the 'Book ID' that the borrower needs to return.  

If the return date is in the past, the function calculates the number of days elapsed and displays an appropriate message on the screen.  

The function expects a returning date in the format `DD/MM/YYYY`, which has already been validated (*see code below $\downarrow$*). It then places the returning date into a list, splitting each element by the `/` character. From this list, the day, month, and year are extracted, and the `datetime` module from `datetime` is used to check whether the returning date is the same as today or in the past.  

Again, if the date entered is in the past, the number of days between today and the "*old*" due date will be calculated and displayed accordingly with an appropriate message.  

###### Date Format Validation Code

```python
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
```

## Testing with Screenshots

### Login Screen

#### Test Case 1: Correct Username and Password

Please enter the following username and password:

```console
Username: Sunitilesh
Password: 1234
```

![[login - right username - passwd.png | 625]]

#### Test Case 2: Correct Username and Incorrect Password

Please enter the following username and password:

```console
Username: Sunitilesh
Password: password
```

![[login - right username - wrong passwd.png | 625]]

#### Test Case 3: Incorrect Username and Correct Password

Please enter the following username and password:

```console
Username: username
Password: 1234
```

![[login - wrong username - right passwd.png | 625]]

#### Test Case 4: Incorrect Username and Incorrect Password

Please enter the following username and password:

```console
Username: username
Password: password
```

![[login - wrong username - passwd.png | 625]]

### Register Borrowers

>Please refer to [[#Data In Files]] for the original/current data in the files.

#### Before we Register

Here are the details of our new borrower that we are going to register.

```console
First Name,Last Name, Address, Phone
Test First Name,Test Last Name,Test Address,Test Phone Number
```

>[!INFO]
>
>>[!NOTE] Borrower ID Value
>>Our 'Borrower ID' is automatically incremented based on the last 'Borrower ID' found in the `borrower.txt` file.
>>This is done using the function `last_borrower_id()` which is found in the `functions.py` file itself.
>
>>[!NOTE] Phone Number Format - Validation
>>Phone number should be in the Mauritian mobile phone number format ( *exclude country code, i.e `+230`* ).
>>
>>Meaning that the phone number should only contain 8 digits.
>

#### Testing Registering of Borrower

>Please note that we are expecting the user to be able to select and option using the keyboard.

In this is case, we are starting at the 'Borrower Sub-Functions Menu'

##### Steps

1. The program is going to ask the user to enter the number of borrower to register

![[register borrower - screen.png | 625]]

2. Enter required details about the new borrower

>In this case we are intentionally making a **mistake** for the Phone Number.

![[register borrower - wrong phone.png | 625]]

3. Therefore, go ahead and enter correct phone number

| Correct Phone Number |
| -------------------- |
| 52647986 |

![[register borrower - correct phone.png | 625]]

Therefore if we head over to the directory `~/Desktop/Library System/data_files` and the following command:

- For Linux / MacOS Users

```bash
cat borrower.txt | grep "Test First Name"
```

- For Windows Users

```powershell
Get-Content borrower.txt | findstr "Test First Name"
```

Hence, we should be able to get the following result $\downarrow$:

```console
11,Test First Name,Test Last Name,Test Address,52647986
```

### Search Borrower by ID

As we have just registered the new borrower, and we know that their ID is `11`, we are going to use our program to check if our search functionality is working.

#### Steps

After registering the borrower, we are going to return to the same 'Borrower Sub-Functions Menu'. Therefore, please navigate to our 'General Option' using the numbers or alphabet in the menu.

You should then arrive at this screen $\downarrow$:

![[main option to general option.png | 625]]

1. Enter a wrong option like `something`

>This should return a <span style="color: orange;">warning</span> message and send us **back** to the *General Sub-Functions Menu*!

![[general option - wrong option entered.png | 625]]

2. Now, select option `3` to go to the search function

![[search borrower option.png | 625]]

3. In this case, enter `3` for the amount of borrower to search

![[search borrower - amount.png | 625]]

4. Therefore, go ahead and enter our newly registered borrower's ID which is `11`

![[search borrower - right ID.png | 625]]

5. Now, we are going to search for an ID that is not present in our `borrower.txt` file

![[search borrower - wrong ID.png | 625]]

6. We are now going to enter and **invalid** borrower ID

>In this case, we should get a <span style="color: orange;">warning</span> message and program should go back to *General Sub-Functions Menu*

![[search borrower - invalid ID.png | 625]]

### View All Borrowers in System

#### Steps

Now, after using/entering the invalid borrower ID. You should find yourself in the *General Sub-Functions Menu* again.

We are going to view all the current borrowers that are in the library system

1. Therefore, select `2`

>All the borrower should be displayed

![[general - view all borrowers.png | 625]]

### View All Books in System

Similar, if we wanted to view all the books that are in library, whether the 'Availability' is `True`/`False.

1. Hence, instead of selecting `2`... Select `1`

![[general - view all books.png | 625]]

### Borrow Books

Our newly registered borrower wants to borrow a book. Hence, go back to the *Borrower Sub-Functions Menu*

#### Steps

1. In the borrower menu, select the option 'Borrow Book'

>You will then be presented with this screen

![[borrower option - borrower ID book.png | 625]]

2. Thus, enter `11` for the 'Borrower ID'

![[borrower option - amount book borrow.png | 625]]

3. In this case, the borrower wants to borrower 2 books. Hence enter `2` for the amount of books to borrow

![[borrower option - take book 1.png | 625]]

>The program will then display all the **available** books and will ask the staff to enter the 'Book ID' that the user wants to take

4. Borrower wants to take the book 'To Kill a Mockingbird' and also 'War and Peace'

- Taking the book 'To Kill a Mockingbird'

![[borrower option - take book 1.png | 625]]

- Taking the book 'War and Peace'

![[borrower option - taken book 2.png | 625]]

>Again, after taking $x$ amount of books... The program will go back to the *Borrower Sub-Functions Menu*. 

#### View All Available Books Again

Therefore, if we head back to our *Book Sub-Functions Menu*, and select 'View Available Books'. We should get an output like this $\downarrow$.

![[book option - view available.png | 625]]

### Return Book

No head over back to our *Borrower Sub-Function Menu* and select 'Return Book'

1. Provide the program with the Borrower ID of the person who wants to return book(s).

![[borrower option - return book amount.png | 625]]

2. Now, enter `2` for the amount of books to return

>Note that the borrower only wants to return a single book!

![[borrower option - return valid book.png | 625]]

3. The borrower wants to return the book 'To Kill a Mockingbird'

![[borrower option - returned valid book.png | 625]]

4. Go ahead and enter the following book ID, i.e `100`

![[borrower option - returned invalid book.png | 625]]

As the 'Book ID' has **not** been found... The program sends us back to the *Borrower Sub-Functions Menu*.

### Given Due Date - Output Borrower and Book ID

If we again `cat` / `Get-Content` for our `book_borrower.txt` file. we should have something have this $\downarrow$:

```console
Borrower ID,ISBN,Start Date,End Date
11,6,11/03/2025,10/04/2025
```

>We only have 1 record as borrower `11` has already returned a book!

Let's go ahead and *forcefully* add 2 fake records. Please enter the following data into the `book_borrower.txt` file

```console
100,44,02/12/2024,01/01/2025
101,33,08/02/2025,10/03/2025
```

No, go to our *General Sub-Functions Menu* and select `5` to arrive at the screen below $\downarrow$:

![[general function - return ID amount.png | 625]]

#### Test Case 1: Invalid Date Format

Please enter the following date:

```console
Date Format: 10th April 2025
```

>![[general option - invalid date 1.png | 625]]

Please enter the following date:

```console
Date Format: 10-04-2025
```

>![[general option - invalid date 2.png | 625]]

Please enter the following date:

```console
Date Format: 10/4/2025
```

>![[general option - invalid date 3.png | 625]]

#### Test Case 2: Valid Date Format

Please enter the following date:

```console
Date Format: 10/04/2025
```

>![[general option - right date 1.png | 625]]

#### Test Case 3: Date is 10/03/2025

![[general option - right date 3.png | 625]]

#### Test Case 4: Date is 26/09/2003

>![[general option - right date 4.png | 625]]


# Conclusion

In summary, the new system helps Mr. Sunitilesh manage his library more efficiently by digitising borrower and book records. With this program, tracking books and borrower details becomes easier, reducing errors and saving time compared to the previous manual method.

## Achievements

- Works on any computer as long as the [[#System Requirements]] are met $\checkmark$  
- Stores digital information on books and borrowers $\checkmark$  
- Updates information based on actions $\checkmark$  
    - Modify borrower details  
    - Change a book's availability when borrowed or returned  
- Provides warning messages $\checkmark$  

## Challenges - Problems Encountered

1. **Different Methods of Working**  
    - Each team member had a different coding style.  
    - As a result, we had to refactor the code to maintain consistency.  

2. **Working in a *Large* Codebase**  
    - It was challenging to keep track of related functions.  

3. **Updating *Data* in the Text File**  
    - Initially, we were unaware of the correct steps required to update data in a text file:
        1. Read the existing file.  
        2. Open a temporary file.  
        3. Modify the necessary *data*.  
        4. Write all data (*including the modified one*) to the temporary file.  
        5. Delete the original text file and rename the *new* temporary file.  
    - This approach is an **Operating System constraint**, not a programming language constraint.  

## Future Work  

- Implement a database for data storage and use Python as the front-end, connecting via a [Database API](https://en.wikipedia.org/wiki/API).  
- Send email notifications to borrowers **5 days before** their due date as a reminder to return books.  
- Develop a Graphical User Interface using technologies/frameworks such as:  
    - [Tkinter](https://docs.python.org/3/library/tkinter.html)  
    - [PyQt](https://doc.qt.io/qtforpython-6/)  
- Refactor the `update_borrower()` function  
    - Allow updates to specific details

---

# References

## Skip Header Line

Stack Overflow user (2011) ‘Read file from line 2 or skip header row’, Stack Overflow, 4 January. Available at: https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row.

Initially for my Markdown ToDo Project, [Doits](https://github.com/Sunhaloo/doits), I use the `.seek(1)` function. But it did **not** work in this case. Therefore, we used:

```python
# skips the first line in a text file
next(file_name_variable)
```

## Read Last Line in a File

Stack Overflow user (2017) ‘How to read the last line of a file in Python’, Stack Overflow, 15 September. Available at: https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python.

Here is the code that we used to read the last line in a file:

```python
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
```

In this case, the variable `line` will still contain the **last** line in the text file.

## Modify/Update a Specific File

Stack Overflow user (2008) ‘How to modify a text file’, Stack Overflow, 15 September. Available at: https://stackoverflow.com/questions/125703/how-to-modify-a-text-file.

>[!TIP] Lack of Knowledge  
>Initially, we did **not** realise that updating a specific value in a text file cannot be done "*inline*".  
>To modify data in a text file, the following steps must be performed:  
>  
>1. Open the existing file in read mode.  
>2. Create a temporary file.  
>3. Modify the required data.  
>4. Write all the updated data to the temporary file.  
>5. Delete the original text file.  
>6. Rename the temporary text file to match the original filename.  
>  
>This behaviour is due to how operating systems handle file modifications. No programming language can directly edit a file *in place* without rewriting it.  
>  
>From what we understand, when a file is opened, the OS loads its contents into RAM. When the user presses the **Save** button, the original file on the secondary storage is deleted, and the updated version from RAM is written back to storage.  

## Date Format

Sunhaloo (n.d.) DOITS main.py, GitHub. Available at: https://github.com/Sunhaloo/DOITS/blob/main/main.py.

```python
current_date = datetime.now().strftime("%d-%m-%Y")
datetime_header = datetime.now().strftime("%H:%M - %d/%m/%Y")
```

>Use `stftime()` from code to format the date in the required time.

## For Report Inspiration

Sunhaloo (n.d.) PyYu README, GitHub. Available at: https://github.com/Sunhaloo/PyYu/blob/main/README.md.

Sunhaloo (n.d.) Doits learning.md, GitHub. Available at: https://github.com/Sunhaloo/doits/blob/main/learning.md.

# Appendix

## Full Code

### Main File

```python
# import functions file
import functions


# our main fucntion
def main():
    # call function to allow staff to login into system
    functions.login_screen()
    # call function to allow program to display main meny screen
    functions.display_main_options()


# source the main function
if __name__ == "__main__":
    main()
```

### Functions File

```python
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
```

### Borrower File

```python
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
```

### Book File

```python
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
```

---

# Socials

- **Instagram**: https://www.instagram.com/s.sunhaloo
- **YouTube**: https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg
- **GitHub**: https://www.github.com/Sunhaloo

---

S.Sunhaloo
Thank You!