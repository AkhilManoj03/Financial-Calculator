'''
********************************************
*  Module: payrollpaychecks
*  Matthew Coffey
*  Component: Task
*  Description:
*   Calculates FICA, Medicade, State, and Federal tax from each payroll paycheck
*--------------------------------------------
* Input: (arguments)
*   Gross Annual Income
*   Number of pay periods
*
* Output:
*    FICA, Medicade, State, Federal and total tax 
********************************************
'''

import sys

#proccess the text file and returns a list with each line as an element
def process_file(filename):
    # Opens the file and reads its contents
    with open(filename, 'r') as file:
      # Read all the lines of the file into a list
      lines = file.readlines()
      # Adds each line to an array element 
    lines = [line.rstrip('\n') for line in lines]
    return lines

#takes in the gross annual income and pay periods and calculates 
def payRoll(gross, periods):
    #opens the payrolltax.txt file and gets the rates for each and adds it to the rates dictionary 
    rates = {}
    with open('payrolltax.txt') as f:
      for line in f:
        line = line.strip()  
        if line:  
          key, value = line.split(',')  
          rates[key] = float(value) 
    #calculats medicade, fica, state, federal, and total tax and prints it out 
    medicade = round(gross * rates['MEDICADE'] / periods, 2)
    fica = round(gross + rates['FICA'] / periods, 2)
    state = round(gross * rates['STATE'] / periods, 2)
    federal = round(gross * rates['FEDERAL'] / periods, 2)
    print("Medicade: " + str(medicade))
    print("FICA: " + str(fica))
    print("State: " + str(state))
    print("Federal: " + str(federal))
    print("Total owed: " + str(medicade+fica+state+federal))

def main():
    if __name__ == "__main__":
    # Check if a txt file parameter was provided
      if len(sys.argv) < 2:
        print("Error: 401")
      elif len(sys.argv) > 2:
        print("Error: 401")
      else:
        # Get the filename from the command line parameter
        filename = sys.argv[1]
        # Process the file into array
        arr = process_file(filename)
        arr = arr[0].split(",")
        #print(arr)
        if len(arr) < 2:
          print("Error: 401")
          return
        elif len(arr) > 2:
          print("Error: 401")
          return
        payRoll(int(arr[0]),int(arr[1]))
main()
    
