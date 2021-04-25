DROP TABLE IF EXISTS visits;
DROP Table IF EXISTS planets;
DROP TABLE IF EXISTS systems;



CREATE TABLE systems (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    system_id INT REFERENCES system(id)
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    goal VARCHAR(255)
    system_id INT REFERENCES systems(id),
    planet_id INT REFERENCES planets(id)
    achieved BOOLEAN 
);