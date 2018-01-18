#!/usr/bin/env python
"""
    File name: XETUdata.py
    Author: Jorge Quintero
    Date created: 10/30/2017
    Date last modified: 11/07/2017
    Python version: 3.6
"""
from time import sleep
from calendar import month_name
from datetime import datetime
from datetime import timedelta


def menu():
    """Displays to the user the variety of commands he can use."""
    print("\nWelcome, please choose the action you want to perform:\n\n\
          \t1.- Add data of the productions.\n\
          \t2.- Generate a resume of the productions.\n\
          \t3.- Remove the data of the file.\n\
          \t4.- Check specific data of a certain day.\n\
          \t9.- Exit.\n")


def checker(msg):
    """Ask the user for an input and checks it.

    Keyword arguments:
        msg (str): Is the instruction you give the user.

    Returns:
        int: A correct number of user input.
    """
    while True:
        try:
            u_in = int(input(msg))
        except ValueError:
            print("Sorry, invalid input, please try again.")
        else:
            break
    return u_in


def data_productions():
    """User manually writes data to a file.

    Description:
        We ask the user for the period which the data corresponds to, next we request
        the info of every line and turn, in each day of the week.

    Returns:
        It returns the two days of the user input.
    """
    pro_info = info_ask()
    # Converts the number of the number to it's name.
    month_start = str(month_name[int(pro_info[2])])
    month_end = str(month_name[int(pro_info[3])])
    # Here we open the file and the first line we created above.
    with open('productData.txt', 'a') as file:
        file.write("Production line report from %s-%s of %s-%s, year %s.\n"
                   % (str(pro_info[0]).zfill(2), str(pro_info[1]).zfill(2),
                      month_start, month_end, pro_info[4]))
    # This loops thought all days, all lines and all turns and adds the data each time.
    start_date = datetime(pro_info[4], pro_info[2], pro_info[0])
    for d in range(1, 8):
        print("\nEnter the data of day " + str(d))
        for l in range(1, 6):
            for t in range(1, 4):
                print("\nWrite the following data of the line %s and turn %s"
                      % (str(l), str(t)))
                # The abs() method is just in case the user writes negatives.
                products = abs(checker("Number of products: "))
                stopped = abs(checker("Number of times it stopped: "))
                togo_data = "Line %s,Turn %s,%s-%s-%s,%s,%s\n"\
                            % (str(l), str(t), start_date.day, start_date.month,
                               start_date.year, str(products), str(stopped))
                with open('productData.txt', 'a') as file:
                    file.write(togo_data)
        # This line changes the number of the day.
        start_date = start_date + timedelta(days=1)


def info_ask():
    """Asks and validates the user inputs for the product data file generation.

    :return: A list containing the range of the week, it's days, months, and year.
    """
    while True:
        print("\nYou must enter following data of the week:")
        # The absolute is in case the user puts a negative number.
        start_day = abs(checker("\nEnter the start day: "))
        start_month = abs(checker("Enter the number of month of that day: "))
        end_day = abs(checker("Enter the end day: "))
        end_month = abs(checker("Enter the number of month of that day: "))
        info_year = abs(checker("Enter the year: "))
        if 0 < start_month <= 12 and 0 < end_month <= 12:
            try:
                final_date = datetime(info_year, start_month, start_day) - datetime(info_year, end_month, end_day)
            except ValueError:
                print("\nSorry, that month doesn't have that many days.")
                sleep(2)
                continue
            else:
                if final_date.days < 0 and abs(final_date.days) == 6 and len(str(info_year)) == 4:
                    return [start_day, end_day, start_month, end_month, info_year]
        print("Please, enter valid info.")
        sleep(2)


def generate_resume():
    """Writes a resume of the productData.txt in dataResume.txt file.

    Description:
        Calls two other functions in order to extract the important information
        of productData.txt, then we write all the information extracted into a
        nice formatted view for the user.

    Returns:
        It doesn't return anything, it writes on a file.
    """
    # We take the info of the first line of the file product data.
    with open('productData.txt', 'r') as file:
        checking = file.readline()
        week_days = [checking[28:30], checking[31:33]]
    # Assigns to each line it's corresponding dictionary.
    l1, l2, l3, l4, l5 = (dict_gen(1), dict_gen(2), dict_gen(3), dict_gen(4), dict_gen(5))
    production_lines = [l1, l2, l3, l4, l5]
    # This will count the days.
    counter = 0
    with open('dataResume.txt', 'a') as resume:
        testing = 'Week from %s to %s.\n\n' % (week_days[0], week_days[1])
        resume.write(testing)
        for line in production_lines:
            counter += 1
            for turn in range(1, 4):
                # The next two lines coverts all the strings in the lists to ints.
                products = [int(i) for i in line[turn][0]]
                stopped_times = [int(i) for i in line[turn][1]]
                resume.write('Production line number: ' + str(counter) + '\n')
                resume.write('Turn: ' + str(turn) + '\n')
                resume.write('Total produced products of the week: %s\n' % (str(sum(products))))
                resume.write('Times the line stopped: %s\n' % (str(sum(stopped_times))))
                resume.write('Day in which the machine stopped most: %s\n\n' % (most_stops(line, turn)))


