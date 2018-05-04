import os
import csv

"""This is the PyBoss Hw main script file"""
fullName = []
firstName = []
lastName = []
DOB = []
DOBNew = []
SSN = []
SSNNew = []
newState = []
newEmployeeInfo = []



userfile = input("Which file would you like to open?   ")
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
newuserfile = userfile + ".csv"
 

csvpath = os.path.join("output", newuserfile)
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State" ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(newEmployeeInfo)
        
