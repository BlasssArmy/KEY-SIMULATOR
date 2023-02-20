"""tests funcion 3"""
import unittest
from secure_all import AccessManager,AccessManagementException

class TestAccessManager(unittest.TestCase):
    '''clase de tests'''
    def test_comprobar_keys_correcta_1(self):
        """Test para validar"""
        my_key=AccessManager()
        result=my_key.open_door("115342913a466a9385574062e9340bfe5273a1e48f9d60d30bb23d5494327770")
        self.assertEqual(True,result)

    def test_comprobar_keys_correcta_2(self):
        """Test para validar"""
        my_key=AccessManager()
        result=my_key.open_door("149e8fa1d70e962c863ddca72015abe013e8e9cfff23244b8e457eb7abb390c8")
        self.assertEqual(True,result)

    def test_comprobar_keys_incorrectos_1(self):
        """Test para validar"""
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.open_door("555e8fa1d70e962c863ddca72015abe013e8e9cfff23244b8e457eb7abb390c8")
        self.assertEqual(cm.exception.message, "key is not found or is expired")

    def test_comprobar_keys_incorrectos_2(self):
        """Test para validar"""
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.open_door("555e8faq3e8e9cfff23244")
        self.assertEqual(cm.exception.message, "invalid key")
"""
    def test_comprobar_loop0_times(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.open_door("555e8faq3e8e9cfff23244")
        self.assertEqual(cm.exception.message, "invalid key")

    def test_comprobar_loop1_times(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.open_door("555e8faq3e8e9cfff23244")
        self.assertEqual(cm.exception.message, "invalid key")

    def test_comprobar_loop2_times(self):
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            result = my_key.open_door("555e8faq3e8e9cfff23244")
        self.assertEqual(cm.exception.message, "invalid key")
"""
if __name__ == '__main__':
    unittest.main()
