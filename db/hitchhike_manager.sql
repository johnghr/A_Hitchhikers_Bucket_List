DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS systems;




CREATE TABLE systems (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    goal VARCHAR(255)
    system_id INT REFERENCES systems(id),
    achieved BOOLEAN 
);