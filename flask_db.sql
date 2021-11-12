-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: congac
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `congacs`
--

DROP TABLE IF EXISTS `congacs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `congacs` (
  `id_cognac` int NOT NULL AUTO_INCREMENT,
  `title_cognac` varchar(140) NOT NULL,
  `text_cognac` text,
  `date_cognac` datetime DEFAULT NULL,
  `slug_cognac` varchar(140) NOT NULL,
  `id_factory` int DEFAULT NULL,
  `seo_description_cognac` varchar(240) DEFAULT NULL,
  PRIMARY KEY (`id_cognac`),
  UNIQUE KEY `slug_cognac` (`slug_cognac`),
  KEY `id_factory` (`id_factory`),
  CONSTRAINT `congacs_ibfk_1` FOREIGN KEY (`id_factory`) REFERENCES `factories` (`id_factory`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `congacs`
--

LOCK TABLES `congacs` WRITE;
/*!40000 ALTER TABLE `congacs` DISABLE KEYS */;
/*!40000 ALTER TABLE `congacs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countrys`
--

DROP TABLE IF EXISTS `countrys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countrys` (
  `id_country` int NOT NULL AUTO_INCREMENT,
  `title_country` varchar(140) NOT NULL,
  `text_country` text,
  `seo_description_country` varchar(240) DEFAULT NULL,
  `slug_country` varchar(140) NOT NULL,
  PRIMARY KEY (`id_country`),
  UNIQUE KEY `slug_country` (`slug_country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countrys`
--

LOCK TABLES `countrys` WRITE;
/*!40000 ALTER TABLE `countrys` DISABLE KEYS */;
/*!40000 ALTER TABLE `countrys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factories`
--

DROP TABLE IF EXISTS `factories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factories` (
  `id_factory` int NOT NULL AUTO_INCREMENT,
  `title_factory` varchar(140) NOT NULL,
  `text_factory` text,
  `site_factory` varchar(140) DEFAULT NULL,
  `date_factory` datetime DEFAULT NULL,
  `slug_factory` varchar(140) NOT NULL,
  `seo_description_factory` varchar(240) DEFAULT NULL,
  `id_country` int DEFAULT NULL,
  PRIMARY KEY (`id_factory`),
  UNIQUE KEY `slug_factory` (`slug_factory`),
  KEY `id_country` (`id_country`),
  CONSTRAINT `factories_ibfk_1` FOREIGN KEY (`id_country`) REFERENCES `countrys` (`id_country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factories`
--

LOCK TABLES `factories` WRITE;
/*!40000 ALTER TABLE `factories` DISABLE KEYS */;
/*!40000 ALTER TABLE `factories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(140) NOT NULL,
  `user_mail` varchar(140) NOT NULL,
  `user_psw` varchar(140) NOT NULL,
  `user_date` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Nikolay','admin@admin.by','pbkdf2:sha256:150000$HmWN7SaZ$10a062c98af9a1fa379981e13a3ca9244cd39b7279362c3c04f6907c2784b490','2021-08-05 16:42:53'),(2,'Pavel','as@as.by','pbkdf2:sha256:150000$oO9HArEa$4728fe1a811e4ebe37fd50e9f163ce5949a4c3d00fb02b61f5a00f71b89f01d0','2021-09-28 15:25:48');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-28 16:43:54
