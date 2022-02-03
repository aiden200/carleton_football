import sys
import csv
import glob
import os
'''
Python script to create the files listed under the README.
Please contact the author regarding questions or issues about the program.
Wrote by Aiden Chang.
Last Updated: 01/29/2022 by Aiden Chang

TODOS:
Ask Journell about the desired columns 
Generate an export criteria
Find the designated states per Coac

states
send to admissions yes, height weight

fields not interested in 


'''

DEBUG = False
'''
Merges all the different csv files in the subdirectory ncsa_data. 
Must be encoded in utf-8 format.
Must be in csv.
Generates one combined datasheet of all the NCSA recruits.
Columns are
    'First Name', 'Last Name', 'Recruiting Profile Link', 'Grad Year', 'Position(s)', 'Height', 
    'Weight', 'High School', 'Club Team', 'Phone', 'Email', 'Address', 'City', 'State', 'Zip', 
    'Rating', 'GPA', 'Class Rank'
'''
def merge_NCSA_Data():
    i = 0
    if os.path.exists("./final_data_sets/ncsa_combined_data.csv"):
        os.remove("./final_data_sets/ncsa_combined_data.csv")
    with open("./final_data_sets/ncsa_combined_data.csv", 'w', encoding = "UTF-8", newline = '') as wFile:
        writer = csv.writer(wFile)

        #read any csv files in this directory
        path = "./ncsa_data/*.csv" 
        writer.writerow(['First Name', 'Last Name', 'Recruiting Profile Link', 'Grad Year', 'Position(s)', 'Height', 'Weight', 'High School', 'Club Team', 'Phone', 'Email', 'Address', 'City', 'State', 'Zip', 'Rating', 'GPA', 'Class Rank'])
        for fileName in glob.glob(path):
            f = open(fileName, 'r', encoding = "UTF-8")
            with f as rFile:
                spamreader = csv.reader(rFile, delimiter=',')
                print("Reading file: " + fileName)
                categories = next(spamreader)

                for line in spamreader:
                    writer.writerow(create_line(categories, line))
                    i+= 1
        f.close()
        wFile.close()
    print("Generated %d recruits" % (i))
'''
create the line with the correct categories in the correct spot
'''
['First Name', 'Last Name', 'Recruiting Profile Link', 'Grad Year', 'Position(s)', 'Height', \
    'Weight', 'High School', 'Club Team', 'Phone', 'Email', 'Address', 'City', 'State', 'Zip', \
        'Rating', 'GPA', 'Class Rank']
def create_line(categories, line):
    returnList = []
    if find_indicies(categories, "First Name") != -1:    
        returnList.append(line[find_indicies(categories, "First Name")])
    else:
        returnList.append("")
    if find_indicies(categories, "Last Name") != -1:    
        returnList.append(line[find_indicies(categories, "Last Name")])
    else:
        returnList.append("")
    if find_indicies(categories, "Recruiting Profile Link") != -1:    
        returnList.append(line[find_indicies(categories, "Recruiting Profile Link")])
    else:
        returnList.append("")
    if find_indicies(categories, "Grad Year") != -1:    
        returnList.append(line[find_indicies(categories, "Grad Year")])
    else:
        returnList.append("")
    if find_indicies(categories, "Position(s)") != -1:    
        returnList.append(line[find_indicies(categories, "Position(s)")])
    else:
        returnList.append("")
    if find_indicies(categories, "Height") != -1:    
        returnList.append(line[find_indicies(categories, "Height")])
    else:
        returnList.append("")
    if find_indicies(categories, "Weight") != -1:    
        returnList.append(line[find_indicies(categories, "Weight")])
    else:
        returnList.append("")
    if find_indicies(categories, "High School") != -1:    
        returnList.append(line[find_indicies(categories, "High School")])
    else:
        returnList.append("")
    if find_indicies(categories, "Club Team") != -1:    
        returnList.append(line[find_indicies(categories, "Club Team")])
    else:
        returnList.append("")
    if find_indicies(categories, "Phone") != -1 or find_indicies(categories, "Cell Phone") != -1:
        if find_indicies(categories, "Phone") > find_indicies(categories, "Cell Phone"):
            returnList.append(line[find_indicies(categories, "Phone")])
        else:
            returnList.append(line[find_indicies(categories, "Cell Phone")])
    else:
        returnList.append("")
    if find_indicies(categories, "Email") != -1:    
        returnList.append(line[find_indicies(categories, "Email")])
    else:
        returnList.append("")
    if find_indicies(categories, "Address") != -1:    
        returnList.append(line[find_indicies(categories, "Address")])
    else:
        returnList.append("")
    if find_indicies(categories, "City") != -1:    
        returnList.append(line[find_indicies(categories, "City")])
    else:
        returnList.append("")
    if find_indicies(categories, "State") != -1:    
        returnList.append(line[find_indicies(categories, "State")])
    else:
        returnList.append("")
    if find_indicies(categories, "Zip") != -1:    
        returnList.append(line[find_indicies(categories, "Zip")])
    else:
        returnList.append("")
    if find_indicies(categories, "Rating") != -1:    
        returnList.append(line[find_indicies(categories, "Rating")])
    else:
        returnList.append("")
    if find_indicies(categories, "GPA") != -1:    
        returnList.append(line[find_indicies(categories, "GPA")])
    else:
        returnList.append("")
    if find_indicies(categories, "City") != -1:    
        returnList.append(line[find_indicies(categories, "Class Rank")])
    else:
        returnList.append("")
    return returnList
