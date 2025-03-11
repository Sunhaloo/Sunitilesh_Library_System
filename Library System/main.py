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
