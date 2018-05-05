import os
import csv

"""This is the PyBoss Hw main script file
declare variables for use in main function, not necessary but helps me understand what key variables are
"""
fullName = []
DOB = []
DOBNew = []
SSN = []
SSNNew = []
newEmployeeInfo = []


'ask for user input of file name, not including .csv suffix'
userfile = input("Which file would you like to open?   ")
'open file and define a function to grab state abbreviations'
with open(userfile + ".csv" , 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    def GetState(arg1):
            us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }
            return us_state_abbrev[arg1] 
    
    'iterate through each line in csv file and split full name'
    'afterwards split DOB and replace with //'
    'pull last 4 digits of SSN and replace the rest with *'
    'call GetState function to get abbreviation'
    'append everything to a new dict'
    for line in csv_reader:
        fullName = line["Name"].split(' ')
        firstName = fullName[0] 
        lastName = fullName[1]
        DOB = line["DOB"].split("-")
        DOBNew = (DOB[1] + "/" + DOB[2] + "/" + DOB[0])
        SSNSplit = line["SSN"].split("-")
        SSNNew = "***-**-" + SSNSplit[2]
        newState = GetState(line["State"])
        newEmployeeInfo.append(
            {
                "Emp ID" : line["Emp ID"],
                "First Name" : firstName,
                "Last Name"  : lastName,
                "DOB" : DOBNew,
                "SSN" : SSNNew,
                "State" : newState         
            
            }
        )
'write new csv file and use newEmployeeInfo to write rows'        
newuserfile = userfile + ".csv"
 

csvpath = os.path.join("output", newuserfile)
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State" ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(newEmployeeInfo)
    
    for line in newEmployeeInfo:
        print(line)
        
