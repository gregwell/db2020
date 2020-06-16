-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2020 at 10:05 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trustnet`
--

-- --------------------------------------------------------

--
-- Table structure for table `firma`
--

CREATE TABLE `firma` (
  `id_firma` int(11) NOT NULL,
  `nazwa` text COLLATE utf8_polish_ci NOT NULL,
  `branza` text COLLATE utf8_polish_ci NOT NULL,
  `miasto` text COLLATE utf8_polish_ci NOT NULL,
  `liczba_opinii` int(11) NOT NULL,
  `srednia` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `firma`
--

INSERT INTO `firma` (`id_firma`, `nazwa`, `branza`, `miasto`, `liczba_opinii`, `srednia`) VALUES
(1, 'jan grzegorz trzeci glowice', 'janice pawlice', 'janów lubelski', 0, 0),
(2, 'Janek Podolski uslugi', 'Fryzjer', 'Krakow', 0, 0),
(4, 'Hej sokoly firma handlowa', 'Gastronomia', 'Krakow', 0, 0),
(5, 'Fryzjerstwo u mnie i Spolki', 'Fryzjer', 'Krakow', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `opinie`
--

CREATE TABLE `opinie` (
  `id_opinia` int(11) NOT NULL,
  `liczba_gwiazdek` int(11) NOT NULL,
  `opis` text COLLATE utf8_polish_ci NOT NULL,
  `FirmaID` int(11) NOT NULL,
  `UzytkownikID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `opinie`
--

INSERT INTO `opinie` (`id_opinia`, `liczba_gwiazdek`, `opis`, `FirmaID`, `UzytkownikID`) VALUES
(1, 3, 'dsd', 2, 1),
(2, 5, 'Kuku', 4, 1),
(3, 2, 'spoko firma', 4, 1),
(4, 2, 'spoko firma ale moja curka studiuje prawo', 5, 1),
(5, 1, 'fajnie i spoko', 5, 1),
(6, 3, 'fajna firma i wogule', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `uzytkownik`
--

CREATE TABLE `uzytkownik` (
  `id_uzytkownik` int(11) NOT NULL,
  `imie` text COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `uzytkownik`
--

INSERT INTO `uzytkownik` (`id_uzytkownik`, `imie`, `nazwisko`) VALUES
(1, 'greg', 'well'),
(2, 'lala', 'jaha'),
(3, 'jan', 'kowalski'),
(4, 'jan', 'kowalski'),
(5, 'jan', 'kowalski'),
(6, 'jan', 'kowalski'),
(7, 'grzegorz', 'studzinowski'),
(8, 'jan', 'kowalski'),
(9, 'grzegorz', 'studzinowski'),
(10, 'grzegorz', 'studzinowski'),
(11, 'Grzegurzek', 'Studzionek'),
(12, 'Grzegurzek', 'Stawarowski'),
(13, 'Janek', 'Jankowski'),
(14, 'hhh', 'jjj'),
(15, 'Grzegurzulec', 'Grzegurzowski'),
(16, 'jan', 'kowalski'),
(17, 'jan', 'janowski'),
(18, 'janek', 'jankoiczowicz'),
(19, '2', '1'),
(20, 'janowicz', 'janowiczowsky'),
(21, 'jan', 'nowak');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `firma`
--
ALTER TABLE `firma`
  ADD PRIMARY KEY (`id_firma`);

--
-- Indexes for table `opinie`
--
ALTER TABLE `opinie`
  ADD PRIMARY KEY (`id_opinia`);

--
-- Indexes for table `uzytkownik`
--
ALTER TABLE `uzytkownik`
  ADD PRIMARY KEY (`id_uzytkownik`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `firma`
--
ALTER TABLE `firma`
  MODIFY `id_firma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `opinie`
--
ALTER TABLE `opinie`
  MODIFY `id_opinia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `uzytkownik`
--
ALTER TABLE `uzytkownik`
  MODIFY `id_uzytkownik` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
