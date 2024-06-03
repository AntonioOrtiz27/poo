-- Crear base de datos
CREATE DATABASE logipack;

USE logipack;

-- Tabla de Sucursales
CREATE TABLE Sucursal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    provincia VARCHAR(50),
    localidad VARCHAR(50),
    direccion VARCHAR(100)
);

-- Tabla de Reparadores
CREATE TABLE Reparador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    dni VARCHAR(10),
    idsucursal INT,
    FOREIGN KEY (idsucursal) REFERENCES Sucursal (id)
);

-- Tabla de Transportes
CREATE TABLE Transporte (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numerotransporte VARCHAR(20) UNIQUE NOT NULL,
    fechahorasalida DATETIME,
    fechahorallegada DATETIME,
    idsucursal INT,
    FOREIGN KEY (idsucursal) REFERENCES Sucursal (id)
);

-- Tabla de Paquetes
CREATE TABLE Paquete (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numeroenvio VARCHAR(20) UNIQUE NOT NULL,
    peso DECIMAL(5, 2),
    nomdestino VARCHAR(50),
    dirdestino VARCHAR(100),
    entregado BOOLEAN DEFAULT FALSE,
    observaciones TEXT,
    idsucursal INT,
    idtransporte INT,
    idreparador INT,
    FOREIGN KEY (idsucursal) REFERENCES Sucursal (id),
    FOREIGN KEY (idtransporte) REFERENCES Transporte (id),
    FOREIGN KEY (idreparador) REFERENCES Reparador (id)
);