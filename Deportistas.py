class deportistas:
    def __init__(self, mysql):
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
        
    def consultar(self):
        sql = "SELECT * FROM deportista WHERE activo=1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, deportista):
        sql = f"INSERT INTO deportista (documento,nombre,estatura,peso,nacimiento,fecha_creado,activo)\
            VALUES ('{deportista[0]}','{deportista[1]}','{deportista[2]}','{deportista[3]}','{deportista[4]}','{deportista[5]}',1)"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def modificar(self, deportista):
        sql = f"UPDATE deportista SET nombre='{deportista[1]}',\
            estatura='{deportista[2]}',peso='{deportista[3]}'\
                WHERE documento='{deportista[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
    def borrar(self, documento):
        sql = f"UPDATE deportista SET activo=0 WHERE documento={documento}"
        self.cursor.execute(sql)
        self.conexion.commit()
