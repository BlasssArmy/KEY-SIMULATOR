"""Module """
import secure_all
import json
from pathlib import Path
import re
from datetime import datetime

class AccessManager:
    """Class for providing the methods for managing the access to a building"""

    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""
        if len(dni) != 9 or not str.isdigit(dni[:-1]):
            return False
        dni_number = int(dni[:-1])
        valid_char = 'TRWAGMYFPDXBNJZSQVHLCKE'
        if valid_char[dni_number % 23] == dni[-1]:
            return True
        return False


    @staticmethod
    def validate_access_type(access_type):
        '''Validamos el tipo de acceso sólo vale Resident o Guest'''
        if access_type != "Resident" and access_type != "Guest":
            raise secure_all.access_management_exception.AccessManagementException(
                "El tipo de acceso solicitado no es válido.")
        return True

    @staticmethod
    def validate_name_and_surname(name_and_surname):
        """Validamos el Nombre y Apellido"""

        regex_name = r"[A-Za-z]\s[A-Za-z]"
        if not re.search(regex_name, name_and_surname):
            raise secure_all.access_management_exception.AccessManagementException(
                "El nombre no es válido")
        return True

    @staticmethod
    def validate_email(email):
        """Valida el email"""

        regex_mail = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z]"
        if not re.search(regex_mail, email):
            raise secure_all.access_management_exception.AccessManagementException(
                "El formato de correo electrónico no es válido")
        return True

    @staticmethod
    def validate_days(access_type, validity):
        """Validamos que los dias correspondan"""

        if access_type == "Guest" and (validity < 2 or validity > 15):
            raise secure_all.access_management_exception.AccessManagementException(
                "El número de días no tiene un valor válido")
        if access_type == "Resident" and validity != 0:
            raise secure_all.access_management_exception.AccessManagementException(
                "El número de días no tiene un valor válido")
        return True

    def request_access_code(self, id_document, full_name, access_type, email_address, validity):
        """Nos devuelve el codigo de acceso para la persona que lo solicita"""
        file_pf_request = str(Path.home()) + "/PycharmProjects/G80.T2.EG3/src/JsonFiles/storeRequest.json"

        code = secure_all.access_request.AccessRequest(id_document, full_name, access_type, email_address,
                                                       validity).access_code

        request = secure_all.access_request.AccessRequest(id_document, full_name, access_type, email_address,
                                                          validity).__dict__
        request.update({"_AccessRequest__access_code": code})

        list_of_requests = []

        if not self.validate_dni(id_document):
            raise secure_all.access_management_exception.AccessManagementException(
                "El DNI recibido no es válido o no tiene un formato válido")

        if self.validate_name_and_surname(full_name) and self.validate_access_type(access_type) and self.validate_email(
                email_address) and self.validate_days(access_type, validity):

            try:
                with open(file_pf_request, "r", encoding="utf-8", newline="") as file:
                    list_of_requests = json.load(file)
                    for requets in list_of_requests:
                        for key in requets:
                            if key == "_AccessRequest__id_document" and requets[key] == id_document:
                                raise secure_all.access_management_exception.AccessManagementException("DNI usado")

                list_of_requests.append(request)
                with open(file_pf_request, "w", encoding="utf-8", newline="") as file:
                    json.dump(list_of_requests, file, indent=2)

            except FileNotFoundError:
                list_of_requests.append(request)
                with open(file_pf_request, "w", encoding="utf-8", newline="") as file:
                    json.dump(list_of_requests, file, indent=2)

            return code

    @staticmethod
    def comprobar_que_el_archivo_formato_json(path):
        """Comprobamos que el fichero que pasamos como parámetro sea un .json"""

        if path[-5:] != ".json":
            raise secure_all.access_management_exception.AccessManagementException("El archivo no tiene formato JSON.")



    def get_access_key(self, input_file):
        """Función que devuelve una key """

        File_pf_request = str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/storeRequest.json"
        self.comprobar_que_el_archivo_formato_json(input_file)
        file_pf_request = str(Path.home()) + "/PycharmProjects/G80.T2.EG3/src/JsonFiles/storeRequest.json"  # El path de fichero de requets

        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                fichero_parametro = json.load(file)  # Cargamos el fichero que nos han pasado como parámetro

        except json.JSONDecodeError as ex:
            raise  secure_all.access_management_exception.AccessManagementException("JSON-decode error - Wrong JSON format") from  ex

        try:
            with open(file_pf_request, "r", encoding="utf-8", newline="") as file:
                fichero_request = json.load(file)  # Cargamos el fichero donde estan todos los datos de todas las solicitudes(requets)
            with open(File_pf_request, "r", encoding="utf-8", newline="") as file:
                fichero_request = json.load(file)
        except FileNotFoundError as ex:
            raise  secure_all.access_management_exception.AccessManagementException("Wrong path") from  ex


        validity = None
        is_in_requets = False
        lista_parametros = ["AccessCode", "DNI", "NotificationMail"]

        if len(fichero_parametro) != 3:
            raise secure_all.access_management_exception.AccessManagementException(
                "JSON-decode error - Wrong JSON format")
        for a in fichero_parametro:
            if a not in lista_parametros:
                raise secure_all.access_management_exception.AccessManagementException(
                    "JSON-decode error - Wrong JSON format")
        for j in fichero_request:
            if fichero_parametro["DNI"] == j["_AccessRequest__id_document"] and fichero_parametro["AccessCode"] == j["_AccessRequest__access_code"]:
                for x in fichero_parametro["NotificationMail"]:
                    if x == j["_AccessRequest__email_address"]:
                        is_in_requets = True
                        validity=j["_AccessRequest__validity"]

        if is_in_requets is not True :
            raise secure_all.access_management_exception.AccessManagementException("No se encuentra el archivo de datos")

        my_beautiful_key = secure_all.access_key.AccessKey(fichero_parametro["DNI"], fichero_parametro["AccessCode"],fichero_parametro["NotificationMail"], validity)

        file_path_keys=str(Path.home()) + "\PycharmProjects\G80.T2.EG3/src/JsonFiles/storeKeys.json"
        code_key=my_beautiful_key.key

        dict=my_beautiful_key.__dict__



        dict["_AccessKey__key"]=code_key #Añadimos code_key al diccionario


        list_of_keys=[]


        try:
            with open(file_path_keys, "r", encoding="utf-8", newline="") as file:
                list_of_keys = json.load(file)

            list_of_keys.append(dict)
            with open(file_path_keys, "w", encoding="utf-8", newline="") as file:
                json.dump(list_of_keys, file, indent=2)

        except FileNotFoundError:
            list_of_keys.append(dict)
            with open(file_path_keys, "w", encoding="utf-8", newline="") as file:
                json.dump(list_of_keys, file, indent=2)

        return code_key


    @staticmethod
    def check_key(key):
        """Comprobamos que el formato de la key es correcto"""
        regex_key = '[0-9a-f]{64}'
        if re.search(regex_key,key):
            return True
        raise secure_all.access_management_exception.AccessManagementException("invalid key")
    @staticmethod
    def read_key_file(input_file):
        """Leemos la Key"""
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                list_keys = json.load(file)
        except json.JSONDecodeError as ex:
            raise secure_all.access_management_exception.AccessManagementException(
                "JSON-decode error - Wrong JSON format") from ex

        except FileNotFoundError as ex:
            raise secure_all.access_management_exception.AccessManagementException("Wrong path") from ex
        return list_keys
    def open_door(self,key):
        """Si la key es correcta devolvemos un True"""
        self.check_key(key)
        storeKeys = str(Path.home()) + "/PycharmProjects/G80.T2.EG3/src/JsonFiles/storeKeys.json"
        list_keys=self.read_key_file(storeKeys)

        justnow = datetime.utcnow()
        justnow_timestamp =datetime.timestamp(justnow)

        for k in list_keys:

            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"]>justnow_timestamp or k["_AccessKey__expiration_date"]==0):
                return True

        raise secure_all.access_management_exception.AccessManagementException("key is not found or is expired")
