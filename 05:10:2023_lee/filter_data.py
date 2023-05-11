import pandas as pd


arms = pd.read_csv("arms_data/Academic_Information_Football__20230511.csv")
xos = pd.read_csv("xos_data/XOSlist.csv")

init_length = len(xos)


names = arms.iloc[:,1:3]
droped_count = 0

for i in range(len(names)):
    first_name = names.iloc[i][0]
    last_name = names.iloc[i][1]
    cf = xos.loc[xos["First Name"] == first_name]
    cl = xos.loc[xos["Last Name"] == last_name]
    if len(cf) != 0 and len(cl) != 0:
        for index in cl.index:
            if index in cf.index:
                droped_count += 1
                xos.drop(index, inplace = True )
    
xos.to_csv("filtered_data.csv")
print(f"Initial Recruits: {init_length}\nFiltered Recruits: {droped_count}")
    
