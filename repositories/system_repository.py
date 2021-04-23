from db.run_sql import run_sql

from models.system import System
from models.task import Task



def save(visit):
    sql = "INSERT INTO systems (name) VALUES (%s) RETURNING *"
    values = [system.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    system.id = id
    return system