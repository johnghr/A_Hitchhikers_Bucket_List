from db.run_sql import run_sql

from models.system import System
from models.visit import Visit



def save(system):
    sql = "INSERT INTO systems (name) VALUES (%s) RETURNING *"
    values = [system.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    system.id = id
    return system

def select_all():
    systems = []

    sql = "SELECT * FROM systems"
    results = run_sql(sql)

    for row in results:
        system = System(row['name'], row['id'])
        systems.append(system)
        return system


def select(id):
    system = None
    sql = "SELECT FROM systems WHERE id = %s"
    values = [id]
    result = run_sql(values, sql)[0]

    if system is not None:
        system = System(result['name'], result['id'])
    return system



def delete_all():
    sql = "DELETE  FROM systems"
    run_sql(sql)