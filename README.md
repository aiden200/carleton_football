# NCSA and frontrush automatic cross reference program
## Made for Carleton College football recruiting
### Author: Aiden Chang, Last Updated: 01/28/2022

Reusable program to update recruit data. <br />
This site was built using [GitHub Pages](https://pages.github.com/). <br />
Refer to a [github tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) if unfamiliar with github <br />
These instructions are for mac users.<br />

**Virtual Enviroment Instructions**
Use code
```
pipenv install --dev
pipenv shell
```
to install dependencies and run on the pipenv shell.

**How to run**
Place all the recruit data from NCSA into the *ncsa_data* folder.<br />
All of the NCSA data must be in csv format and utf-8 encoded.<br />
Place a single recruit data from Front Rush in the *front_rush_recruits* folder.<br />
The file must be in csv format and utf-8 encoded. ***make sure there is only one file***<br />

Refer to the virtual enviroment instructions if your local machine do not have the same dependencies.<br />
Type in ```python3 generate_data.py``` and your combined file will be generated in the *combinedData.csv* file.<br />
