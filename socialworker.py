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

#new_case attributes a case number that either corresponds to domestic violence like 1.1, 1.2, 1.3 
def new_case(case):
    for number, case_type in enumerate(case, start=1):
        print(f"{case_type['case number']}. {case_type['complaint']}")
    case_number = int(input("Which case option will you be adding to? (Type the number) "))
    name = input("What is the name of this new case? ")

    case[case_number - 1]["case name"] = name
    print(cases)

# #status_report updates status of date from one of the case options to a different one or to "none"
def status_report():
    for number, category in enumerate(cases, start=1):
        case_name = category["case name"] or category["complaint"]
        print(f"{category['case number']}. {case_name}")
    try:
        case_number = int(input("\n Which case would you like to update? "))
        category = cases[case_number - 1]
    except (ValueError, IndexError):
        print("Please enter a valid case number.")
        return

    report_date = input("Date (YYYY-MM-DD): ").strip()
    category["status report"] = report_date
    case_name = category["case name"] or category["complaint"]
    print(f"{case_name} - {category['status report']}")
    print(cases)
# #calc_solution prints one of the keys in the dictionary along with the notes updated to that portion 
# def calc_solution():

#Nashayla's addition to change multiple things if needed
def initial_choices():
    while True:
        print("Choose one using its number:\n 1: Add a case\n 2: Case status\n 3: Add to notes\n 4: Review your cases notes\n 5: delete resolved case \n6: Exit ")
        choice = input("Your choice: ")

        if choice == "1":
            new_case(cases)
        elif choice == '2':
            status_report()
        elif choice == '3':
            for case in cases:
                name = case["case name"] or case["complaint"]
                print(f"{case['case number']}. {name}")

            case_number = int(input("Which case are you adding notes to? "))
            note = input("Enter your note: ")
            cases[case_number - 1]["notes"].append(note)
            print(cases)

        elif choice == '4':
            for case in cases:
                name = case["case name"] or case["complaint"]
                print(f"{case['case number']}. {name}")

            case_number = int(input("Which case notes do you want to look at "))
            for note in cases[case_number - 1]["notes"]:
                selected_case = cases[case_number - 1]

                if selected_case["notes"]:
                    for note in selected_case["notes"]:
                        print(note)
        # elif choice == "5":
        #     #delete resolved cases
        # elif choice == "6":
        #     print("Exited")
        #     break
        else:
            print("Please choose from the options provided")
        # elif choice == '3':
        #     #add notes to case
        # elif choice == '4':
        #     #review cases notes
        # elif choice == "5":
        #     #delete resolved cases
        # elif choice == "6":
        #     print("Exited")
        #     break


initial_choices()