"""Contains the class Access Key"""
import hashlib

class AccessKey():
    """Class representing the key for accessing the building"""

    def __init__(self, dni, access_code, notification_emails, validity):
        self.__key = None  # Creamos este atributo que nos devuelve la llave creada.
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__id_document = dni
        self.__access_code = access_code
        self.__notification_emails = notification_emails
        #justnow = datetime.utcnow()
        self.__issued_at =1618514085.955216

        if validity == 0:
            self.__expiration_date = 0
        else:
            #timestamp is represneted in seconds.microseconds
            #validity must be expressed in senconds to be added to the timestap
            self.__expiration_date = self.__issued_at + (validity* 30 * 24 * 60 * 60)#Añadimos un *30 para que al hacer los test, estos no expiren

    def __signature_string(self):
        """Composes the string to be used for generating the key"""
        return "{alg:"+str(self.__alg)+",typ:"+str(self.__type)+",accesscode:"+str(self.__access_code)+",issuedate:"+str(self.__issued_at)+",expirationdate:"+str(self.__expiration_date)+"}"

    @property
    def id_document( self ):
        """Property that represents the dni of the visitor"""
        return self.__id_document

    @id_document.setter
    def id_document( self, value ):
        self.__id_document = value

    @property
    def access_code(self):
        """Property that represents the access_code of the visitor"""
        return self.__access_code
    @access_code.setter
    def access_code(self, value):
        self.__access_code = value

    @property
    def notification_emails(self):
        """Property that represents the access_code of the visitor"""
        return self.__notification_emails

    @notification_emails.setter
    def notification_emails(self, value ):
        self.__notification_emails = value

    @property
    def key(self):
        """Returns the sha256 signature"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value
