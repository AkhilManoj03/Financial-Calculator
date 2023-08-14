"""
********************************************
*  Module: messages.py
*  Component: Utility
*  Description:
*   Prints Errors in correct language
*--------------------------------------------
* Input: (arguments)
*   Error code from service broker
*   Language from service broker
*   (read from JSON data)
*
* Output:
*    Printed Error in correct language
********************************************
"""

import sys
import os
import json

current_dir = os.getcwd()

def readJson(language: str='english'):
    os.chdir(os.path.join(current_dir, "MessageCode"))
    with open(language.lower() + ".txt", encoding="utf-8") as f:
        datas = json.load(f)
    os.chdir(current_dir)
    return datas

def errorMessageDatas(language: str='english'):
    if language.upper() == "SPANISH":
        return readJson(language)
    if language.upper() == "GERMAN":
        return readJson(language)
    language = "ENGLISH"
    return readJson(language)

def getServiceBrokerErrorMessage(ServiceCode: str, language:  str = "ENGLISH"):
    errorMessage = errorMessageDatas(language)
    if language.upper() == "SPANISH":
        return errorMessage[ServiceCode]
    if language.upper() == "GERMAN":
        return errorMessage[ServiceCode]
    return errorMessage[ServiceCode]

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("401")
    elif len(sys.argv) == 2:
        print(getServiceBrokerErrorMessage(sys.argv[1]))
    else:
        print(getServiceBrokerErrorMessage(sys.argv[1],sys.argv[2]))


if __name__ == "__main__":
    main()