'''
finds the indicies that the category_type corresponds in the data sheet.
If not found, return -1
'''
def find_indicies(categories, category_type):
    for i in range(len(categories)):
        if categories[i] == category_type:
            return i
    return -1

'''
Gathers front rush data and stores it in a dic. The key is the name of the recruit and the value 
is the list that contains all of the information of the recruit.
The key is stored in the format: firstname + lastname + state(ALL LOWERCASE)

IMPORTANT:
state needs to be in the third column, as first name needs to be in the first and last name in the second
'''
def gather_front_rush_data():
    path = './front_rush_recruits/*.csv'
    recruit_data = {}
    for fileName in glob.glob(path):
        f = open(fileName, 'r', encoding = "UTF-8")
        with f as rFile:
            spamreader = csv.reader(rFile, delimiter=',')
            next(spamreader)
            for line in spamreader:
                recruit_data[generate_name(line[0] + line[1] + line[2])] = line
                #print(generate_name(line[0] + line[1] + line[2]))
    
    f.close()
    return recruit_data

'''
returns the general format of the name string that functions will use it as key to identify.
lowercase first name + last name + state
'''
def generate_name(name):
    name = name.lower()
    name = name.replace(" ","")
    name = name.replace("'","")
    name = name.replace("/","")
    return name


'''
Creates new recruits from NCSA data that are not in frontrush.
Reads from "./final_data_sets/ncsa_combined_data.csv"
'''
def create_new_recruits(front_rush_data):
    i = 0
    if os.path.exists("./final_data_sets/new_recruits.csv"):
        os.remove("./final_data_sets/new_recruits.csv")
    with open("./final_data_sets/new_recruits.csv", 'w', encoding = "UTF-8", newline = '') as wFile:
        writer = csv.writer(wFile)
        writer.writerow(['Last Name', 'First', 'HS', 'Email', 'Twitter', 'Cell Phone', \
            'Address', 'City', 'State', 'Zip', 'Video Link', 'Send to Admissions', 'Source', \
                'Recruiting Coach', 'Grad Year', 'Primary Position', 'Positions (All)', 'GPA', 'ACT', 'SAT'])
        f = open("./final_data_sets/ncsa_combined_data.csv", 'r', encoding = "UTF-8")
        with f as rFile:
            
            spamreader = csv.reader(rFile, delimiter=',')
            next(spamreader)
            for line in spamreader:
                if generate_name((line[0] + line[1] + abriviate_states(line[13]))) not in front_rush_data:
                    i+= 1
                    write_line = [line[1], line[0], line[7], line[10],"" ,line[9], line[11], line[12], \
                        abriviate_states(line[13]), line[14], "", "Yes", "NCSA", find_coach(abriviate_states(line[13])), \
                            line[3], abriviate_position(line[4]), "", line[16], "", ""]
                    writer.writerow(write_line)
        print("Generated " + str(i) + " recruits.")
        f.close()
        wFile.close()
    
'''
Finds the coach with the corresponding states
'''
def find_coach(state):
    #NEED TO UPDATE THIS
    state_responsibility = [
        ["Lee", "OH", 'MO', 'KS', 'IL', 'MI', 'KY', 'WV', 'SD', 'ND', 'NE', 'AB', 'ON'],
        ["Journell", "AK", 'CA', 'CO', 'HI', 'ID', 'MT', 'OK', 'OR', 'UT', 'WA', 'WI', 'WY'],
        ["Kent", "AL", 'FL', 'GA', 'IN', 'LA', 'MS', 'SC', 'TN', 'TX'],
        ["Davies", "PA", 'NC', 'MA', 'NJ', 'NY', 'DE', 'CT', 'NH', 'MD', 'DC', 'ME', 'RI', 'VT', 'VA'],
        ['Van Epps', 'MN'],
        ["Erickson", "AZ", 'NV', 'NM']
    ]
    for item in state_responsibility:
        if state in item:
            return item[0]
    print("WARNING: Couldn't find coach assigned to state: " + state)
    print("Assigning to Journell")
    return "Jounell"

