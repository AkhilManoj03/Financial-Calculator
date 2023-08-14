"""
********************************************
*  Module: CalcFederalTaxes
*  William Simms
*  Component: Task
*  Description:
*   Calculates amount of federal taxes owed
*--------------------------------------------
* Input: (arguments)
*   Tax year filing status for
*   Status (joint, single, Head of household first letter in lower case)
*   Gross annual income
*
* Output:
*    Amount of federal taxes owed
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
    itemList = [str(i) for i in itemList]

    # Checks if there are 3 items in the .txt if there are not
    # the program exits the function and prints an error code
    if len(itemList) != 3:
        error = "Error: 401"
        return error

    # Uses year at 0 index and filing status in the form of a letter at 1 index
    txtString = itemList[0] + itemList[1] + '.txt'
    grossAnnualIncome = int(itemList[2])

    # Opens document for filing year and status specified
    with open(txtString, 'r') as Document:
        DocumentList = Document.readlines()

    federalTaxes = 0
    previousItem0 = 0
    leftoverTaxableIncome = grossAnnualIncome

    for item in DocumentList:

        # Stores each line of document in a list
        # List items are separated by a comma in the document
        itemList = item.split(",")
        itemList = [float(i) for i in itemList]

        # Stops for loop if the gross annual income is less than the amount
        # specified as the tax bracket max amount
        if grossAnnualIncome <= itemList[0]:
            holder = federalTaxes
            federalTaxes = leftoverTaxableIncome * itemList[1] + holder
            break

        # Running calculation of amount owed in taxes
        else:
            taxProduct = (itemList[0] - previousItem0) * itemList[1]
            federalTaxes = federalTaxes + taxProduct
            leftoverTaxableIncome = grossAnnualIncome - itemList[0]
            previousItem0 = itemList[0]

    federalTaxes = str(round(federalTaxes, 2))

    return federalTaxes


def main():
    # Ensures that correct amount of command line arguments had been provided
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("401")
    else:
        print(calc(sys.argv[1]))


if __name__ == "__main__":
    main()

"""For reference, this was tested with UserInputFedTax.txt containing input
in the form of ## 2020,S,100000 ## and those were the numbers used.
Expected output is 18079.5"""