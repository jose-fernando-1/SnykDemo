"""Exemplo didático intencionalmente vulnerável. Use apenas localmente."""
import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="Snyk Demo — versão vulnerável")
DB_PATH = ":memory:"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, 'Alice')")
    conn.execute("INSERT OR IGNORE INTO users (id, name) VALUES (2, 'Bruno')")
    return conn

@app.get("/")
def home():
    return {"message": "Snyk demo: versão vulnerável", "docs": "/docs"}

@app.get("/users")
def get_user(user_id: str = Query(default="1", description="ID de demonstração")):
    # INTENCIONALMENTE INSEGURO: concatenação/interpolação na consulta SQL.
    # Não use este padrão em aplicações reais.
    conn = get_connection()
    try:
        sql = f"SELECT id, name FROM users WHERE id = {user_id}"
        rows = conn.execute(sql).fetchall()
        return {"users": [{"id": row[0], "name": row[1]} for row in rows]}
    finally:
        conn.close()
