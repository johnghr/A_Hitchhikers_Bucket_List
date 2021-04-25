from db.run_sql import run_sql

from models.planet import Planet

def save(planet):
    sql = "INSERT INTO planets (name, system_id) VALUES (%s, %s) RETURNING *"
    values = [planet.name, planet.system.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    planet.id = id
    return planet
