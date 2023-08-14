import unittest
from io import StringIO
from unittest.mock import patch
from payrollpaychecks import process_file, payRoll


class TestPayroll(unittest.TestCase):

    def setUp(self):
        # Set up the file name and expected output
        self.file_name = 'UserInputPayroll.txt'
        self.expected_output = 'Medicade: 13.94\nFICA: 67.31\nState: 33.65\nFederal: 336.54\nTotal owed: 451.44\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_payroll(self, mock_stdout):
        # Arrange
        with open(self.file_name, 'w') as f:
            f.write('50000\n52\n')

        # Act
        arr = process_file(self.file_name)
        payRoll(int(arr[0]), int(arr[1]))

        # Assert
        self.assertEqual(mock_stdout.getvalue(), self.expected_output)

    def tearDown(self):
        # Remove the test file after the test is completed
        import os
        os.remove(self.file_name)
