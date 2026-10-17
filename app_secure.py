"""Versão corrigida para comparação com a demonstração vulnerável."""
import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="Snyk Demo — versão corrigida")
DB_PATH = ":memory:"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, 'Alice')")
    conn.execute("INSERT OR IGNORE INTO users (id, name) VALUES (2, 'Bruno')")
    return conn

@app.get("/")
def home():
    return {"message": "Snyk demo: versão corrigida", "docs": "/docs"}

@app.get("/users")
def get_user(user_id: int = Query(default=1, ge=1, description="ID numérico de demonstração")):
    # CORRIGIDO: consulta parametrizada; o valor não é concatenado ao SQL.
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, name FROM users WHERE id = ?",
            (user_id,),
        ).fetchall()
        return {"users": [{"id": row[0], "name": row[1]} for row in rows]}
    finally:
        conn.close()
