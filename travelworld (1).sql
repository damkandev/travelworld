-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 11, 2024 at 05:03 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `travelworld`
--

-- --------------------------------------------------------

--
-- Table structure for table `destino`
--

CREATE TABLE `destino` (
  `id` int NOT NULL,
  `nombre` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `actividades` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `precio` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `destino`
--

INSERT INTO `destino` (`id`, `nombre`, `descripcion`, `actividades`, `precio`) VALUES
(1, 'Copa Cabanna', 'Un lugar de muchas playuas', 'Bañarse sucio', 21849),
(3, 'Manuel Montt', 'WUAAAAAAA', 'WUAAAAAAAA', 213848);

-- --------------------------------------------------------

--
-- Table structure for table `paquete_destino`
--

CREATE TABLE `paquete_destino` (
  `id` int NOT NULL,
  `paquete_id` int NOT NULL,
  `destino_id` int NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `precio_unico` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paquete_destino`
--

INSERT INTO `paquete_destino` (`id`, `paquete_id`, `destino_id`, `fecha_inicio`, `fecha_fin`, `precio_unico`) VALUES
(3, 3, 1, '2024-10-20', '2024-11-20', 53),
(4, 3, 3, '2024-09-20', '2024-08-20', 12);

-- --------------------------------------------------------

--
-- Table structure for table `paquete_turistico`
--

CREATE TABLE `paquete_turistico` (
  `id` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `destinos` json NOT NULL,
  `precio_total` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `paquete_turistico`
--

INSERT INTO `paquete_turistico` (`id`, `nombre`, `destinos`, `precio_total`) VALUES
(3, 'pruebon', '[{\"destino_id\": 1, \"fecha_inicio\": \"2024-10-20\", \"precio_unico\": 53, \"fecha_termino\": \"2024-11-20\", \"nombre_destino\": \"Copa Cabanna\"}, {\"destino_id\": 3, \"fecha_inicio\": \"2024-09-20\", \"precio_unico\": 12, \"fecha_termino\": \"2024-08-20\", \"nombre_destino\": \"Manuel Montt\"}]', 65);

-- --------------------------------------------------------

--
-- Table structure for table `reserva`
--

CREATE TABLE `reserva` (
  `id` int NOT NULL,
  `id_paquete` int NOT NULL,
  `username` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reserva`
--

INSERT INTO `reserva` (`id`, `id_paquete`, `username`) VALUES
(1, 3, 'damian');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `username` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `rut` int NOT NULL,
  `full_name` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`username`, `rut`, `full_name`, `password`, `is_admin`) VALUES
('damian', 219324987, 'Damian Alberto Panes Lobos', 'scrypt:32768:8:1$gS1FdVlb4kKXooTz$1580c6311a58eab02ca5e3ab0de63b0825d20feebe9d6de4ba7178b95253a2b992126b28c6e1209c1abe5785d835104663dd452bcaa6b8549661351f02b6eca8', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destino`
--
ALTER TABLE `destino`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `paquete_destino`
--
ALTER TABLE `paquete_destino`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paquete_id` (`paquete_id`),
  ADD KEY `destino_id` (`destino_id`);

--
-- Indexes for table `paquete_turistico`
--
ALTER TABLE `paquete_turistico`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paquete` (`id_paquete`,`username`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`username`(30)),
  ADD KEY `username_idx` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `destino`
--
ALTER TABLE `destino`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `paquete_destino`
--
ALTER TABLE `paquete_destino`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `paquete_turistico`
--
ALTER TABLE `paquete_turistico`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `paquete_destino`
--
ALTER TABLE `paquete_destino`
  ADD CONSTRAINT `destino_id` FOREIGN KEY (`destino_id`) REFERENCES `destino` (`id`),
  ADD CONSTRAINT `paquete_id` FOREIGN KEY (`paquete_id`) REFERENCES `paquete_turistico` (`id`);

--
-- Constraints for table `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `id_paquete` FOREIGN KEY (`id_paquete`) REFERENCES `paquete_turistico` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `usuarios` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
