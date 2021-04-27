from db.run_sql import run_sql

from models.system import System


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
    return systems


def select(id):
    user = None
    sql = "SELECT * FROM systems WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        system = System(result['name'], result['id'] )
    return system

def update(system):
    sql = "UPDATE systems SET name = %s WHERE id = %s"
    values = [system.name, system.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM systems WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE  FROM systems"
    run_sql(sql)