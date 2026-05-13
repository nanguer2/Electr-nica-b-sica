import  pyhodbc
# Configura la conexion a tu SQL Server local
server = "localhost\SQLEXPRESS"
database = "Main"
username = "admin"
password = "12345"

Dethon

connection_string = f'Driver={(SQL Server}} ;Server={server} ; Database={c

# Conecta a la base de datos
connection = pyodbc. connect(connection_string)
cursor = connection. cursor()

# Ejemplo de consulta SELECT
query = M0"
SELECT Alarma, Count(Alarma) AS 'Cantidad' FROM PLC_02
GROUP BY Alarma

cursor.execute (query)
# Imprime los resultados
for nombre, cantidad in cursor:
print(f"Tenemos {cantidad} sensores con estado (nombre}")

# Cierra la conexion
connection. close()