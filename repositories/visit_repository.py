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

def delete_all():
    sql = "DELETE  FROM visits"
    run_sql(sql)

def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
        system = system_repository.select(row['id'])
        visit = Visit(row['goal'], system, row['achieved'], row['id'])
        visits.append(visit)
    return visit

def select(id):
    visit = None

    sql = "SELECT * FROM visits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        system = system_repository.select(result['system_id'])
        visit = Visit(result['goal'], system, result['achieved'], result['id'])
    return visit