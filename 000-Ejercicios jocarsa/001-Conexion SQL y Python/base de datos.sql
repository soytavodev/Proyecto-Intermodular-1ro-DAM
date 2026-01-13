CREATE DATABASE IF NOT EXISTS clientes;
USE clientes;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    edad INT
);

INSERT INTO clientes (nombre, apellidos, edad) VALUES 
('Ana', 'García', 30),
('Luis', 'Pérez', 25),
('María', 'López', 40);

-- Creación del usuario (solo si no existe)
CREATE USER IF NOT EXISTS 'clientes'@'localhost' IDENTIFIED BY 'Clientes123$';
GRANT ALL PRIVILEGES ON clientes.* TO 'clientes'@'localhost';
FLUSH PRIVILEGES;
