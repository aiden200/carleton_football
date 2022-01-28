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
    with open("combinedData.csv", 'w', encoding = "UTF-8", newline = '') as wFile:
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
    #testFunction()

main()