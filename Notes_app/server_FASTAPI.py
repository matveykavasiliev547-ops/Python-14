from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

db = sqlite3.connect('base.db', check_same_thread=False)

cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL)
    ''')

db.commit()

class Note(BaseModel):
    content: str


@app.post("/notes")
def add_note(note: Note):
    cursor.execute('INSERT INTO notes (content) VALUES (?)',(note.content,))
    db.commit()
    return {"status": "Ok", "id": cursor.lastrowid}

@app.get("/notes")
def get_notes():
    cursor.execute('SELECT id, content FROM notes')
    rows = cursor.fetchall()
    return [{"id": row[0], "content": row[1]} for row in rows]

@app.delete("/notes/{note_id}")
def delete_notes(note_id: int):
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"status": "deleted"}

@app.put("/notes/{note_id}")
def update_notes(note_id: int, note: Note):
    cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (note.content, note_id))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Note not found!")
    return {"status": "updated"}

@app.get("/")
def root():
    return {"message": "Hello, this is Notes API"}



