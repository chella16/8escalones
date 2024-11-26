
class DAO_Administradores ():
    
    def __init__(self, bd):
        self.__BD = bd
    
    def verificacion (self, user, contraseña):
        
        conexion = self.__BD.get_conexion()
        c = conexion.cursor()
        
        c.execute ("SELECT 1 FROM administradores WHERE nombre_administrador = (?) AND contraseña_administrador = (?)", (user, contraseña,))
        resu = c.fetchone()
        if resu:
            self.__BD.cerrar_conexion()
            return True
        else:
            self.__BD.cerrar_conexion()
            return False
    
    def alta_administrador (self, user, contraseña):
        conexion = self.__BD.get_conexion()
        c = conexion.cursor()
        
        c.execute ("INSERT INTO administradores (nombre_administrador, contraseña_administrador) VALUES (?, ?)", (user, contraseña,))
        
        conexion.commit()
        self.__BD.cerrar_conexion()
