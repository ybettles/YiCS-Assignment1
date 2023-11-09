def clean_up():
    """
    f refers to text_to_clean.txt
    sf refers to student_names.txt
    use text to read in the appropriate file
    cleaned is used store the wanted characters
    :return: cleaned
    """
    f = "text_to_clean.txt"
    sf = "student_names.txt"
    cleaned = ""

    # lower case char, upper case char, blank, full stop - valid characters
    ACCEPTED_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .\n"
    with open(f, 'r') as text:
        for line in text:
            for char in line:
                if char in ACCEPTED_CHARACTERS:
                    cleaned += char
    cleaned += "\n"
    with open(sf, 'w') as name_file:
        name_file.write(cleaned)
    return cleaned

def build_id():
    '''
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :return: id_list
    '''
    f = "student_names.txt"
    id_list = []

    # reading in the names
    with open(f, 'r') as names:
        for name in names:
            # splitting them into forename, middle name(s), and surname
            split_name = name.split(" ")
            # getting initials of each name
            initials = [word[0].lower() for word in split_name]
            """if they have three initials, great, thats the id
            if they have two or one initials, fill the empty spaces with an x
            if they have more than three initials, take the first two initials and the final initial.
            all of these should be appended to the list """
            if len(initials) == 3:
                id_list.append(initials[0] + initials[1] + initials[2])
            elif len(initials) == 2:
                id_list.append(initials[0] + "x" + initials[1])
            elif len(initials) == 1:
                id_list.append(initials[0] + "xx")
            else:
                id_list.append(initials[0]+initials[1]+initials[-1])
    print(id_list)
    return id_list


def validate_password(password):
    """
    illegal_password is the list that is built up showing the invalid parts of the password
    Validate the password to verify if it is legal or not as per Question 3
    There is a password.txt file given to you to verify invalid passwords
    :param password: make use of the password found in main(), the test file will also have additional passwords to test
    :return: illegal_password; a list of errors with the password provided. if no errors, list will be empty.
    """
    # initialising variables and constants
    illegal_password = []
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTHER_ACCEPTED_CHARS = "0123456789_"
    invalid_chars = False
    has_upper = False
    has_lower = False
    has_leading_digit = password[0].isdigit()

    # checking that all the characters are valid, and seeing whether the case is mixed or not
    for char in password:
        if char not in LOWER and char not in UPPER and char not in OTHER_ACCEPTED_CHARS:
            invalid_chars = True
        if char in LOWER:
            has_lower = True
        if char in UPPER:
            has_upper = True

    is_mixed_case = has_upper and has_lower

    # opening and reading in the commonly used passwords to make sure they are not present in the password given
    with open("password.txt", 'r') as f:
        commonly_used = f.read().split("\n")

    # length checks
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    if len(password) > 12:
        illegal_password.append("TOO LONG")
    # character validity check
    if invalid_chars:
        illegal_password.append("WRONG CHARACTERS")
    # mixed case check
    if not is_mixed_case:
        illegal_password.append("NOT MIXED CASE")
    # checking to make sure leading character is not a digit
    if has_leading_digit:
        illegal_password.append("LEADING DIGIT")
    # commonly used password check
    if password in commonly_used:
        illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")

    # return list of errors (if none, list will be empty)
    return illegal_password


def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """
    final_list = []
    # iterate over the id list
    for id in id_list:
        # start with 0000, if that already exists (with same initials) then increment and try again, etc. until a unique one exists
        identifier = 0
        while True:
            # create and format the id string
            id_string = f'{id}{identifier:04}'
            if id_string in final_list:
                # increment the identifier number if that unique id already exists
                identifier+=1
                continue
            elif f'{id}{9999}' in final_list:
                # if somehow there are already 10,000 students with the same 3 character id, then no more unique
                # identifiers are available with this formatting, so throw an error
                raise Exception(f"Sorry but all unique identifiers for id: {id} are taken, please contact a system administrator for help.")
            else:
                # if the id string is unique, then append it to the final list
                final_list.append(id_string)
                break

    # opening the unique ids file in write mode to write the newly created ids in
    with open("unique_ids.txt", "w") as f:
        for id_string in final_list:
            f.write(id_string + "\n")

    # opening the create emails file in write mode to write the student emails in
    with open("create_emails.txt", "w") as ef:
        for id_string in final_list:
            ef.write(id_string + "@student.bham.ac.uk\n")

    return final_list


def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = "addresses.txt"
    split_addrs = []
    ACCEPTED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789, "
    with open(f, 'r') as text:
        # need to strip out the newline characters and since we aren't able to use .split, this is the easiest way to do it
        for line in text:
            address = ""
            for char in line:
                if char in ACCEPTED_CHARS:
                    # adding the valid characters back in
                    address += char
            if address != "": # making sure any empty lines get ignored
                # unpacking it because it's easier and then there's no off-by-one errors, also more readable
                address1, address2, city, postcode = address.split(", ")
                # appending only the first line and postcode
                split_addrs.append([address1, postcode])
    return split_addrs


def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    # initialising variables and constant
    validate_pcode = []
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    # iterating through all the addresses
    for address in split_addrs:
        # getting the postcode for the current address
        postcode = address[1]
        # adding the index to the list
        validate_pcode.append(count)

        # validating length
        if len(postcode) != 6:
            # if it's too short replace it with dollar signs and append false to validate_pcode
            postcode = '$$$$$$'
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if postcode[0] not in UPPER:
            # if the first character isn't an uppercase letter, append false
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if not (postcode[1].isdigit() and postcode[2].isdigit() and postcode[3].isdigit()):
            # if the next three characters aren't numbers, append false
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if not (postcode[4] in UPPER and postcode[5] in UPPER):
            # if the fifth and sixth characters are not uppercase letters, append false
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        # increment the index
        count+=1

    return validate_pcode


def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the dictionary, i.e. unique id is key, and the short addr for each student is value
    """
    # initialising the variable that will be needed
    f = "unique_ids.txt"
    combo = {}
    count = 0
    # opening the file in read mode
    with open(f, "r") as id_file:
        # iterating through the lines of the file
        for id in id_file:
            # pairing each id (each line of the file) with each address from the list
            combo[id] = short_addr[count]
            count += 1
    return combo


def main():
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up()
        elif choice == '2':
            id_list = build_id()
        elif choice == '3':
            validate_password("1abcDE%")
        elif choice == '4':
            create_unique(id_list)
        elif choice == '5':
            short_addr = create_short_address()
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()



