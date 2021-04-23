from db.run_sql import run_sql

from models.visit import Visit
from models.system import System

import repositories.system_repository as system_repository

def save(visit):
    sql = "INSERT INTO visits (goal, system_id, achieved) VALUES (%s, %s, %s) RETURNING *"
    values = [visit.goal, visit.system.id, visit.achieved]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id
    return visit