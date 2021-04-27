from db.run_sql import run_sql

from models.planet import Planet

import repositories.system_repository as system_repository

def save(planet):
    sql = "INSERT INTO planets (name, system_id) VALUES (%s, %s) RETURNING *"
    values = [planet.name, planet.system.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    planet.id = id
    return planet

def select_all():
    planets = []

    sql = "SELECT * FROM planets"
    results = run_sql(sql)

    for row in results:
        system = system_repository.select(row['system_id'])
        planet =  Planet(row['name'], system, row['id'])
        planets.append(planet)

    return planets

def select(id):
    planet = None

    sql = "SELECT * FROM planets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        system = system_repository.select(result['system_id'])
        planet = Planet(result['name'], system, result['id'])
    
    return planet

def update(planet):
    sql = "UPDATE planets SET name = %s WHERE id = %s"
    values = [planet.name, planet.system.id, planet.id]
    run_sql(sql, values)
        
def delete(id):
    sql = "DELETE FROM planets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM planets"
    run_sql(sql)



