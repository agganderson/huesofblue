CREATE DATABASE  IF NOT EXISTS `huesofblue` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `huesofblue`;
-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: huesofblue
-- ------------------------------------------------------
-- Server version	5.5.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `concerns`
--

DROP TABLE IF EXISTS `concerns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concerns` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anxiety` varchar(45) DEFAULT NULL,
  `depression` varchar(45) DEFAULT NULL,
  `stress` varchar(45) DEFAULT NULL,
  `substance_abuse` varchar(45) DEFAULT NULL,
  `eating_disorders` varchar(45) DEFAULT NULL,
  `relationships` varchar(45) DEFAULT NULL,
  `grief` varchar(45) DEFAULT NULL,
  `other` varchar(45) DEFAULT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_concerns_users1_idx` (`users_id`),
  CONSTRAINT `fk_concerns_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concerns`
--

LOCK TABLES `concerns` WRITE;
/*!40000 ALTER TABLE `concerns` DISABLE KEYS */;
INSERT INTO `concerns` VALUES (3,'1','1','0','1','0','0','1','0',83),(4,'1','0','1','0','0','0','0','1',84),(5,'0','1','1','0','0','1','1','1',85),(6,'1','1','1','1','1','1','1','1',86),(7,'1','1','1','1','1','1','1','1',87),(8,'1','0','1','1','0','0','0','0',88);
/*!40000 ALTER TABLE `concerns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connections`
--

DROP TABLE IF EXISTS `connections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `connections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `users_id` int(11) NOT NULL,
  `users_id1` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_users_has_users_users2_idx` (`users_id1`),
  KEY `fk_users_has_users_users1_idx` (`users_id`),
  CONSTRAINT `fk_users_has_users_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2` FOREIGN KEY (`users_id1`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connections`
--

LOCK TABLES `connections` WRITE;
/*!40000 ALTER TABLE `connections` DISABLE KEYS */;
/*!40000 ALTER TABLE `connections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keys`
--

DROP TABLE IF EXISTS `keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keys`
--

LOCK TABLES `keys` WRITE;
/*!40000 ALTER TABLE `keys` DISABLE KEYS */;
/*!40000 ALTER TABLE `keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `form_q1` varchar(255) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `zip_code` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `bio` varchar(45) DEFAULT NULL,
  `user_level` varchar(45) DEFAULT NULL,
  `mentor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (83,'I have issues.','Andrew','Wibel','95037','a@gmail.com','awibel','$2b$12$udPJwhkWT2TGkhhJNCnzk.nZh3/9pVGh.D2DeJqkuLd8p43ZGP/bm','2016-01-28 15:16:37','2016-01-28 15:16:37','Stuff and what nots.','nonadmin','Yes'),(84,'Stuff and things','Mari','Mari','12345','mari@gmail.com','mari','$2b$12$aWaDuQNtpVJxMmOpxVJEguKK9/JXq8nEaXJBIZPJqM0A1X2h7o2lW','2016-01-28 15:33:11','2016-01-28 15:33:11','Crazy','nonadmin','Yes'),(85,'Stuff and things','Ali','Anderson','54321','ali@gmail.com','ali','$2b$12$ZWsTEbkyYkV7HMNXh13ZluIqrl8LObu9uP0Ruxh7Z2ucAzAoBtnni','2016-01-28 15:35:05','2016-01-28 15:35:05','Whoaaaaaa','nonadmin','Yes'),(86,'I like issues!','Sonya','Panish','54321','s@gmail.com','sonya','$2b$12$d6RSa8jOtIBQCz5gC6ycr.JMhDIkV5REkJkL479xA.76MgNjCHm3y','2016-01-28 15:36:31','2016-01-28 15:36:31','stuffffffffffff','nonadmin','Yes'),(87,'so many issues...','Jim','Bob','12345','jimbob@gmail.com','jimbob','$2b$12$qgHLHjpLl9.pVOycyB495u8a2nPRBA6R.E1.sd.51TGigVQoGhMfu','2016-01-28 15:37:44','2016-01-28 15:37:44','ooogabooga','nonadmin','No'),(88,'im nuts','Jane','Bob','95037','janebob@gmail.com','janebob','$2b$12$vh1zAP5FJuhEuGm7CLDh9ehydshKuJj68gUoFWg4juHWt5herXDMu','2016-01-28 15:39:18','2016-01-28 15:39:18','i need help.','nonadmin','No');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'huesofblue'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-28 18:55:01
