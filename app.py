from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.rouse('/')
def saludo():
    #conexion
    conn = psycopg2.connect(
        host="db"
        database="testdb",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )
    #creamos el cursor
    cur = conn.cursor()
    cur.execute("SELECT 'Hola de postgre'")
    #hacemos que tome la primera fila del resultado
    msg = cur.fetchone()[0]
    cur.close()
    conn.close()
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

