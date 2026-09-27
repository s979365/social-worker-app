# Code your program directly here or include a link to your work here
# Aiwin and Nashayla's code yayyayayya
# Aiwin will build the lists + dictionary and the functions/starting the functions and names
# Nashayla will build within the functions for the CREATE/READ/UPDATE/DELETE
# Add case numbers
#Case workers can only have once case in each category so there isnt too much of a workload
#poverty aid is an example space to see if everything runs smoothly

cases = [{"case number": 1, "complaint": "domestic violence", "case name": "", "service offered": "safe housing", "status report": "", "notes": []},
    {"case number": 2, "complaint": "self harm", "case name": "", "service offered": "crisis lifeline", "status report": "", "notes": []},
    {"case number": 3, "complaint": "orphaned child", "case name": "", "service offered": "foster care", "status report": "", "notes": []},
    {"case number": 4, "complaint": "drug abuse", "case name": "", "service offered": "group counseling", "status report": "", "notes": []},
    {"case number": 5, "complaint": "child neglect", "case name": "", "service offered": "parenting classes", "status report": "", "notes": []},
    {"case number": 6, "complaint": "geriatric care", "case name": "", "service offered": "assisted living", "status report": "", "notes": []},
    {"case number": 7, "complaint": "child murderers", "case name": "", "service offered": "protective custody", "status report": "", "notes": []},
    {"case number": 8, "complaint": "homelessness", "case name": "", "service offered": "transitional shelters", "status report": "", "notes": []},
    {"case number": 9, "complaint": "ex:Poverty aid", "case name": "", "service offered": "program referels", "status report": "", "notes": []}]

# Aiwin you must absolutely not delete this
def select_case(case_number):
        return cases[case_number - 1]



#new_case attributes a case number that either corresponds to domestic violence like 1.1, 1.2, 1.3 
# It was supposed to do that but since each case only gets one name under its category this does not matter anymore
def new_case(case):
    for number, case_type in enumerate(case, start=1):
        print(f"{case_type['case number']}. {case_type['complaint']}")
        #Keep int there so we can assign numerical values for the case numbers and subtract or add to list 
    case_number = int(input("Which case option will you be adding to? (Type the number) "))
    name_case = input("What is the name of this new case? ")

    selected_case = select_case(case_number)
    selected_case["case name"] = name_case
    print(f"Your new case {name_case} has been added under the {selected_case['complaint']} class.")

# #status_report updates status of date from one of the case options to a different one or to "none"
def status_report():
    for number, category in enumerate(cases, start=1):
        case_name = category["case name"] or category["complaint"]
        print(f"{category['case number']}. {case_name}")
    try:
        case_number = int(input("\n Which case would you like to update? "))
        category = select_case(case_number)
    except ValueError:
        print("Please enter a valid case number.")
        return

    report_date = input("Date: ")
    category["status report"] = report_date
    case_name = category["case name"] or category["complaint"]
    print(f"{case_name} - {category['status report']}")
    print(f"The latest update on the the case file named {case_name} was {report_date}")
 #calc_solution prints one of the keys in the dictionary along with the notes updated to that portion 
 # I don't think I did this correctly
def calc_solution():
    for case in cases:
        name_case = case["case name"] or case["complaint"]
        print(f"{case['case number']}. {name}")
    case_number = int(input("What case would you like the full overview for? "))
    selected_case = select_case(case_number)
    print(f"Case Number: {selected_case['case number']}")
    print(f"Complaint: {selected_case['complaint']}")
    print(f"Case Name: {selected_case['case name'] or selected_case['complaint']}")
    print(f"Service Offered: {selected_case['service offered']}")
    print(f"Status Report: {selected_case['status report']}")
    print(f"Notes: {selected_case['notes']}")
#Nashayla's addition to change multiple things if needed
#might break
def initial_choices():
    while True:
        print("Choose one using its number:\n 1: Add a case\n 2: Case status\n 3: Add to notes\n 4: Review your cases notes\n 5: Case overview\n 6: Clear case name and information\n 7: Exit")
        menu_choice = input("Your choice: ")

        if menu_choice == "1":
            new_case(cases)

        elif menu_choice == '2':
            status_report()

        elif menu_choice == '3':
            for case in cases:
                name_case = case["case name"] or case["complaint"]
                print(f"{case['case number']}. {name}")

            case_number = int(input("Which case are you adding notes to? "))
            selected_case = select_case(case_number)
            note = input("Enter your note: ")
            selected_case["notes"].append(note)
            print(cases)

        elif menu_choice == '4':
            for case in cases:
                name = case["case name"] or case["complaint"]
                print(f"{case['case number']}. {name}")

            case_number = int(input("Which case notes do you want to look at "))
            selected_case = select_case(case_number)
            if selected_case["notes"]:
                for note in selected_case["notes"]:
                    print(note)
            else:
                print("This case has no notes yet.")

        elif menu_choice == "5":
            calc_solution()

        elif menu_choice == "6":
            for case in cases:
                print(f"{case['case number']}. {case['case name'] or case['complaint']}")
            case_number = int(input("Which case would you like to clear? "))
            case = select_case(case_number)
            case["case name"], case["status report"], case["notes"] = "", "", []
            print("Case information has been resolved. You will no longer be able to access the digital version of this case.")
       
        elif menu_choice == "7":
            print("Exited")
           
            break
        else:
            print("Please choose from the options provided")


initial_choices()