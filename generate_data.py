import sys
import csv
import glob


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
    with open("ncsa_combined_data.csv", 'w', encoding = "UTF-8", newline = '') as wFile:
        writer = csv.writer(wFile)

        #read any csv files in this directory
        path = "./ncsa_data/*.csv" 
        writer.writerow(['First Name', 'Last Name', 'Recruiting Profile Link', 'Grad Year', 'Position(s)', 'Height', 'Weight', 'High School', 'Club Team', 'Phone', 'Email', 'Address', 'City', 'State', 'Zip', 'Rating', 'GPA', 'Class Rank'])
        for fileName in glob.glob(path):
            f = open(fileName, 'r', encoding = "UTF-8")
            with f as rFile:
                spamreader = csv.reader(rFile, delimiter=',')
                next(spamreader)
                for line in spamreader:
                    writer.writerow(line)
        f.close
        wFile.close


'''
Gathers front rush data and stores it in a dic. The key is the name of the recruit and the value 
is the list that contains all of the information of the recruit.
The key is stored in the format: firstname + lastname (ALL LOWERCASE)

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
                recruit_data[generate_name(line[0] + line[1])] = line
                print(generate_name(line[0] + line[1] + line[2]))
    
    f.close()
    return recruit_data

'''
returns the general format of the name string that functions will use it as key to identify.
lowercase first name + last name
'''
def generate_name(name):
    name = name.lower()
    name = name.replace(" ","")
    name = name.replace("'","")
    name = name.replace("/","")
    return name


def testFunction():
    path = "./ncsa_data/*.csv"
    for fileName in glob.glob(path):
        print(fileName) 

'''
main methode that calls all the functions. Will generate one big dataset, then load all the data from
front rush recruits. Then will cross reference and write
'''
def main():
    merge_NCSA_Data()
    front_rush_data = gather_front_rush_data()
    #create a dic that maps the columns from NCSA to front rush
    #create a function that cross references the combined_ncsa_data and front rush dic to either add or write new lines into it
        #We can seperate this into three fields, one for new recruits
        #one with the old recruits but updated info
        #one combined with both of them
        #make sure to label the correct coaches and watch for null spaces. Add NCSA for source, good luck!
    #testFunction()

main()