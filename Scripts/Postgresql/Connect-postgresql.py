import psycopg2

# Parámetros de conexión
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"  # Opcional, por defecto es 5432

# Crear la conexión usando f-string
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Crear cursor y ejecutar consulta
cur = conn.cursor()
cur.execute("SELECT * FROM articles")
rows = cur.fetchall()

# Mostrar resultados
for row in rows:
    print(row)

# Cerrar conexión
cur.close()
conn.close()
