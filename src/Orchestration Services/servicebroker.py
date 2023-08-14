'''
*******************************************************************************
* Service Broker
* Akhil Manoj
* Component: Orchestration Services
********************************************************************************
* Function:
* Runs the service modules and returns the output from them 
*-------------------------------------------------------------------------------
* Input:
* Parameters - Service Name, inputs for the respective modules, language(default to english if not specified)
* Output: Outputs from the modules 
* Return – None
********************************************************************************
'''
import sys
import subprocess
import os
import re


arr = sys.argv[1:]

# Check if the last element is a number
if re.match(r"\d+", str(arr[-1])):
    error_language = "ENGLISH"
else:
    # Read the contents of the languages.txt file
    os.chdir("..")
    os.chdir("Utility")
    with open("languages.txt", "r") as file:
        languages = file.read().splitlines()

    # Check if the language is in the list languages
    if str(arr[-1]).upper() in languages:
        error_language = str(arr[-1])
    else:
        error_language = "ENGLISH"
        command = ["python3", "messages.py", str(813), str(error_language)]
        output = subprocess.run(command, capture_output=True, text=True)
        print(output.stdout)

    # Remove the last element from the list
    arr.pop()

files = []
for file in os.listdir():
  if os.path.isfile(file):
    files.append(file)

os.chdir("..")
os.chdir("Orchestration Services")
services_dict = {}
with open('services.txt', 'r') as f:
  # loop through each line in the file
  for line in f:
    # split the line into key and value using comma as separator
    key, value = line.strip().split(',')
    # add the key-value pair to the dictionary
    services_dict[key] = value
service = str(arr[0])
if service in services_dict:
  split = services_dict[service].split(" ")
  language = split[0]
  language = language[1:]
  file = split[1]
  file = file[:-1]
  os.chdir("..")
  os.chdir("Business Services")
  with open('output.txt', 'w') as f:
    for element in arr[1:]:
        if(element == arr[-1]):
          f.write(element)
        else:
          f.write(element + ',')
  command = [language, file, "output.txt"]
  #print(command) 
  output = subprocess.run(command, capture_output=True, text=True)
  output = output.stdout
  if "Error" in output:
    os.chdir("..")
    os.chdir("Utility")
    output = output.split("Error: ")
    error = int(output[1])
    split = services_dict["Error"].split(" ")
    language = split[0]
    language = language[1:]
    file = split[1]
    file = file[:-1]
    command = [language, file, str(error), str(error_language)]
    output = subprocess.run(command, capture_output=True, text=True)
    output = output.stdout
    print(output)  
  else:
    print(output)
else:
  os.chdir("..")
  os.chdir("Utility")
  #print(os.getcwd())
  command = ["python3", "messages.py", str(703), str(error_language)]
  output = subprocess.run(command, capture_output=True, text=True)
  print(output.stdout)
  
  
'''
Example of how it works
cmd line prompt: python3 servicebroker.py Payroll 100000 4
Runs the service broker and passes the argument Payroll to signify that it wants to run the payroll paychecks calculation and then provides the two parameters for the calculation, 100000(gross annual income) and 4(number of pay periods)
output:
Medicade: 362.5
FICA: 100000.02
State: 875.0
Federal: 8750.0
Total owed: 109987.52
'''

