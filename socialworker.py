# Code your program directly here or include a link to your work here
# Aiwin and Nashayla's code yayyayayya
# Aiwin will build the lists + dictionary and the functions/starting the functions and names
# Nashayla will build within the functions for the CREATE/READ/UPDATE/DELETE
# Add case numbers
#Case workers can only have once case in each category so there isnt too much of a workload
cases = [
   "domestic violence" , "self harm" , "orphaned child" , "drug abuse" ,
   "child neglect" , "geriatric care" , "child murderers" , "homelessness"
]

help = [
    "safe housing" , "crisis lifeline" , "foster care" , "group counseling" ,
    "parenting classes" , "assisted living" , "protective custody" , "transitional shelters"
]

# cases = [
#     {'case number': 1, 'complaint': 'domestic violence', 'service offered': 'safe housing', 'last meeting': '8/2/2026', 'notes': []},
# ]


# Create a dictionary connecting cases to help
# case_number = {}
case_number = {}
value_to_add = 8
counter = 1
for i in range(len(cases)):
    case_number[cases[i]] = {
        "help": help[i],
        "case_number": counter
    }
    counter += 1
print(case_number)
# The client notes
notes = {}
#new_case attributes a case number that either corresponds to domestic violence like 1.1, 1.2, 1.3 
# def new_case(case):
#
# #status_report updates status of date from one of the case options to a different one or to "none"
# def status_report():
    
# #calc_solution prints one of the keys in the dictionary along with the notes updated to that portion 
# def calc_solution():
