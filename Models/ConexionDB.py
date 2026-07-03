import mariadb as sql

class ConexionDB():
    def __init__(self):
        self.__host = "localhost"
        self.__port = 3306
        self.__user = "admin"
        self.__password = "juan123"
        self.__database = "Usuario_Notas"
        self.__connection = None
    
    def getconnection(self):
        return self.__connection
    
    def CrearConnection(self):
        self.__connection = sql.connect(
            host = self.__host,
            port = self.__port,
            user = self.__user,
            password = self.__password,
            database = self.__database,
        )
    
    def CerrarConnection(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None