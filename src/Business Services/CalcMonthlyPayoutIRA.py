"""
********************************************
*  Module: CalcMonthlyPayoutIRA
*  William Simms
*  Component: Task
*  Description:
*   Calculates monthly payout amount for IRA based on start payout age and
*   completed payout age
*--------------------------------------------
* Input: (arguments)
*   Gross amount in IRA
*   Age for starting payout
*   Age for payout completion
*
* Output:
*    Amount for each monthly payout
********************************************
"""

import sys


def calc(UserInput):

    # Opens document with name provided on command line
    with open(UserInput, 'r') as Document:
        DocumentList = Document.readlines()

    # Stores each comma separated item in a list
    lineHolder = DocumentList[0]
    itemList = lineHolder.split(",")
    itemList = [int(i) for i in itemList]

    # Checks if there are 3 items in the .txt if there are not
    # the program exits the function and prints an error code
    if len(itemList) != 3:
        error = "Error: 401"
        return error

    # Simple calculations for finding monthly payout amount
    subbedAge = itemList[2] - itemList[1]
    monthTotal = subbedAge * 12
    grossIRA = itemList[0]
    monthlyPayout = grossIRA / monthTotal
    monthlyPayout = str(round(monthlyPayout, 2))

    return monthlyPayout


def main():
    # Ensures that correct amount of command line arguments had been provided
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Error: 401")
    else:
        print(calc(sys.argv[1]))


if __name__ == "__main__":
    main()

"""For reference, this was tested with UserInputIRA.txt containing input
in the form of ## 800000,65,85 ## and those were the numbers used.
Expected output is 3333.33"""