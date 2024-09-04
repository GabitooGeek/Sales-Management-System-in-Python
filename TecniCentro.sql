
-- Tabla para productos
CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

-- Tabla para proveedores
CREATE TABLE Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla para clientes
CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla para ventas
CREATE TABLE Ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    cantidad INT NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);

-- Smartphones
INSERT INTO Productos (nombre, precio, stock) VALUES
('iPhone 13 Pro', 999.00, 50),
('Samsung Galaxy S21', 799.00, 40),
('Google Pixel 6', 699.00, 30),
('OnePlus 9 Pro', 899.00, 35),
('Xiaomi Mi 11', 699.00, 45),
('Sony Xperia 1 III', 1099.00, 25);

-- Laptops
INSERT INTO Productos (nombre, precio, stock) VALUES
('MacBook Air M1', 999.00, 20),
('Dell XPS 13', 1299.00, 15),
('Lenovo ThinkPad X1 Carbon', 1499.00, 10),
('HP Spectre x360', 1299.00, 18),
('ASUS ROG Zephyrus G14', 1499.00, 12),
('Microsoft Surface Laptop 4', 1299.00, 22);

-- Tablets
INSERT INTO Productos (nombre, precio, stock) VALUES
('iPad Pro', 799.00, 30),
('Samsung Galaxy Tab S7', 649.00, 25),
('Microsoft Surface Pro 7', 799.00, 20),
('Amazon Fire HD 10', 149.00, 40),
('Lenovo Tab P11 Pro', 499.00, 30),
('Huawei MatePad Pro', 599.00, 28);

-- Smartwatches
INSERT INTO Productos (nombre, precio, stock) VALUES
('Apple Watch Series 7', 399.00, 35),
('Samsung Galaxy Watch 4', 349.00, 30),
('Fitbit Versa 3', 229.00, 20),
('Garmin Forerunner 945', 599.00, 15),
('Amazfit GTS 2', 179.00, 25),
('Suunto 7', 499.00, 18);

-- Auriculares y audífonos
INSERT INTO Productos (nombre, precio, stock) VALUES
('AirPods Pro', 249.00, 40),
('Sony WH-1000XM4', 349.00, 30),
('Bose QuietComfort 35 II', 299.00, 25),
('Sennheiser HD 560S', 199.00, 35),
('Jabra Elite 85t', 229.00, 20),
('Beats Studio3 Wireless', 349.00, 15);

-- Cámaras
INSERT INTO Productos (nombre, precio, stock) VALUES
('Canon EOS R5', 3899.00, 10),
('Sony Alpha a7 III', 1999.00, 15),
('Nikon Z6 II', 1999.00, 12),
('Fujifilm X-T4', 1699.00, 20),
('Panasonic Lumix GH5', 1399.00, 18),
('GoPro HERO10 Black', 499.00, 25);

-- Accesorios de computadora
INSERT INTO Productos (nombre, precio, stock) VALUES
('Teclado mecánico Logitech G915', 249.00, 30),
('Ratón inalámbrico Razer DeathAdder V2', 69.00, 40),
('Monitor LG UltraFine 4K', 699.00, 20),
('Webcam Logitech C920', 79.00, 35),
('Base de enfriamiento para laptop Cooler Master', 29.00, 50),
('Docking station Dell WD19', 199.00, 15);

-- Sistemas de hogar inteligente
INSERT INTO Productos (nombre, precio, stock) VALUES
('Amazon Echo Dot', 39.99, 50),
('Google Nest Hub', 99.99, 30),
('Philips Hue Starter Kit', 129.99, 25),
('Ring Video Doorbell', 199.99, 20),
('Smart Thermostat Nest Learning', 249.99, 15),
('TP-Link Kasa Smart Plug', 29.99, 40);

-- Consolas de videojuegos
INSERT INTO Productos (nombre, precio, stock) VALUES
('PlayStation 5', 499.99, 10),
('Xbox Series X', 499.99, 12),
('Nintendo Switch', 299.99, 18),
('Oculus Quest 2', 299.99, 25),
('PlayStation VR', 299.99, 20),
('Nvidia Shield TV', 199.99, 30);

-- Almacenamiento externo
INSERT INTO Productos (nombre, precio, stock) VALUES
('Disco duro externo Seagate 2TB', 79.99, 40),
('SSD portátil Samsung T5', 89.99, 30),
('Memoria USB SanDisk 128GB', 19.99, 50),
('NAS Synology DS220+', 299.99, 15),
('Tarjeta SD Kingston 256GB', 29.99, 45),
('WD My Passport 4TB', 119.99, 20);

-- Redes y conectividad
INSERT INTO Productos (nombre, precio, stock) VALUES
('Router Wi-Fi 6 ASUS RT-AX88U', 249.99, 20),
('Extensor de red TP-Link AC750', 29.99, 35),
('Adaptador de red USB TP-Link', 14.99, 40),
('Módem Netgear Nighthawk', 129.99, 25),
('Switch Ethernet TP-Link TL-SG108', 29.99, 30),
('Sistema mesh Wi-Fi Google Nest', 169.99, 15);

-- Impresoras
INSERT INTO Productos (nombre, precio, stock) VALUES
('Impresora láser HP LaserJet Pro', 149.99, 25),
('Impresora multifunción Epson EcoTank', 299.99, 20),
('Impresora fotográfica Canon SELPHY', 99.99, 30),
('Impresora portátil HP Sprocket', 79.99, 40),
('Escáner Fujitsu ScanSnap', 349.99, 15),
('Brother HL-L2350DW', 149.99, 25);

