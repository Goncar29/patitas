import sqlite3


class BaseDeDatos:
    url = '/home/carlos/EDX/proyecto/patitas.db'

    def _crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDeDatos.url)
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        self.conexion.commit()
        self._cerrar_conexion()

        return filas