"""tests función 1"""
import unittest
from secure_all import AccessManager,AccessManagementException
from pathlib import Path
from os import remove
import os
import os.path

class MyTestCase(unittest.TestCase):
    """clase de tests"""
    @classmethod
    def setUpClass(cls):
        """Borramos el fichero cada vez que lo iniciamos"""
        my_file = str(Path.home()) + "/PycharmProjects/G80.T2.EG3/src/JsonFiles/storeRequest.json"
        if os.path.exists(my_file):
            remove(my_file)

    def test_request_access_code_dni_guest_ok_1(self):
        """Test para validar"""
        ms = AccessManager()
        value = ms.request_access_code("06648714N", "Alberto Blas", "Guest", "123@gmail.com", 5)
        self.assertEqual(value, "0423f1b8bf30ded51090b741ac33593c")

    def test_request_access_code_dni_resident_ok_2(self):
        """Test para validar"""
        ms = AccessManager()
        value = ms.request_access_code("02735176Q", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(value, "ae20be24d691f0a09668b9dddab9354b")

    def test_request_access_code_dni_repetido_3(self):
        """Test para validar"""
        ms = AccessManager()
        value = ms.request_access_code("12345678Z", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(value, "023fe62b081fb11625a0651d34dea7cf")
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("12345678Z", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message, "DNI usado")

    def test_request_access_code_7_numeros_4(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("0273517Z", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_8_numeros_5(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("027351765Z", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_no_letra_dni_6(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("12345678", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_2_letras_dni_7(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("12345678QE", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_letra_numeros_cambiados_8(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("Q02735176", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_letra_entre_numeros_9(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("027Q35176", "Fidel Navaaa", "Resident", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_tipo_de_acceso_distinto_10(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Amigo", "fidel@gmail.com", 0)
        self.assertEqual(cm.exception.message,"El tipo de acceso solicitado no es válido.")

    def test_request_access_code_guest_menos_dias_11(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidel@gmail.com", 1)
        self.assertEqual(cm.exception.message,"El número de días no tiene un valor válido")

    def test_request_access_code_guest_mas_dias_12(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidel@gmail.com", 16)
        self.assertEqual(cm.exception.message,"El número de días no tiene un valor válido")

    def test_request_access_code_resident_num_dist_0_13(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Resident", "fidel@gmail.com", 1)
        self.assertEqual(cm.exception.message,"El número de días no tiene un valor válido")

    def test_request_access_code_nums_end_email_14(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidel@gmail.34", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_no_at_email_15(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidelgmail.com", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_blank_email_16(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "@gmail.es", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_no_domain_email_17(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidel@gmail", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_no_domain_2_email_18(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "fidel@.es", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_no_email_19(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Fidel Navaaa", "Guest", "", 13)
        self.assertEqual(cm.exception.message,"El formato de correo electrónico no es válido")

    def test_request_access_code_no_dni_20(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("", "Fidel Navaaa", "Guest", "fidel@gmail.es", 13)
        self.assertEqual(cm.exception.message,"El DNI recibido no es válido o no tiene un formato válido")

    def test_request_access_code_no_name_21(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "", "Guest", "fidel@gmail.es", 13)
        self.assertEqual(cm.exception.message, "El nombre no es válido")

    def test_request_access_code_int_name_22(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "45 86", "Guest", "fidel@gmail.es", 13)
        self.assertEqual(cm.exception.message, "El nombre no es válido")

    def test_request_access_code_name_no_surname_23(self):
        """Test para validar"""
        ms = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            ms.request_access_code("02735176Q", "Alberto", "Guest", "fidel@gmail.es", 13)
        self.assertEqual(cm.exception.message, "El nombre no es válido")


if __name__ == '__main__':
    unittest.main()
