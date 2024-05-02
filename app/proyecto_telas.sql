-- Tabla para camisetas
CREATE TABLE camisetas (
    id INTEGER PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    color VARCHAR(50),
    talla VARCHAR(10),
    material VARCHAR(100),
    precio FLOAT
);

-- Tabla para pantalones
CREATE TABLE pantalones (
    id INTEGER PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    color VARCHAR(50),
    talla VARCHAR(10),
    material VARCHAR(100),
    precio FLOAT
);

-- Tabla para chaquetas
CREATE TABLE chaquetas (
    id INTEGER PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    color VARCHAR(50),
    talla VARCHAR(10),
    material VARCHAR(100),
    precio FLOAT
);

-- Tabla para clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(200)
);

-- Tabla para pedidos
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    fecha_pedido DATE,
    cliente_id INTEGER,
    camiseta_id INTEGER,
    pantalon_id INTEGER,
    chaqueta_id INTEGER,
    cantidad INTEGER,
    total FLOAT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (camiseta_id) REFERENCES camisetas(id),
    FOREIGN KEY (pantalon_id) REFERENCES pantalones(id),
    FOREIGN KEY (chaqueta_id) REFERENCES chaquetas(id)
);

-- Tabla para tiendas
CREATE TABLE tiendas (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200)
);

-- Tabla para inventario de tiendas
CREATE TABLE inventario_tiendas (
    id INTEGER PRIMARY KEY,
    tienda_id INTEGER,
    camiseta_id INTEGER,
    pantalon_id INTEGER,
    chaqueta_id INTEGER,
    cantidad_disponible INTEGER,
    FOREIGN KEY (tienda_id) REFERENCES tiendas(id),
    FOREIGN KEY (camiseta_id) REFERENCES camisetas(id),
    FOREIGN KEY (pantalon_id) REFERENCES pantalones(id),
    FOREIGN KEY (chaqueta_id) REFERENCES chaquetas(id)
);

-- Tabla para envíos
CREATE TABLE envios (
    id INTEGER PRIMARY KEY,
    pedido_id INTEGER,
    fecha_envio DATE,
    direccion_destino VARCHAR(200),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

-- Tabla para pagos
CREATE TABLE pagos (
    id INTEGER PRIMARY KEY,
    pedido_id INTEGER,
    monto FLOAT,
    fecha_pago DATE,
    metodo_pago VARCHAR(50),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

-- Tabla para proveedores
CREATE TABLE proveedores (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(200)
);