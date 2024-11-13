-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 25-05-2024 a las 06:31:50
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `RopaUrbana`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Productos`
--

CREATE TABLE `Productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Productos`
--

INSERT INTO `Productos` (`id`, `nombre`, `precio`, `stock`) VALUES
(1, 'Camiseta Blanca', 19.99, 95),
(2, 'Pantalón Vaquero', 49.99, 75),
(3, 'Vestido Rojo', 39.99, 50),
(4, 'Chaqueta de Cuero', 99.99, 30),
(5, 'Sudadera con Capucha', 29.99, 60),
(6, 'Camiseta Negra', 19.99, 110),
(7, 'Pantalón de Chándal', 29.99, 80),
(8, 'Falda Vaquera', 34.99, 45),
(9, 'Abrigo de Lana', 149.99, 20),
(10, 'Camisa de Algodón', 24.99, 90),
(11, 'Camiseta de Tirantes', 14.99, 120),
(12, 'Pantalón Corto', 24.99, 70),
(13, 'Jersey de Punto', 39.99, 40),
(14, 'Vestido Floral', 44.99, 55),
(15, 'Blazer Negro', 79.99, 25),
(16, 'Chaleco', 29.99, 85),
(17, 'Bufanda de Lana', 19.99, 150),
(18, 'Guantes de Cuero', 24.99, 110),
(19, 'Sombrero de Paja', 15.99, 130),
(20, 'Zapatos Deportivos', 59.99, 50),
(21, 'Botas de Montaña', 89.99, 40),
(22, 'Sandalias', 29.99, 70),
(23, 'Zapatos de Vestir', 69.99, 30),
(24, 'Camiseta Gris', 19.99, 100),
(25, 'Pantalón Cargo', 34.99, 75),
(26, 'Blusa Blanca', 24.99, 65),
(27, 'Chaqueta Vaquera', 49.99, 50),
(28, 'Camiseta de Manga Larga', 24.99, 80),
(29, 'Pantalón de Vestir', 39.99, 45),
(30, 'Abrigo Impermeable', 89.99, 20),
(31, 'Falda Plisada', 29.99, 60),
(32, 'Jersey de Lana', 49.99, 35),
(33, 'Chaleco de Plumas', 59.99, 25),
(34, 'Pañuelo de Seda', 19.99, 140),
(35, 'Calcetines', 9.99, 200),
(36, 'Cinturón de Cuero', 24.99, 110),
(37, 'Gorra', 14.99, 130),
(38, 'Zapatos de Tacón', 79.99, 40),
(39, 'Mocasines', 49.99, 60),
(40, 'Botines', 89.99, 35),
(41, 'Bañador', 24.99, 70),
(42, 'Bikini', 29.99, 65),
(43, 'Mono', 44.99, 50),
(44, 'Chaqueta de Punto', 39.99, 40),
(45, 'Pantalón de Algodón', 34.99, 90),
(46, 'Camiseta Rayada', 19.99, 110),
(47, 'Falda de Cuero', 49.99, 30),
(48, 'Suéter', 39.99, 80),
(49, 'Camiseta Deportiva', 29.99, 120);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Proveedores`
--

CREATE TABLE `Proveedores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `contacto` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Proveedores`
--

INSERT INTO `Proveedores` (`id`, `nombre`, `contacto`) VALUES
(1, 'Nike', 'contacto@nike.com'),
(2, 'Adidas', 'contacto@adidas.com'),
(3, 'Puma', 'contacto@puma.com'),
(4, 'Under Armour', 'contacto@underarmour.com'),
(5, 'Reebok', 'contacto@reebok.com'),
(6, 'New Balance', 'contacto@newbalance.com'),
(7, 'ASICS', 'contacto@asics.com'),
(8, 'Columbia', 'contacto@columbia.com'),
(9, 'The North Face', 'contacto@thenorthface.com'),
(10, 'Patagonia', 'contacto@patagonia.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Ventas`
--

CREATE TABLE `Ventas` (
  `id` int(11) NOT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `fecha_venta` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Productos`
--
ALTER TABLE `Productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Proveedores`
--
ALTER TABLE `Proveedores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Ventas`
--
ALTER TABLE `Ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_id` (`producto_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Productos`
--
ALTER TABLE `Productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de la tabla `Proveedores`
--
ALTER TABLE `Proveedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `Ventas`
--
ALTER TABLE `Ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Ventas`
--
ALTER TABLE `Ventas`
  ADD CONSTRAINT `Ventas_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `Productos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