'''
Returns the abriviated string version of the position. Returns multiple positions as a string if there are multiple
'''
def abriviate_position(positions):
    abriv_position = {
        "runningback": "RB",
        "cornerback" :"CB",
        "widereceiver" : "WR",
        "middlelinebacker" : "LB",
        "outsidelinebacker" : "OLB",
        "offensivetackle" : "OL",
        "quarterback" : "QB",
        "safety" : "S",
        "center" : "OL",
        "offensiveguard" : "OL",
        "defensivetackle" : "DT",
        "athlete" : "Athlete",
        "punter" : "P",
        "tightend" : "TE",
        "defensiveend":"DE",
        "fullback":"FB",
        "kicker":"K",
        "longsnapper":"LS"
    }

    if ',' in positions:
        list_positions = positions.split(",")
        return_string = ""
        for single_position in list_positions:
            shortened_position= single_position.lower()
            shortened_position = shortened_position.replace(" ","")
            if shortened_position not in abriv_position:
                print("ERROR: " + positions + "position not recognized, check spelling or contact author")
                return_string = return_string + ","
            else:
                return_string = return_string + abriv_position[shortened_position] + ","
        return return_string[:len(return_string)-1]
    else:
        shortened_position = positions.lower()
        shortened_position = shortened_position.replace(" ","")
        if shortened_position not in abriv_position:
            print("ERROR: " + positions + "position not recognized, check spelling or contact author")
            return ""
        return abriv_position[shortened_position]


'''
changes full name state to abriviation. Throws an error and exits if its not there.
'''
def abriviate_states(state):
    states = {
    'alaska': 'AK',
    'alabama': 'AL',
    'arkansas': 'AR',
    'arizona': 'AZ',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'district of columbia': 'DC', #check
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'iowa': 'IA',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'massachusetts': 'MA',
    'maryland': 'MD',
    'maine': 'ME',
    'michigan': 'MI',
    'minnesota': 'MN',
    'missouri': 'MO',
    'mississippi': 'MS',
    'montana': 'MT',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'nebraska': 'NE',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'nevada': 'NV',
    'new york': 'NY',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode island': 'RI',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'virginia': 'VA',
    'vermont': 'VT',
    'washington': 'WA',
    'wisconsin': 'WI',
    'west virginia': 'WV',
    'wyoming': 'WY'
    }
    state = state.lower()
    if state not in states:
        print("ERROR " + state + "not a valid state")
        exit(0)
    return states[state]

def testFunction():
    path = "./formatting_examples/example_format.csv"
    '''for fileName in glob.glob(path):
        print(fileName) '''
    
    print(['Last Name', 'First', 'HS', 'Email', 'Twitter', 'Cell Phone', \
            'Address', 'City', 'State', 'Zip', 'Video Link', 'Send to Admissions', 'Source', \
                'Recruiting Coach', 'Grad Year', 'Primary Position', 'Positions (All)', 'GPA', 'ACT', 'SAT'])
    '''
    f = open(path, 'r', encoding = "UTF-8")
    with f as rFile:
        spamreader = csv.reader(rFile, delimiter=',')
        #next(spamreader)
        for line in spamreader:
            print(line)
            break
    '''

'''
main methode that calls all the functions. Will generate one big dataset, then load all the data from
front rush recruits. Then will cross reference and write
'''
def main():
    if DEBUG:
        testFunction()
    else:
        print("Starting Program...\n")
        print('Merging NCSA datasheets...\n')
        merge_NCSA_Data()
        print("Done\n\nCreated merge file in ncsa_combined_data.csv in directory final_data_sets\n\nLoading front rush recruit data...\n")
        front_rush_data = gather_front_rush_data()
        print("Done\n\nCross referencing... this might take some time\n")
        create_new_recruits(front_rush_data)
        print("Created new Recruit data in new_recruits.csv\n")
        #create a dic that maps the columns from NCSA to front rush
        #create a function that cross references the combined_ncsa_data and front rush dic to either add or write new lines into it
            #We can seperate this into three fields, one for new recruits
            #one with the old recruits but updated info
            #one combined with both of them
            #make sure to label the correct coaches and watch for null spaces. Add NCSA for source, good luck!


main()