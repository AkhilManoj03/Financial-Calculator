'''
*******************************************************************************
* Server Broker unit test
* Matthew Coffey
* Component: Utiity
********************************************************************************
* Function:
* test the Server Broker module
*-------------------------------------------------------------------------------
* Input:
* Parameters - none
* Output: the test score
********************************************************************************
'''
import unittest
import subprocess


class TestPayroll(unittest.TestCase):

    def test_payroll(self):
        command = ["python3", "servicebroker.py", "Payroll", "100000", "4"]
        expected_output = "Medicade: 362.5\nFICA: 100000.0175\nState: 875.0000000000001\nFederal: 8750.0\nTotal owed: 109987.5175\n\n"
        output = subprocess.run(command, capture_output=True, text=True).stdout
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
