DROP TABLE IF EXISTS systems;
DROP Table IF EXISTS planets;
DROP TABLE IF EXISTS visits;


CREATE TABLE systems (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    system_id INT REFERENCES systems(id) ON DELETE CASCADE,
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    goal VARCHAR(255),
    planet_id INT REFERENCES planets(id) ON DELETE CASCADE, 
    achieved BOOLEAN 
);