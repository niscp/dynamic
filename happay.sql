-- MySQL dump 10.13  Distrib 5.6.27, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: happay_data
-- ------------------------------------------------------
-- Server version	5.6.27-0ubuntu0.14.04.1

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
-- Table structure for table `next_question`
--

DROP TABLE IF EXISTS `next_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `next_question` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `option_one` int(11) DEFAULT NULL,
  `option_two` int(11) DEFAULT NULL,
  `option_three` int(11) DEFAULT NULL,
  `option_four` int(11) DEFAULT NULL,
  `soft_delete` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `next_question`
--

LOCK TABLES `next_question` WRITE;
/*!40000 ALTER TABLE `next_question` DISABLE KEYS */;
INSERT INTO `next_question` VALUES (3,1,2,3,4,5,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(4,2,3,6,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(5,3,4,0,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(6,4,5,0,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(7,5,6,7,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(8,6,0,0,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01'),(9,7,0,0,0,0,0,'2016-05-10 15:30:01','2016-05-10 15:30:01');
/*!40000 ALTER TABLE `next_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_value`
--

DROP TABLE IF EXISTS `question_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question_value` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `question` text,
  `option_one` varchar(255) DEFAULT NULL,
  `option_two` varchar(255) DEFAULT NULL,
  `option_three` varchar(255) DEFAULT NULL,
  `option_four` varchar(255) DEFAULT NULL,
  `soft_delete` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_value`
--

LOCK TABLES `question_value` WRITE;
/*!40000 ALTER TABLE `question_value` DISABLE KEYS */;
INSERT INTO `question_value` VALUES (1,'What is your Name?','Nishank','Sachin','Amit','Ramesh',0,'2016-05-10 03:53:39','2016-05-10 03:53:39'),(2,'What do you do?','Doctor','Lawyer','Engineer','student',0,'2016-05-10 14:16:40','2016-05-10 14:16:40'),(3,'what is your strength','no idea','quick learning','tech enabled','restless',0,'2016-05-10 15:21:51','2016-05-10 15:21:51'),(4,'what is your fav programming language','php','python','c','java',0,'2016-05-10 15:22:07','2016-05-10 15:22:07'),(5,'what is area of expertise','computer networks','database','algo','operating system',0,'2016-05-10 15:22:08','2016-05-10 15:22:08'),(6,'what do you hate?','no idea','algo','ds','networks',0,'2016-05-10 15:22:08','2016-05-10 15:22:08'),(7,'what is your first programming language','no idea','php','c','python',0,'2016-05-10 15:22:10','2016-05-10 15:22:10'),(11,'hi','a','b','c','d',0,'2016-05-10 16:26:57','2016-05-10 16:26:57'),(12,'hihi','a','b','c','d',0,'2016-05-11 00:55:33','2016-05-11 00:55:33'),(17,'zzz','a','b','c','d',0,'2016-05-11 01:13:34','2016-05-11 01:13:34'),(18,'my new question','check me','sure','do it','hi',0,'2016-05-11 01:15:46','2016-05-11 01:15:46'),(19,'\'hi nishank\'','\'yes\'','\'tell me\'','\'say\'','\'j\'',0,'2016-05-11 01:31:18','2016-05-11 01:31:18');
/*!40000 ALTER TABLE `question_value` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-11 11:12:24
