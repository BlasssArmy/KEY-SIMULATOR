"""tests función 2"""
import unittest
from secure_all import AccessManager,AccessManagementException
from pathlib import Path
from os import remove
import os
import os.path

class TestAccessManager(unittest.TestCase):
    """clase de tests"""
    @classmethod
    def setUpClass(cls):
        my_file = str(Path.home()) + "/PycharmProjects/G80.T2.EG3/src/JsonFiles/storeKeys.json"
        if os.path.exists(my_file):
            remove(my_file)

    def test_access_key_ok_con_2_emails_1(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/correcto_2_emails.json"
        my_key = AccessManager().get_access_key(my_file)
        self.assertEqual("149e8fa1d70e962c863ddca72015abe013e8e9cfff23244b8e457eb7abb390c8",my_key)

    def test_access_key_ok_con_1_email_2(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/correcto_1_email.json"
        my_key = AccessManager().get_access_key(my_file)
        self.assertEqual("115342913a466a9385574062e9340bfe5273a1e48f9d60d30bb23d5494327770", my_key)

    def test_access_key_otro_formato_fichero_3(self):
        """Test para validar"""
        my_file=str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_es_json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"El archivo no tiene formato JSON.")

    def test_access_key_los_datos_no_estan_storeRequest_4(self):
        """Test para validar"""
        my_file=str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_data_in_storeRequest.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"No se encuentra el archivo de datos")

    def test_access_key_dos_brackets_de_comienzo_5(self):
        """Test para validar"""
        my_file=str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/double_start_bracket.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"JSON-decode error - Wrong JSON format")

    def test_access_key_sin_bracket_de_comienzo_6(self):
        """Test para validar"""
        my_file=str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_start_bracket.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"JSON-decode error - Wrong JSON format")

    def test_access_key_sin_bracket_de_final_7(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_end_bracket.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"JSON-decode error - Wrong JSON format")

    def test_access_key_doble_bracket_de_final_8(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/double_end_bracket.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,"JSON-decode error - Wrong JSON format")

    def test_access_key_no_datos_9(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_datos.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_datos_duplicados_10(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/datos_repetidos.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_campo_1_repetido_11(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/campo_1_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_campo_1_12(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/no_campo_1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_separador_1_repetido_13(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/separador_1_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_separador_1_14(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_separador_1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_campo_2_repetido_15(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/campo_2_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_campo_2_16(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/campo_2_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_separador_2_17(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_separador_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_separador_2_repetido_18(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/separador_2_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_campo_3_19(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_campo_3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_campo_3_repetido_20(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/campo_3_repetido.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_e1_repetida_21(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/e1_repetida.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_e1_22(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_e1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_igualdad1_23(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_igualdad1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_igualdad1_24(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_igualdad1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_valor_dato1_25(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_valor_dato1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_valor_dato1_26(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_valor_dato1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_comillas_e1_27(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_e1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_comillas_e1_28(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_comillas_e1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_AccessCode_29(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_AccessCode.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_AccessCode_30(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_AccessCode.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_comillas_VD1_31(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_VD1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_dobles_comillas_VD1_32(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/dobles_comillas_VD1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_v1_33(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_v1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_v1_34(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_v1.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_etiqueta_2_35(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_etiqueta_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_etiqueta_2_36(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_etiqueta_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_igualador_2_37(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_igualador_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_igualador_2_38(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_igualador_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_valor_dato_2_39(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_valor_dato_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_doble_valor_dato_2_40(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_valor_dato_2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_comillas_e2_41(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_e2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_comillas_e2_42(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_comillas_e2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_DNI_43(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_DNI.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_DNI_44(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_DNI.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_comillas_vd2_45(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_vd2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_dobles_comillas_vd2_46(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/dobles_comillas_vd2.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_dato_DNI_47(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_dato_DNI.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_dato_DNI_48(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_dato_DNI.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_letra_dni_49(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_letra_dni.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_doble_letra_dni_50(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_letra_dni.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_doble_numeros_dni_51(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_numeros_dni.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_numeros_dni_52(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_numeros_dni.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_etiqueta_3_53(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_etiqueta_3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_etiqueta_3_54(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_etiqueta_3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_igualador_3_55(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_igualador_3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_igualador_3_56(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_igualador_3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_vd3_57(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_vd3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_vd3_58(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_vd3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_comillas_e3_59(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_e3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_comillas_e3_60(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_comillas_e3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_doble_NotificationMail_61(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_NotificationMail.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_NotificationMail_62(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_NotificationMail.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_corchs_dato3_63(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_corchs_dato3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message,  "No se encuentra el archivo de datos")

    def test_access_key_dobles_corchs_dato3_64(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/dobles_corchs_dato3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_sin_comillas_dato3_65(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_comillas_dato3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "JSON-decode error - Wrong JSON format")

    def test_access_key_sin_v3_66(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/sin_v3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")

    def test_access_key_doble_v3_67(self):
        """Test para validar"""
        my_file = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/doble_v3.json"
        my_key = AccessManager()
        with self.assertRaises(AccessManagementException) as cm:
            my_key.get_access_key(my_file)
        self.assertEqual(cm.exception.message, "No se encuentra el archivo de datos")
