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

