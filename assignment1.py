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
    # insert code here to clean the file as per question 1
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
    """
    f refers to the student_names.txt file created in clean_up()
    id_list is the list return with the id's created from the name / surname of each student
    :return: id_list
    """
    f = "student_names.txt"
    id_list = []
    #insert code here to create the id's as per question 2
    with open(f, 'r') as names:
        for name in names:
            split_name = name.split(" ")
            initials = [word[0].lower() for word in split_name]
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
    :return: illegal_password
    """
    illegal_password = []
    #insert code here to validate all the conditions of the password as per question 3
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTHER_ACCEPTED_CHARS = "0123456789_"
    invalid_chars = False
    has_upper = False
    has_lower = False
    has_leading_digit = password[0].isdigit()

    for char in password:
        if char not in LOWER and char not in UPPER and char not in OTHER_ACCEPTED_CHARS:
            invalid_chars = True
        if char in LOWER:
            has_lower = True
        if char in UPPER:
            has_upper = True

    is_mixed_case = has_upper and has_lower

    with open("password.txt", 'r') as f:
        commonly_used = f.read().split("\n")

    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    if len(password) > 12:
        illegal_password.append("TOO LONG")
    if invalid_chars:
        illegal_password.append("WRONG CHARACTERS")
    if not is_mixed_case:
        illegal_password.append("NOT MIXED CASE")
    if has_leading_digit:
        illegal_password.append("LEADING DIGIT")
    if password in commonly_used:
        illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")

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

    for id in id_list:
        identifier = 0
        while True:
            id_string = f'{id}{identifier:04}'
            if id_string in final_list:
                identifier+=1
                continue
            else:
                final_list.append(id_string)
                break

    with open("unique_ids.txt", "w") as f:
        for id_string in final_list:
            f.write(id_string + "\n")

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
        count = 0
        for line in text:
            address =""
            for char in line:
                if char in ACCEPTED_CHARS:
                    address += char
            if address != "": # making sure any empty lines get ignored
                # unpacking it because it's easier and then there's no off-by-one errors, also more readable
                address1, address2, city, postcode = address.split(", ")
                split_addrs.append([address1, postcode])
    return split_addrs


def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    validate_pcode = []
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for address in split_addrs:
        postcode = address[1]
        validate_pcode.append(count)
        if len(postcode) != 6:
            postcode = '$$$$$$'
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if postcode[0] not in UPPER:
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if not (postcode[1].isdigit() and postcode[2].isdigit() and postcode[3].isdigit()):
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        if not (postcode[4] in UPPER and postcode[5] in UPPER):
            validate_pcode.append("False")
        else:
            validate_pcode.append("True")
        count+=1

    return validate_pcode


def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the dictionary, i.e. unique id is key, and the short addr for each student is value
    """
    f = ""
    ids = f.read()
    combo = {}



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



