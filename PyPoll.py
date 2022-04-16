#Data we need to retreive
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

### Import the datetime class from the datetime module.
#import datetime
### Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
### Print the present time.
#print("The time right now is ", now)

### 1. Launch the Python interpreter.
### 2. Type import csv to import the module.
### 3. Press Enter.
### 4. Type dir(csv). The "dir" is short for "directory".

### Assign a variable for the file to load and the path.
#file_to_load = r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis\Resources\election_results.csv"
#### Open the election results and read the file.
#with open(file_to_load) as election_data:

     ### To do: perform analysis.
     #print(election_data)

### 1. Import the csv and os modules.
#import csv
#import os
### 2. Add the filename variable that references the path to election_results.csv.
#file_to_load = os.path.join(r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis","Resources", "election_results.csv")
### 3. Open the election_results.csv using the with statement as the filename object, election_data.
#with open(file_to_load) as election_data:
### 4. Print the filename object.
#    print(election_data)

### Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join(r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis","analysis", "election_analysis.txt")
### Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()

### Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join(r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis","analysis", "election_analysis.txt")

### Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    ### Write some data to the file.
    #txt_file.write("Hello World")

    ### Write three counties to the file.
     #txt_file.write("Countries in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join(r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis","Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(r"C:\Users\aramo\Documents\TEC\Modulo 3\Election_Analysis","analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)