CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    ano INTEGER,
    placa TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS maintenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER,
    tipo TEXT,
    descricao TEXT,
    data TEXT,
    km INTEGER,
    custo REAL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);
