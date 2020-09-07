CREATE DATABASE  IF NOT EXISTS `meteo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `meteo`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: meteo
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `fonte`
--

DROP TABLE IF EXISTS `fonte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fonte` (
  `FONTEID` varchar(45) NOT NULL,
  `Tipo fonte` varchar(45) DEFAULT NULL,
  `Statica/Dinamica` varchar(45) DEFAULT NULL,
  `pubblica/privata` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`FONTEID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `luogo`
--

DROP TABLE IF EXISTS `luogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `luogo` (
  `LUOGOID` varchar(45) NOT NULL,
  `Regione` varchar(45) DEFAULT NULL,
  `Provincia` varchar(45) DEFAULT NULL,
  `Comune` varchar(45) DEFAULT NULL,
  `Localita` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`LUOGOID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rilevazione`
--

DROP TABLE IF EXISTS `rilevazione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rilevazione` (
  `TEMPOID` varchar(45) NOT NULL,
  `LUOGOID` varchar(45) NOT NULL,
  `FONTEID` varchar(45) NOT NULL,
  `PRECIPITAZIONE` float DEFAULT NULL,
  `TEMPERATURA` float DEFAULT NULL,
  `VENTO` float DEFAULT NULL,
  `PRESSIONE` float DEFAULT NULL,
  `UMIDITA` int DEFAULT NULL,
  `RADIAZIONE` float DEFAULT NULL,
  PRIMARY KEY (`TEMPOID`,`LUOGOID`,`FONTEID`),
  KEY `LUOGOID_idx` (`LUOGOID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tempo`
--

DROP TABLE IF EXISTS `tempo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tempo` (
  `TEMPOID` varchar(8) NOT NULL,
  `Data` date DEFAULT NULL,
  `Anno` int DEFAULT NULL,
  `Mese` varchar(10) DEFAULT NULL,
  `Mese_numero` int DEFAULT NULL,
  `Giorno` int DEFAULT NULL,
  PRIMARY KEY (`TEMPOID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-03 18:46:49
