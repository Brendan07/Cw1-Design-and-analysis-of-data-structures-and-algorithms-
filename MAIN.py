"""
Brendan Baker DaTsa CW Part 1 Animal Sanctuary
"""
import csv
from Pets import Pets  # Importing the Classes from their file
from Wild import Wild
from Treatment import Treatments

pet_data = []  # Creating a list to store the pet data
wild_data = []
treatment_data = []
abuse_list = []
abandoned_list = []

file_pet = "DADSA 2019-20 CWK A DATA PETS(1) (1).csv"  # Assigning files to a easier to read variable
file_wild = "DADSA 2019-20 CWK A WILD ANIMALS (1).csv"
file_treatment = "DADSA 2019-20 CWK A TREATMENT (1).csv"


# Menu function where the user can select which option they would select or which submenu they would like
def main_menu():
    menu = ["1:View All Data", "2:Search by ID", "3:Create new entry ", "4:Edit Data", "5:Other ", "0: Exit"]

    print(menu)
    c = int(input("Please give an option:"))
    if c == 1:
        print_all_data()
        main_menu()

    elif c == 2:
        search_id_function()

    elif c == 3:
        new_entry()

    elif c == 4:

        print("Which sort of data would you like to edit:")
        print("1:Pet data")
        print("2:Wild animal data")
        print("3:Treatment data")
        c = int(input("please enter an option:"))

        if c == 1:
            edit_menu_pet()
        elif c == 2:
            edit_menu_wild()
        elif c == 3:
            edit_menu_treatment()

    elif c == 5:
        submenu()

    elif c == 0:
        exit(" Thank you, You have now exited the program")


# Submenu function which is a submenu of main menu Prints different options to the user
def submenu():
    menu = ["1: List of animals ready for adoption", "2:List of animal abusers or abandoners",
            "3:Return to main menu", "4:List of animals ready to return to owner", "0: Exit"]

    print(menu)
    c = int(input("Please give an option: "))
    if c == 1:
        adoption_menu()

    elif c == 2:
        abandoned_and_abused()

    elif c == 3:
        adoption_menu()

    elif c == 4:
        ready_for_return_pet()
        ready_for_return_wild()

    elif c == 0:
        exit(" Thank you, You have now exited the program")


# ADOPTION SUBMENU FOR TASK 2E and 2F Prints which list you ask the user for which animal they want to view for adoption
def adoption_menu():
    menu = ["1:Cat", "2:dog ", "0:Return to submenu"]
    print(menu)
    c = int(input("Please enter an option"))

    if c == 1:
        ready_adoption_pet('cat')
        adoption_menu()

    elif c == 2:
        ready_adoption_pet("dog")
        adoption_menu()

    elif c == 0:
        submenu()

    else:
        print("Error Please enter following the format, For example: 'Dog' or 'Cat'./n ")
        adoption_menu()


# Menu to allow the user to select whether to view a list of abused or abandoned animals
def abandoned_and_abused():
    menu = ["1:List of abusers", "2:List of abandoners", "0:Return to submenu"]
    print(menu)
    c = int(input("Please enter an option"))

    if c == 1:

        col_reader_abuse()
    elif c == 2:

        col_reader_abandoner()

    elif c == 0:
        submenu()
    else:
        print("Error please enter a valid option")
        abandoned_and_abused()


# Function to allow the user which type of new entry they would like
def new_entry():
    menu = ["1:New pet entry", "2:New wild animal entry", "3:New treatment entry", "0:return to menu."]

    print(menu)
    c = int(input("Please give an option: "))
    if c == 1:
        add_pet()

    elif c == 2:
        add_wild()

    elif c == 3:
        add_treatment()

    elif c == 0:
        main_menu()


