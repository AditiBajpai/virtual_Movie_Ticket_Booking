/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`moviedb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `moviedb`;

/*Table structure for table `userticket` */

DROP TABLE IF EXISTS `userticket`;

CREATE TABLE `userticket`(
  `name` VARCHAR(20) NOT NULL,
  `gender` VARCHAR(20) NOT NULL,
  `age` INT(2) NOT NULL,
  `ticketprice` VARCHAR(20) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `ticketnumber` VARCHAR(20) PRIMARY KEY
)
