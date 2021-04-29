from db.run_sql import run_sql

from models.visit import Visit
from models.system import System

import repositories.system_repository as system_repository
import repositories.planet_repository as planet_repository

def save(visit):
    # id assigned in database but not in python object instance
    sql = "INSERT INTO visits (goal, planet_id, achieved) VALUES (%s, %s, %s) RETURNING *"
    values = [visit.goal, visit.planet.id, visit.achieved]
    results = run_sql(sql, values)
    id = results[0]['id']
    # assigns id created in database to python object instance
    visit.id = id
    return visit


def select_all():
    visits = []

    sql = "SELECT * FROM visits"
    results = run_sql(sql)

    for row in results:
       
        planet = planet_repository.select(row['planet_id'])
        visit = Visit(row['goal'], planet, row['achieved'], row['id'])
        visits.append(visit)
    
    return visits

def select(id):
    visit = None

    sql = "SELECT * FROM visits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        planet = planet_repository.select(result['planet_id'])
        visit = Visit(result['goal'], planet, result['achieved'], result['id'])
    return visit

def update(visit):
    sql = "UPDATE visits SET (goal, planet_id, achieved) = (%s, %s, %s) WHERE id = %s"
    values = [visit.goal, visit.planet.id, visit.achieved, visit.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