# TASK 2A Function that takes the users input and stores as list then appends to tha
def add_pet():
    pet_id = input("Enter ID: ")
    pet_input = input("Enter type of pet: ")
    pet_input1 = input("Enter Breed: ")
    pet_input2 = input("Is your pet Vaccinated: ")
    pet_input3 = input("Is your pet Neutered: ")
    pet_input4 = input("What's your pets microchip number: ")
    pet_input5 = input("Reason for admission: ")
    pet_input6 = input("Date of Arrival: ")
    pet_input7 = input("Enter departure date: ")
    pet_input8 = input("Please enter destination: ")
    pet_input9 = input("Please enter destination address: ")

    row = [pet_id, pet_input, pet_input1, pet_input2, pet_input3, pet_input4, pet_input5, pet_input6, pet_input7,
           pet_input8, pet_input9]

    with open(file_pet, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    csvfile.close()
    print("Thank you the entry has been added.")
    main_menu()


def add_wild():
    w_id_input = input("Enter ID: ")
    wild_input1 = input("Enter type of Animal: ")
    wild_input2 = input("Is your pet Vaccinated: ")
    wild_input3 = input("Reason for admission: ")
    wild_input4 = input("Date of Arrival: ")
    wild_input5 = input("Enter departure date: ")
    wild_input6 = input("Please enter destination: ")
    wild_input7 = input("Please enter destination address: ")
    # The variables are then stored into a list in the order they will be placed in a row in the csv file With the
    row = [w_id_input, wild_input1, wild_input2, wild_input3, wild_input4, wild_input5, wild_input6, wild_input7]

    with open(file_wild, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    csvfile.close()
    print("Thank you the entry has been added.")
    main_menu()


def add_treatment():
    t_id_input = input("Enter ID: ")
    treatment_input = input("Enter surgery type: ")
    while True:
        treatment_input1 = input("Enter surgery date: ")
        if treatment_input1 != "":
            break
        else:
            print("Surgery must have a date")

    treatment_input2 = input("Enter Medication type: ")
    treatment_input3 = input("Enter medication start date: ")
    treatment_input4 = input("Enter medication end date: ")
    treatment_input5 = input(str("Responsible for abuse:")).title()
    treatment_input6 = input(str("Responsible for abandoning:")).title()

    row = [t_id_input, treatment_input, treatment_input1, treatment_input2, treatment_input3, treatment_input4,
           treatment_input5, treatment_input6]

    with open(file_treatment, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    csvfile.close()
    print("Thank you the entry has been added.")
    main_menu()


# Function that prints all the data from the file
def print_all_data():
    for row in pet_data:
        print(row)
    for row in wild_data:
        print(row)
    for row in treatment_data:
        print(row)


# This function loads the pet data in the program, it reads it using the reader method  'r'
def load_pet_data():
    with open(file_pet, 'r', newline='') as csvfile:  # If csvfile is a file object, it should be opened with newline=''
        reader = list(csv.reader(csvfile))

        for row in reader:  # each row ( more like column) that is red to a index to be store in the class Pets
            pet_data.append(Pets(row[0], row[1], row[2], row[3], row[4], row[5],
                                 row[6], row[7], row[8], row[9], row[10]))


# This function loads the Wild data in the program, it reads it using the reader method  'r'
def load_wild_data():
    with open(file_wild, 'r',
              newline='') as csvfile:  # If csvfile is a file object, it should be opened with newline=''
        reader = list(csv.reader(csvfile))

        for row in reader:  # each row ( more like column) that is red to a index to be store in the class Wild
            wild_data.append(Wild(row[0], row[1], row[2], row[3], row[4], row[5],
                                  row[6], row[7]))


# This function loads the treatment data in the program, it reads it using the reader method  'r'
def load_treatment_data():
    with open(file_treatment) as csvfile:  # If csvfile is a file object, it should be opened with newline=''

        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:  # each row ( more like column) that is red to a index to be store in the class treatment
            treatment_data.append(Treatments(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


# Task 2B Find the full data for an animal by using the animals sanctuary identification
def search_id_function():
    menu = ["1:Search pet", "2:Search wild", "0: Return to main menu"]
    print(menu)
    c = int(input("Please enter an option:"))

    if c == 1:
        pet_idd = input("Enter Pet ID:").upper()  # Makes the ID entered by the user all the characters upper case
        read_id(pet_idd)
        main_menu()

    elif c == 2:
        wild_idd = input("Enter Wild ID:").upper()
        read_id_wild(wild_idd)
        main_menu()

    elif c == 3:
        main_menu()

    else:
        print("Please enter a valid option:")
        main_menu()


# TASK 2A OUTPUT THEs the info of pet and the treatment
def read_id(pet_idd):
    for pet in pet_data:
        if pet.pet_id == pet_idd:
            print('Pet Information')
            print(pet)

    for treatment in treatment_data:  # Now checking to see if this pet has any treatments
        if treatment.treat_id == pet_idd:
            # if the t reatment id matches the parameter pet_idd in the treatment file
            print('Treatment Information')
            print(treatment)  # It will print a row of treatment also under a new bold heading


# TASK B FUNCTIONS takes the ID and matches the ID from the attribute in the Class
def read_id_wild(wild_idd):
    for wild in wild_data:
        if wild.wild_id == wild_idd:
            print("Animal Info")
            print(wild)
    # Also checks too see if the ID has any corresponding treatment to print
    for treatment in treatment_data:
        if treatment.treat_id == wild_idd:  # if the treatment id matches the parameter pet_idd in the treatment file

            print('Treatment Information')
            print(treatment)


# FUNCTION 2F produces a list of dog or cars that are ready for adoption (neutered, vaccinated and micro chipped)
def ready_adoption_pet(an_type):  # user_input passed in as parameter
    for pet in pet_data:
        if an_type.title() == pet.pet_type and pet.vaccinated != "" and pet.neutered != "" and pet.micro_chip != "" \
                and pet.admission_reason != "Lost" and pet.admission_reason != "Car Accident" \
                and pet.destination == "":
            print(pet)


# TASK2C FUNCTION checks the attribute, if not empty append to new list check duplicates:sort
def col_reader_abuse():
    for treatment in treatment_data:
        if treatment.responsible_abuse != "":
            abuse_list.append(treatment.responsible_abuse)
            temp = duplicateGlitch(abuse_list)
            insertion_sort(temp)
    for i in temp:
        print(i)


# TASK 2D FUNCTION Checks the attribute, if not empty append to new list check for duplicates then sort
def col_reader_abandoner():
    for treatment in treatment_data:
        if treatment.responsible_abandoned != "":
            abandoned_list.append(treatment.responsible_abandoned)
            temp = duplicateGlitch(abandoned_list)
            insertion_sort(temp)
    for i in temp:
        print(i)


# Sort function for 2C, 2D AND 2G insertion sort with a variable that stops stack overflow
def insertion_sort(seq):
    seqlength = len(seq)  # Variable set to avoid stack overflow
    for i in range(1, seqlength):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


# Function remove duplicate items from list
def duplicateGlitch(items):
    revised_list = []
    for item in items:
        if item not in revised_list:
            revised_list.append(item)

    return revised_list


# 2G Function that prints the pet animals ready for return in alphabetical order
def ready_for_return_pet():
    temp = []
    print('\nReady to return Pets')
    for return_pet in pet_data:
        if return_pet.micro_chip != "" and (return_pet.admission_reason == "Car Accident" or
                                            return_pet.admission_reason == "Lost") and return_pet.departure == "" \
                and return_pet.destination == "":
            temp.append(return_pet)
    insertion_sort(temp)
    for return_pet in temp:
        print(return_pet)


# 2G Function that prints the wild animals ready for return in alphabetical order
def ready_for_return_wild():
    temp2 = []
    print('\nReady to return Wild animals')
    for return_wild in wild_data:
        if "Abandoned" in return_wild.admission_reason and return_wild.departure == "":
            temp2.append(return_wild)
    insertion_sort(temp2)
    for return_wild in temp2:
        print(return_wild)


# Function returns the pet to the parameter or does not if not found
def return_pet_id(pet_to_return):
    found = False
    for pet in pet_data:
        if pet.pet_id == pet_to_return:
            found = True
            return pet
    if not found:
        return "not found"


# Function returns the wild animal to the parameter or does not if not found
def return_wild_id(wild_to_return):
    found = False
    for wild in wild_data:
        if wild.wild_id == wild_to_return:
            found = True
            return wild
    if not found:
        return "not found"


# Function returns the treatment to the parameter or does not if not found
def return_treatment_id(treatment_to_return):
    found = False
    pet_treatments = []
    for treatment in treatment_data:
        if treatment.treat_id == treatment_to_return:
            found = True
            pet_treatments.append(treatment)
    if len(pet_treatments) > 1:
        print("Choose Selection")
        for i in range(1, len(pet_treatments) + 1):
            print(i, pet_treatments[i - 1])
        c = int(input("Select Option:"))
        c = c - 1
        print("Treatment Information")
        return pet_treatments[c]
    else:
        print("Treatment Information")
        return treatment


# TASK 3 ALL PARTS BELOW
# TASK 3 Menu which takes the ID and assigns it to a attribute against the class Pets
def edit_menu_pet():
    pet_edit = input("Enter Pet ID:").title()  # return
    pet = return_pet_id(pet_edit)

    if (pet == "not found"):
        print("Pet id not in data")
        edit_menu_pet()

    else:

        print(pet)
        print()

        print("Please enter which option you wish to edit: ")
        print("1:Pet Type")
        print("2:Pet Breed")
        print("3:Pet Vaccination")
        print("4::Neutered Status")
        print("5:Microchip number")
        print("6:Admission Reason")
        print("7:Arrival Date")
        print("8:Departure Date")
        print("9:Destination")
        print("10:Destination Address")

        c = int(input("Please give an option: "))
        print("Please enter the changes you wish to make: ")

        if c == 1:
            pet_type = input().title()  # edit
            pet.pet_type = pet_type
            edit_pet(pet)
            thank_you()

        elif c == 2:
            breed = input().title()
            pet.breed = breed
            edit_pet(pet)
            thank_you()

        elif c == 3:
            vaccinated = input().title()
            pet.vaccinated = vaccinated
            edit_pet(pet)
            thank_you()

        elif c == 4:
            neutered = input().title()
            pet.neutered = neutered
            edit_pet(pet)
            thank_you()

        elif c == 5:
            micro_chip = input().title()
            pet.micro_chip = micro_chip
            edit_pet(pet)
            thank_you()

        elif c == 6:
            admission_reason = input().title()
            pet.admission_reason = admission_reason
            edit_pet(pet)
            thank_you()

        elif c == 7:
            arrival = input().title()
            pet.arrival = arrival
            edit_pet(pet)
            thank_you()

        elif c == 8:
            departure = input().title()
            pet.departure = departure
            edit_pet(pet)
            thank_you()

        elif c == 9:
            destination = input().title()
            pet.destination = destination
            edit_pet(pet)
            thank_you()

        elif c == 10:
            destination_address = input().title()
            pet.destination_address = destination_address
            edit_pet(pet)
            thank_you()


# FUNCTION that prints a message acknowledging the changes have been made then terminates the program
def thank_you():
    print("Thank you changes have been made")
    exit("Bye")


# TASK 3 Menu which takes the ID and assigns it to a attribute against the class Wild
def edit_menu_wild():
    wild_edit = input("Enter ID:").upper()
    wild = return_wild_id(wild_edit)

    if wild == "not found":
        print("Wild id not in data")
        edit_menu_wild()

    else:
        print(wild)
        print()

        print("1:Animal Type")
        print("2:Animal Vaccination")
        print("3:Admission Reason")
        print("4:Arrival Date")
        print("5:Departure Date")
        print("6:Destination")
        print("7:Destination Address")

        c = int(input("Please give an option: "))

        if c == 1:
            wild_type = input().title()  # edit
            wild.wild_type = wild_type
            edit_wild(wild)
            thank_you()

        elif c == 2:
            vaccinated = input().title()
            wild.vaccinated = vaccinated
            edit_wild(wild)
            thank_you()

        elif c == 3:
            admission_reason = input().title()
            wild.admission_reason = admission_reason
            edit_wild(wild)
            thank_you()

        elif c == 4:
            arrival = input().title()
            wild.arrival = arrival
            edit_wild(wild)
            thank_you()

        elif c == 5:
            departure = input().title()
            wild.departure = departure
            edit_wild(wild)
            thank_you()

        elif c == 6:
            destination = input().title()
            wild.destination = destination
            edit_wild(wild)
            thank_you()

        elif c == 7:
            destination_address = input().title()
            wild.destination_address = destination_address
            edit_wild(wild)


# TASK 3 Menu which takes the ID and assigns it to a attribute against the class Treatment
def edit_menu_treatment():
    treatment_edit = input("Enter ID:").upper()
    treatment = return_treatment_id(treatment_edit)
    if (treatment == "not found"):
        print("treatment id not in data")
        edit_menu_treatment()
    else:

        print(treatment)
        print()
        print("1:Edit or Enter surgery type")
        print("2:Edit or enter medication")
        print("3:Enter or edit medication start date")
        print("4:Enter or edit medication end date")
        print("5:Edit responsible for abuse")
        print("6:Edit responsible for abandonment")
        print()

        print("Please enter an option: ")
        c = int(input())
        print("Please enter the changes you wish to make")

        if c == 1:
            treat_surgery = input().title()
            treatment.treat_surgery = treat_surgery
            edit_treatment(treatment)

        elif c == 2:
            medication = input().title()
            treatment.medication = medication
            edit_treatment(treatment)

        elif c == 3:
            med_start = input().title()
            treatment.med_start = med_start
            edit_treatment(treatment)

        elif c == 4:
            med_end = input().title()
            treatment.med_end = med_end
            edit_treatment(treatment)

        elif c == 5:
            responsible_abuse = input().title()
            treatment.responsible_abuse = responsible_abuse
            edit_treatment(treatment)

        elif c == 6:
            responsible_abandoned = input().title()
            treatment.responsible_abandoned = responsible_abandoned
            edit_treatment(treatment)


# TASK 3 FUNCTION that writes over the exsisting file with the headings and new data
def edit_pet(pet_id_to_edit):
    c = csv.reader(open(file_pet))
    lines = list(c)

    for row in lines:
        if row[0] == pet_id_to_edit.pet_id:
            row[1] = pet_id_to_edit.pet_type
            row[2] = pet_id_to_edit.breed
            row[3] = pet_id_to_edit.vaccinated
            row[4] = pet_id_to_edit.neutered
            row[5] = pet_id_to_edit.micro_chip
            row[6] = pet_id_to_edit.admission_reason
            row[7] = pet_id_to_edit.arrival
            row[8] = pet_id_to_edit.departure
            row[9] = pet_id_to_edit.destination
            row[10] = pet_id_to_edit.destination_address

    writer = csv.writer(open(file_pet, 'w', newline=''))
    writer.writerows(lines)
    print(pet_id_to_edit)


# TASK 3 FUNCTION that writes over the exsisting file with the headings and new data
def edit_wild(wild_id_to_edit):
    c = csv.reader(open(file_wild))
    lines = list(c)

    for row in lines:
        if row[0] == wild_id_to_edit.wild_id:
            row[1] = wild_id_to_edit.wild_type
            row[2] = wild_id_to_edit.vaccinated
            row[3] = wild_id_to_edit.admission_reason
            row[4] = wild_id_to_edit.arrival
            row[5] = wild_id_to_edit.departure
            row[6] = wild_id_to_edit.destination
            row[7] = wild_id_to_edit.destination_address

    writer = csv.writer(open(file_wild, 'w', newline=''))
    writer.writerows(lines)
    print(wild_id_to_edit)


# TASK 3 FUNCTION that writes over the exsisting file with the headings and new data
def edit_treatment(treatment_to_edit):
    c = csv.reader(open(file_treatment))
    lines = list(c)

    for row in lines:
        if row[0] == treatment_to_edit.treat_id and row[2] == treatment_to_edit.surgery_date:
            row[1] = treatment_to_edit.treat_surgery
            row[2] = treatment_to_edit.surgery_date
            row[3] = treatment_to_edit.medication
            row[4] = treatment_to_edit.med_start
            row[5] = treatment_to_edit.med_end
            row[6] = treatment_to_edit.responsible_abuse
            row[7] = treatment_to_edit.responsible_abandoned

    writer = csv.writer(open(file_treatment, 'w', newline=''))
    writer.writerows(lines)
    print(treatment_to_edit)


load_pet_data()
load_treatment_data()
load_wild_data()
main_menu()
