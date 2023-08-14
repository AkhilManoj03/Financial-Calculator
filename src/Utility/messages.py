'''
*******************************************************************************
* Messagses module
* Nguyen Tran
* Component: Utiity
********************************************************************************
* Function:
* The Messages module prints out the messages that have been sent to the module.
*-------------------------------------------------------------------------------
* Input:
* Parameters - Message code, Language to translate the message, language(default to english if not specified)
* Output: Outputs from the modules 
* Return – Error message in the language specified in input parameter
********************************************************************************
'''
import sys
import os
import json

#current_dir = os.getcwd()

def readJson(language: str='english'):
    datas = {}
    if os.path.isfile("MessageCode" + "/" + language.lower() + ".txt"):
        with open("MessageCode" + "/" + language.lower() + ".txt", encoding="utf-8") as f:
            datas = json.load(f)
    else:
        with open("MessageCode/english.txt", encoding="utf-8") as f:
            datas = json.load(f)
    return datas

def errorMessageDatas(language: str='english'):
    return readJson(language.upper())

def getServiceBrokerErrorMessage(ServiceCode: str, language:  str = "ENGLISH"):
    errorMessage = errorMessageDatas(language.upper())
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