-- Componentes de PC
INSERT INTO Productos (nombre, precio, stock) VALUES
('Tarjeta gráfica Nvidia RTX 3080', 699.99, 10),
('Procesador AMD Ryzen 9 5900X', 549.99, 15),
('Placa base ASUS ROG Strix X570-E', 299.99, 18);

-- Proveedores
INSERT INTO Proveedores (nombre, contacto) VALUES
('Proveedor A', 'contacto@proveedora.com'),
('Proveedor B', 'contacto@proveedorb.com'),
('Proveedor C', 'contacto@proveedorc.com'),
('Proveedor D', 'contacto@proveedord.com'),
('Proveedor E', 'contacto@proveedore.com'),
('Proveedor F', 'contacto@proveedorf.com'),
('Proveedor G', 'contacto@proveedorg.com'),
('Proveedor H', 'contacto@proveedorh.com'),
('Proveedor I', 'contacto@proveedori.com'),
('Proveedor J', 'contacto@proveedorj.com'),
('Proveedor K', 'contacto@proveedork.com'),
('Proveedor L', 'contacto@proveedorl.com'),
('Proveedor M', 'contacto@proveedorm.com'),
('Proveedor N', 'contacto@proveedorn.com'),
('Proveedor O', 'contacto@proveedoro.com'),
('Proveedor P', 'contacto@proveedorp.com'),
('Proveedor Q', 'contacto@proveedorq.com'),
('Proveedor R', 'contacto@proveedorr.com'),
('Proveedor S', 'contacto@proveedors.com'),
('Proveedor T', 'contacto@proveedort.com'),
('Proveedor U', 'contacto@proveedoru.com'),
('Proveedor V', 'contacto@proveedorv.com'),
('Proveedor W', 'contacto@proveedorw.com'),
('Proveedor X', 'contacto@proveedorx.com'),
('Proveedor Y', 'contacto@proveedory.com'),
('Proveedor Z', 'contacto@proveedorz.com'),
('Proveedor AA', 'contacto@proveedora1.com'),
('Proveedor AB', 'contacto@proveedorb1.com'),
('Proveedor AC', 'contacto@proveedorc1.com'),
('Proveedor AD', 'contacto@proveedord1.com'),
('Proveedor AE', 'contacto@proveedore1.com'),
('Proveedor AF', 'contacto@proveedorf1.com'),
('Proveedor AG', 'contacto@proveedorg1.com'),
('Proveedor AH', 'contacto@proveedorh1.com'),
('Proveedor AI', 'contacto@proveedori1.com'),
('Proveedor AJ', 'contacto@proveedorj1.com'),
('Proveedor AK', 'contacto@proveedork1.com'),
('Proveedor AL', 'contacto@proveedorl1.com'),
('Proveedor AM', 'contacto@proveedorm1.com'),
('Proveedor AN', 'contacto@proveedorn1.com'),
('Proveedor AO', 'contacto@proveedoro1.com'),
('Proveedor AP', 'contacto@proveedorp1.com'),
('Proveedor AQ', 'contacto@proveedorq1.com'),
('Proveedor AR', 'contacto@proveedorr1.com'),
('Proveedor AS', 'contacto@proveedors1.com'),
('Proveedor AT', 'contacto@proveedort1.com'),
('Proveedor AU', 'contacto@proveedoru1.com'),
('Proveedor AV', 'contacto@proveedorv1.com'),
('Proveedor AW', 'contacto@proveedorw1.com'),
('Proveedor AX', 'contacto@proveedorx1.com'),
('Proveedor AY', 'contacto@proveedory1.com'),
('Proveedor AZ', 'contacto@proveedorz1.com'),
('Proveedor BA', 'contacto@proveedora2.com'),
('Proveedor BB', 'contacto@proveedorb2.com'),
('Proveedor BC', 'contacto@proveedorc2.com'),
('Proveedor BD', 'contacto@proveedord2.com'),
('Proveedor BE', 'contacto@proveedore2.com'),
('Proveedor BF', 'contacto@proveedorf2.com'),
('Proveedor BG', 'contacto@proveedorg2.com'),
('Proveedor BH', 'contacto@proveedorh2.com'),
('Proveedor BI', 'contacto@proveedori2.com'),
('Proveedor BJ', 'contacto@proveedorj2.com'),
('Proveedor BK', 'contacto@proveedork2.com'),
('Proveedor BL', 'contacto@proveedorl2.com'),
('Proveedor BM', 'contacto@proveedorm2.com'),
('Proveedor BN', 'contacto@proveedorn2.com'),
('Proveedor BO', 'contacto@proveedoro2.com'),
('Proveedor BP', 'contacto@proveedorp2.com'),
('Proveedor BQ', 'contacto@proveedorq2.com'),
('Proveedor BR', 'contacto@proveedorr2.com'),
('Proveedor BS', 'contacto@proveedors2.com'),
('Proveedor BT', 'contacto@proveedort2.com'),
('Proveedor BU', 'contacto@proveedoru2.com'),
('Proveedor BV', 'contacto@proveedorv2.com'),
('Proveedor BW', 'contacto@proveedorw2.com'),
('Proveedor BX', 'contacto@proveedorx2.com'),
('Proveedor BY', 'contacto@proveedory2.com'),
('Proveedor BZ', 'contacto@proveedorz2.com');