def most_stops(line, turn):
    """Analyze the data to determine in which day the production line stopped more.

    Keyword arguments:
        line (dict): The dictionary which contains all the products and times the production
                        line stopped.
        turn (int): The turn wanted to analyze.

    Returns:
        The date of the most stops in the desired turn.
    """
    vartop = [int(i) for i in line[turn][1]]
    vartop = max(vartop)
    with open('productData.txt', 'r') as data:
        data.readline()
        for i in data:
            i = i.strip('\n')
            i = i.split(',')
            if int(i[4]) == vartop and i[1] == 'Turn ' + str(turn):
                return i[2]


def dict_gen(line):
    """Generates a dictionary.

    Keyword arguments:
        line (int): Is the line the function will take as reference for search.
    Returns:
        A dictionary that contains 3 keys, each of them represents the a turn of
        the production line, with two list, one containing all the products of the
        turn, and the other all the times it stopped.
    """
    # Creates a dictionary for each line and that represents the 3 turns of each line.
    x = dict([(i, [[], []]) for i in range(1, 4)])
    for turn in range(1, 4):
        with open('productData.txt', 'r') as data:
            # Reading the first line which data isn't needed.
            data.readline()
            for file_line in data:
                working = file_line.strip('\n')
                file_line = working.split(',')
                if file_line[0] == ("Line " + str(line)) and file_line[1] == ("Turn " + str(turn)):
                    x[turn][0].append(file_line[3])
                    x[turn][1].append(file_line[4])
    return x


def par_consult(line, turn, day):
    """Search the products and stops of a certain line and turn in a day.

    :param line: Is the line the user wants to check.
    :param turn: Is the turn the user wants to check.
    :param day: Is the specific day of the data.
    :return: The products and stops depending on the parameters of above.
    """
    with open('productData.txt', 'r') as file:
        file.readline()
        for data in file:
            data = data.strip('\n')
            data = data.split(',')
            desired_date = data[2].split('-')
            if data[0] == "Line " + str(line) and data[1] == "Turn " + str(turn) and desired_date[0] == str(day):
                return [data[3], data[4]]


# Checks if the predetermined files exists and can be used, if not, creates them.
for name in ['productData', 'dataResume']:
    try:
        test = open(name + '.txt', 'a')
    except IOError:
        print('Something went wrong. Contact the administrator.')
        exit()
    else:
        test.close()
# Loop of the program
while True:
    menu()
    sleep(2)
    action = checker('Enter the action to perform based on the menu: ')
    if action == 1:
        with open('productData.txt', 'r') as testing:
            first_line = testing.readline()
        if not first_line:
            data_productions()
            go_on = input("\nDo you want to create the resume? (Yes or no): ")
            go_on = go_on.lower()
            if go_on == 'yes' or go_on == 'ye' or go_on == 'y':
                generate_resume()
            else:
                print("The resume will not be generated.")
                sleep(1)
        else:
            print("The product data file has already info, please clear it.")
    elif action == 2:
        with open('productData.txt', 'r') as testing:
            first_line = testing.readline()
        with open('dataResume.txt', 'r') as testing2:
            second_line = testing2.readline()
        if first_line:
            if not second_line:
                generate_resume()
                print("The resume has been generated and stored in 'dataResume.txt'")
            else:
                print("The resume data file has already info, please clear it.")
                sleep(1)
        else:
            print("The product data file doesn't have info.")
            sleep(1)
    elif action == 3:
        while True:
            print("\nSelect one of the following options:\n\
                      \t1.- Cleanup both files.\n\
                      \t2.- Cleanup productData.txt.\n\
                      \t3.- Cleanup dataResume.txt.\n")
            user_choose = checker("Enter the option you want: ")
            if user_choose == 1:
                open('productData.txt', 'w').close()
                open('dataResume.txt', 'w').close()
                break
            elif user_choose == 2:
                open('productData.txt', 'w').close()
                break
            elif user_choose == 3:
                open('dataResume.txt', 'w').close()
                break
            else:
                print("\nYou must choose something on the list!\n")
                sleep(2)
        print('Everything in the file will be deleted in 2 seconds.')
        sleep(2)
        print("Deleted, press 1 to reenter the info of the week or next week.")
        sleep(1)
    elif action == 4:
        with open('productData.txt', 'r') as testing:
            first_line = testing.readline()
        if first_line:
            while True:
                while True:
                    day = checker("\nSpecify the day of the info (Example: 29): ")
                    # The next lines just prevents errors at the search of the info.
                    line = checker("Enter the production line: ")
                    if 1 <= line <= 5:
                        turn = checker("Enter the turn you want to check: ")
                        if 1 <= turn <= 3:
                            break
                    print("Please, reenter the info.")
                info = par_consult(line, turn, day)
                if not info:
                    print("\nEnter a correct day.\n")
                    sleep(2)
                    continue
                print(("\nIn the day %s of the month, the line %s in the turn %s had:\n" +
                       "\tProducts: %s\n\tStops: %s") % (day, line, turn, info[0], info[1]))
                input("\nPress enter to continue.")
                break
        else:
            print("The product data file has no info.")
    elif action == 9:
        break
    else:
        print("You need to choose a number of the menu.\n")
        sleep(1)
    sleep(1)
    print("\n" * 100)


print('%sThank you for using the program, you will now exit.\nBye bye.' % ("\n" * 100))
exit()
