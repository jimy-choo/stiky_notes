from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

note_db = [{"note_id":1,"text":"string","author":"string","t_create":"2024-03-05T02:34:29.837431","t_mod":"2024-03-05T02:34:29.837431"},{"note_id":2,"text":"string","author":"string","t_create":"2024-03-05T02:34:31.690578","t_mod":"2024-03-05T02:34:31.690578"}]    # база данных

class NoteItem(BaseModel):  # структура сущности - заметки
    note_id: int
    text: str
    author: str
    t_create: datetime
    t_mod: datetime


'''Создание заметки''' 

@app.post('/notes')
async def create_note(note: NoteItem):
    note.note_id = len(note_db) + 1 
    note.t_create = datetime.now()
    note.t_mod = datetime.now()
    note_db.append(note)
    return ()

'''Чтение заметки'''

@app.get('/notes')
async def get_note():
    return note_db

'''Удаление заметки'''

@app.delete('/notes/{note_id}')
async def delete_note(note_id:int):
    for key, value in enumerate(note_db):
        if value.note_id == note_id:
            note_db.pop(key)
            break
    else:
        raise HTTPException(404, detail = "Not found") 
            
