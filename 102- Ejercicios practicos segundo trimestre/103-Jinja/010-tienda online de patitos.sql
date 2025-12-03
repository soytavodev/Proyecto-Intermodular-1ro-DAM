/* ============================================================
   CREACIÓN DE LA BASE DE DATOS
   ============================================================ */
CREATE DATABASE tienda_patos;
USE tienda_patos;

/* ============================================================
   TABLA: categorias_patos (MADRE)
   ============================================================ */
CREATE TABLE categorias_patos (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT
);

/* ============================================================
   TABLA: productos (MADRE)
   ============================================================ */
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    color VARCHAR(50),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias_patos(id_categoria)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

/* ============================================================
   TABLA: clientes (MADRE)
   ============================================================ */
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    telefono VARCHAR(50),
    localidad VARCHAR(255)
);

/* ============================================================
   TABLA: pedidos (HIJA DE clientes)
   ============================================================ */
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    estado VARCHAR(50),
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

/* ============================================================
   TABLA: lineas_pedido (HIJA DE pedidos y productos)
   ============================================================ */
CREATE TABLE lineas_pedido (
    id_linea INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

/* ============================================================
   VISTAS (para mostrar info combinada correctamente)
   ============================================================ */

-- Productos con su categoría
CREATE VIEW vista_productos_categorias AS
SELECT 
    p.id_producto, p.nombre AS producto,
    p.descripcion, p.precio, p.stock, p.color,
    c.nombre AS categoria, c.descripcion AS descripcion_categoria
FROM productos p
LEFT JOIN categorias_patos c ON p.id_categoria = c.id_categoria;

-- Pedidos con datos del cliente
CREATE VIEW vista_pedidos_clientes AS
SELECT
    pd.id_pedido, pd.fecha, pd.estado,
    c.nombre, c.apellidos, c.email
FROM pedidos pd
LEFT JOIN clientes c ON pd.id_cliente = c.id_cliente;

-- Detalle completo de pedidos
CREATE VIEW vista_detalle_pedidos AS
SELECT
    pd.id_pedido, pd.fecha, pd.estado,
    c.nombre AS cliente_nombre, c.apellidos AS cliente_apellidos,
    pr.nombre AS producto, lp.cantidad,
    lp.precio_unitario,
    (lp.cantidad * lp.precio_unitario) AS subtotal
FROM pedidos pd
LEFT JOIN clientes c ON pd.id_cliente = c.id_cliente
LEFT JOIN lineas_pedido lp ON pd.id_pedido = lp.id_pedido
LEFT JOIN productos pr ON lp.id_producto = pr.id_producto;

/* ============================================================
   INSERTS — ORDEN CORRECTO: categorias → productos → clientes → pedidos → lineas_pedido
   ============================================================ */

-- CATEGORÍAS DE PATOS
INSERT INTO categorias_patos (nombre, descripcion) VALUES
('Patos Clásicos', 'Patos de goma tradicionales'),
('Patos Temáticos', 'Patos con temática de películas, profesiones y más'),
('Patos Edición Limitada', 'Modelos exclusivos y coleccionables'),
('Patos Gigantes', 'Patos de goma tamaño XL para bañeras grandes');

-- PRODUCTOS
INSERT INTO productos (nombre, descripcion, precio, stock, color, id_categoria) VALUES
('Pato Clásico Amarillo', 'El tradicional pato de goma de baño', 4.99, 100, 'Amarillo', 1),
('Pato Pirata', 'Pato temático con parche y sombrero', 7.99, 50, 'Negro', 2),
('Pato Superhéroe', 'Pato con capa y máscara', 8.99, 30, 'Azul', 2),
('Pato Edición Dorada', 'Pato de goma recubierto en color dorado', 19.99, 10, 'Dorado', 3),
('Pato XXL Gigante', 'Pato enorme, ideal para piscinas', 49.99, 5, 'Amarillo', 4);

-- CLIENTES
INSERT INTO clientes (nombre, apellidos, email, telefono, localidad) VALUES
('Gustavo', 'Delnardo', 'gustavo@example.com', '666111222', 'Valencia'),
('Betza', 'Matheus', 'betza@example.com', '666333444', 'Madrid'),
('Carlos', 'Ramírez', 'carlos@example.com', '666555666', 'Barcelona');

-- PEDIDOS
INSERT INTO pedidos (fecha, estado, id_cliente) VALUES
('2025-11-21 10:30:00', 'Procesando', 1),
('2025-11-22 14:10:00', 'Enviado', 2),
('2025-11-23 09:00:00', 'Completado', 1);

-- LÍNEAS DE PEDIDO
INSERT INTO lineas_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 4.99),  -- Pedido 1: 2 patos clásicos
(1, 2, 1, 7.99),  -- Pedido 1: 1 pato pirata
(2, 5, 1, 49.99), -- Pedido 2: 1 pato gigante
(3, 4, 2, 19.99), -- Pedido 3: 2 patos edición dorada
(3, 3, 1, 8.99);  -- Pedido 3: 1 superhéroe

