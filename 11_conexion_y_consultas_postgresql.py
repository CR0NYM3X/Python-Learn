# Archivo: 08_conexion_y_consultas_postgresql.py
# Tema: Conexión y consultas en PostgreSQL con psycopg2 y asyncpg
# Descripción: Este script explica cómo instalar bibliotecas, conectarse a PostgreSQL, ejecutar consultas SQL y manejar transacciones, con ejemplos comentados.

# -------------------------------
# 📌 1. Instalación de bibliotecas
# -------------------------------
# Para instalar psycopg2 (sincrónico):
#   pip install psycopg2-binary
# Para instalar asyncpg (asíncrono):
#   pip install asyncpg

# -------------------------------
# 📌 2. Conexión con psycopg2 (sincrónico)
# -------------------------------
import psycopg2

def conexion_psycopg2():
    """Ejemplo de conexión y consulta con psycopg2."""
    try:
        conn = psycopg2.connect(
            dbname="tu_base_de_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Ejecutar una consulta SELECT
        cursor.execute("SELECT * FROM empleados;")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

        # Insertar un nuevo registro
        cursor.execute("INSERT INTO empleados (nombre, edad) VALUES (%s, %s);", ("Ana", 28))

        # Actualizar un registro
        cursor.execute("UPDATE empleados SET edad = %s WHERE nombre = %s;", (29, "Ana"))

        # Eliminar un registro
        cursor.execute("DELETE FROM empleados WHERE nombre = %s;", ("Ana",))

        # Manejo de transacciones
        conn.commit()  # Confirmar los cambios

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error en la conexión o consulta:", e)

# -------------------------------
# 📌 3. Conexión con asyncpg (asíncrono)
# -------------------------------
# ⚠️ Nota: asyncpg debe estar instalado para que este bloque funcione.

import asyncio
# import asyncpg  # Descomenta esta línea si tienes asyncpg instalado

# async def conexion_asyncpg():
#     """Ejemplo de conexión y consulta con asyncpg."""
#     try:
#         conn = await asyncpg.connect(
#             user='tu_usuario',
#             password='tu_contraseña',
#             database='tu_base_de_datos',
#             host='127.0.0.1'
#         )

#         # SELECT
#         filas = await conn.fetch("SELECT * FROM empleados;")
#         for fila in filas:
#             print(dict(fila))

#         # INSERT
#         await conn.execute("INSERT INTO empleados(nombre, edad) VALUES($1, $2);", "Luis", 35)

#         # UPDATE
#         await conn.execute("UPDATE empleados SET edad = $1 WHERE nombre = $2;", 36, "Luis")

#         # DELETE
#         await conn.execute("DELETE FROM empleados WHERE nombre = $1;", "Luis")

#         # Transacción
#         async with conn.transaction():
#             await conn.execute("INSERT INTO empleados(nombre, edad) VALUES($1, $2);", "Marta", 40)

#         await conn.close()
#     except Exception as e:
#         print("Error en asyncpg:", e)

# -------------------------------
# ✅ Conclusión
# -------------------------------
# - psycopg2 es ideal para scripts sincrónicos y es ampliamente usado.
# - asyncpg permite trabajar con PostgreSQL de forma asíncrona, útil en aplicaciones modernas.
# - Ambos permiten ejecutar consultas SQL y manejar transacciones de forma segura.

# Fin del archivo
