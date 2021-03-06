-- MySQL dump 10.13  Distrib 5.5.58, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: resanet
-- ------------------------------------------------------
-- Server version	5.5.58-0+deb8u1

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
-- Table structure for table `Carte`
--

DROP TABLE IF EXISTS `Carte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Carte` (
  `numeroCarte` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mdpCarte` varchar(20) NOT NULL DEFAULT 'azerty',
  `solde` float NOT NULL DEFAULT '0',
  `dateCreation` date NOT NULL,
  `activee` tinyint(1) DEFAULT '0',
  `matricule` int(10) unsigned NOT NULL,
  PRIMARY KEY (`numeroCarte`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Carte`
--

LOCK TABLES `Carte` WRITE;
/*!40000 ALTER TABLE `Carte` DISABLE KEYS */;
INSERT INTO `Carte` VALUES (1,'azerty',60.75,'2018-01-15',1,1),(2,'1977',80,'2018-01-15',1,2),(3,'1970',210,'2018-01-15',1,3),(4,'1972',130,'2018-01-15',1,4),(5,'1968',42,'2018-01-15',1,5),(6,'1994',30,'2018-03-12',1,6),(7,'1994',0,'2018-03-19',1,17);
/*!40000 ALTER TABLE `Carte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Date`
--

DROP TABLE IF EXISTS `Date`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Date` (
  `ferie` date DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Date`
--

LOCK TABLES `Date` WRITE;
/*!40000 ALTER TABLE `Date` DISABLE KEYS */;
INSERT INTO `Date` VALUES ('2018-01-01',1),('2018-04-02',2),('2018-05-01',3),('2018-05-08',4),('2018-05-10',5),('2018-05-21',6),('2018-07-14',7),('2018-08-15',8),('2018-11-01',9),('2018-11-11',10),('2018-12-25',11),('2019-01-01',12),('2019-04-22',13),('2019-05-01',14),('2019-05-08',15),('2019-05-30',16),('2019-06-10',17),('2019-07-14',18),('2019-08-15',19),('2019-11-01',20),('2019-11-11',21),('2019-12-25',22),('2020-01-01',23),('2020-04-13',24),('2020-05-01',25),('2020-05-08',26),('2020-05-21',27),('2020-06-01',28),('2020-07-14',29),('2020-08-15',30),('2020-11-01',31),('2020-11-11',32),('2020-12-25',33);
/*!40000 ALTER TABLE `Date` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fonction`
--

DROP TABLE IF EXISTS `Fonction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Fonction` (
  `idFonction` int(10) unsigned NOT NULL,
  `libelleFonction` varchar(20) NOT NULL,
  `tarifRepas` float NOT NULL,
  PRIMARY KEY (`idFonction`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fonction`
--

LOCK TABLES `Fonction` WRITE;
/*!40000 ALTER TABLE `Fonction` DISABLE KEYS */;
INSERT INTO `Fonction` VALUES (1,'Directeur',8.2),(2,'Cadre',7.3),(3,'Technicien',5.7),(4,'Secrétaire',3.5),(5,'Stagiaire',3.1);
/*!40000 ALTER TABLE `Fonction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Gestionnaire`
--

DROP TABLE IF EXISTS `Gestionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Gestionnaire` (
  `login` varchar(20) NOT NULL,
  `mdp` varchar(20) NOT NULL DEFAULT 'baobab',
  `matricule` int(10) unsigned NOT NULL,
  PRIMARY KEY (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Gestionnaire`
--

LOCK TABLES `Gestionnaire` WRITE;
/*!40000 ALTER TABLE `Gestionnaire` DISABLE KEYS */;
INSERT INTO `Gestionnaire` VALUES ('admin','azerty',5);
/*!40000 ALTER TABLE `Gestionnaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Personnel`
--

DROP TABLE IF EXISTS `Personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Personnel` (
  `matricule` int(10) unsigned NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `dateNaissance` date NOT NULL,
  `idFonction` int(10) unsigned DEFAULT NULL,
  `idService` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`matricule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Personnel`
--

LOCK TABLES `Personnel` WRITE;
/*!40000 ALTER TABLE `Personnel` DISABLE KEYS */;
INSERT INTO `Personnel` VALUES (1,'PRIGENT','Ewen','1975-12-11',1,1),(2,'HECKER','Amal','1977-02-14',2,1),(3,'CAPITAINE','Xavier','1970-04-23',2,1),(4,'THOMAS','Jean-Yves','1972-11-18',2,1),(5,'FONTAINE','Christophe','1968-09-02',5,4),(6,'AFCHAIN','Pierre','1994-12-23',3,8),(7,'AISSOU','Yaniss','1994-05-15',3,8),(8,'ALI','Adnane','1994-11-03',3,8),(9,'ALVES','Aurélien','1994-12-03',3,8),(10,'BA','Béchir','1994-12-03',3,8),(11,'BEN DAHMANE','Yassir','1994-12-08',3,3),(12,'BOURAOUI','Rahma','1994-03-15',3,3),(13,'CHAUDEY','Caroline','1994-12-21',3,3),(14,'CISTA','Walid','1994-12-03',3,3),(15,'CLERGEOT','Anthony','1994-12-09',3,3),(16,'CORY','Yohan','1993-11-13',3,3),(17,'EIBERT','Julien','1994-12-10',3,8),(18,'EL AYACHI','Meryeme','1994-12-11',3,3),(19,'FERGUENE','Juba','1994-12-03',3,3),(20,'GHAZARIAN','Thibaut','1994-12-22',3,3),(21,'GODEFROY','Yoann','1994-04-21',3,3),(22,'HONG','Vathanak','1994-05-20',3,8),(23,'HUMBERT','Cédric','1993-12-03',3,3),(24,'KABACHE','Hugo','1993-08-11',3,3),(25,'LABEL','Pierre','1994-03-03',3,3),(26,'LANDIM SEMEDO','Maxime','1994-12-03',3,3),(27,'LE GUEVEL','Vincent','1994-12-03',3,3),(28,'LEBEAU','Mike','1993-11-03',3,3),(29,'LEFAUCONNIER','José','1994-12-20',3,3),(30,'LOZAC\'H','Bastien','1987-07-17',3,3),(31,'MAGBODU','Michee','1994-12-03',3,8),(32,'MAUREL','Axel','1990-12-03',3,3),(33,'MERHRIOUI','Adam','1994-12-07',3,3),(34,'NLANDU','Christian','1994-05-03',3,3),(35,'PEQUERY','Grégory','1994-11-03',3,3),(36,'PERELLO-Y-BESTARD','Clément','1994-01-08',3,3),(37,'ROLAND','Mathieu','1990-12-03',3,3),(38,'ROSA','Baptiste','1993-12-03',3,3),(39,'TOINON','Tom','1994-12-03',3,3),(40,'TROUILLET','Mickaël','1994-11-01',2,3),(41,'BELHADJ','Taslim','1991-09-03',2,3),(42,'BELLAICHE','Mikaël','1991-12-02',2,3),(43,'HURON','Kévin','1994-12-03',2,3),(44,'JACQUIER','Nicolas','1994-02-03',2,3),(45,'POIRIER','Nicolas','1994-12-04',2,3),(46,'RAFINA','Dany','1994-07-03',2,3),(47,'ROSCO','Steve','1992-03-05',2,3),(48,'UZAN','Alexis','1989-09-07',2,3),(49,'WEBER','Guillaume','1994-08-03',2,3),(50,'WELLE','Guillaume','1994-12-20',2,3);
/*!40000 ALTER TABLE `Personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reservation`
--

DROP TABLE IF EXISTS `Reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reservation` (
  `dateResa` date NOT NULL,
  `numeroCarte` int(10) unsigned NOT NULL,
  PRIMARY KEY (`dateResa`,`numeroCarte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reservation`
--

LOCK TABLES `Reservation` WRITE;
/*!40000 ALTER TABLE `Reservation` DISABLE KEYS */;
INSERT INTO `Reservation` VALUES ('2018-03-13',1),('2018-03-14',1),('2018-03-15',1),('2018-03-16',1),('2018-03-19',1),('2018-03-22',1),('2018-03-27',1),('2018-03-28',1),('2018-03-29',1),('2018-05-02',1),('2018-05-03',1),('2018-05-04',1),('2018-05-07',1),('2018-05-09',1),('2018-05-11',1),('2018-05-14',1),('2018-05-15',1),('2018-05-16',1),('2018-05-17',1),('2018-05-18',1),('2018-05-22',1),('2018-05-24',1);
/*!40000 ALTER TABLE `Reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Service`
--

DROP TABLE IF EXISTS `Service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Service` (
  `idService` int(10) unsigned NOT NULL,
  `nomService` varchar(20) NOT NULL,
  PRIMARY KEY (`idService`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Service`
--

LOCK TABLES `Service` WRITE;
/*!40000 ALTER TABLE `Service` DISABLE KEYS */;
INSERT INTO `Service` VALUES (1,'Direction'),(2,'Commercial'),(3,'R&D'),(4,'DRH'),(5,'Comptable'),(6,'Juridique'),(7,'Accueil'),(8,'DSI'),(9,'Formation'),(10,'Communication');
/*!40000 ALTER TABLE `Service` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-14  9:08:28
