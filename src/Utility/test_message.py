'''
*******************************************************************************
* Messagses unit test
* Nguyen Tran
* Component: Utiity
********************************************************************************
* Function:
* test the messages module
*-------------------------------------------------------------------------------
* Input:
* Parameters - none
* Output: the test score
********************************************************************************
'''
import unittest
import messages

class TestMessage(unittest.TestCase):
    def test_englishMsg(self):
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"english"),
                          'Invalid parameters')
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"English"),
                          'Invalid parameters')
        self.assertEqual(messages.getServiceBrokerErrorMessage('404',"English"),
                          'Not Found')
        self.assertEqual(messages.getServiceBrokerErrorMessage('703',"English"),
                          'Service Not Found')
        self.assertEqual(messages.getServiceBrokerErrorMessage('813',"English"),
                          'Language Not Found')
        self.assertEqual(messages.getServiceBrokerErrorMessage('903',"English"),
                          'Tax Year Not Found')
        

    def test_spanishMsg(self):
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"spanish"),
                          'Parámetros Inválidos')
        self.assertEqual(messages.getServiceBrokerErrorMessage('404',"spanish"),
                          'No Encontrada')
        self.assertEqual(messages.getServiceBrokerErrorMessage('703',"spanish"),
                          'Servicio No Encontrado')
        self.assertEqual(messages.getServiceBrokerErrorMessage('813',"spanish"),
                          'Idioma No Encontrado')
        self.assertEqual(messages.getServiceBrokerErrorMessage('903',"spanish"),
                          'Año Fiscal No Encontrado')
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"spa"),
                          'Invalid parameters')
        

    def test_GermanMsg(self):
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"german"),
                          'Ungültige Parameter')
        self.assertEqual(messages.getServiceBrokerErrorMessage('404',"german"),
                          'Nicht gefunden')
        self.assertEqual(messages.getServiceBrokerErrorMessage('703',"german"),
                          'Service Nicht Gefunden')
        self.assertEqual(messages.getServiceBrokerErrorMessage('813',"german"),
                          'Sprache Nicht Gefunden')
        self.assertEqual(messages.getServiceBrokerErrorMessage('903',"german"),
                          "Steuerjahr Nicht Gefunden")
        self.assertEqual(messages.getServiceBrokerErrorMessage('401',"ger"),
                          'Invalid parameters')


if __name__ == '__main__':
    unittest.main()