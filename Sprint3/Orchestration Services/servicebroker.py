'''
*******************************************************************************
* Service Broker
*
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


arr = sys.argv[1:]
language = str(arr[-1])
#print(language.upper() == "ENGLISH")
if(language.upper() == "ENGLISH"):
  #print(arr)
  arr.pop()
  pass
elif(language.upper() == "SPANISH"):
  arr.pop()
  pass
elif(language.upper() == "GERMAN"):
  arr.pop()
  pass
else:
  language = "ENGLISH"
#print(arr)
  


# Get number of service from first line  
service = str(arr[0])
if (service=="Tax"):
  #Run Federal Taxes Module CalcFederalTaxes
  with open('output.txt', 'w') as f:
    for element in arr[1:]:
        if(element == arr[-1]):
          f.write(element)
        else:
          f.write(element + ',')
  command = ["python3", "CalcFederalTaxes.py", "output.txt"]
  output = subprocess.run(command, capture_output=True, text=True)
  output = output.stdout
  if "Error" in output:
    output = output.split("Error: ")
    error = int(output[1])
    command = ["python3", "messages.py", str(error), str(language)]
    output = subprocess.run(command, capture_output=True, text=True)
    print(output.stdout)  
  else:
    print(output)
  
elif(service=="IRA"):
  #Run Monthly IRA Payout Module
  with open('output.txt', 'w') as f:
    for element in arr[1:]:
        if(element == arr[-1]):
          f.write(element)
        else:
          f.write(element + ',')
  command = ["python3", "CalcMonthlyPayoutIRA.py", "output.txt"]
  output = subprocess.run(command, capture_output=True, text=True)
  output = output.stdout
  if "Error" in output:
    output = output.split("Error: ")
    error = int(output[1])
    command = ["python3", "messages.py", str(error), str(language)]
    output = subprocess.run(command, capture_output=True, text=True)
    print(output.stdout)  
  else:
    print(output)
  
  
elif(service=="Payroll"):
  #Run Payroll Module
  with open('output.txt', 'w') as f:
    for element in arr[1:]:
        f.write(element + '\n')
  command = ["python3", "payrollpaychecks.py", "output.txt"]
  output = subprocess.run(command, capture_output=True, text=True)
  output = output.stdout
  if "Error" in output:
    output = output.split("Error: ")
    error = int(output[1])
    command = ["python3", "messages.py", str(error), str(language)]
    output = subprocess.run(command, capture_output=True, text=True)
    print(output.stdout)  
  else:
    print(output)
  
  
'''
Example of how it works
Command line prompt: "python3 servicebroker.py Payroll 100000 4"
Runs the service broker and passes the argument Payroll to signify that it wants to run the payroll paychecks calculation and then provides the two parameters for the calculation, 100000(gross annual income) and 4(number of pay periods)
output:
Medicade: 362.5
FICA: 100000.0175
State: 875.0000000000001
Federal: 8750.0
Total owed: 109987.5175
'''
