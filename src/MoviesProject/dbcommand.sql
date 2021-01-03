
CREATE DATABASE `moviedb`;

USE `moviedb`;

/*Table structure for table `userticket` */

DROP TABLE IF EXISTS `userticket`;

CREATE TABLE `userticket`(
  `name` VARCHAR(20) NOT NULL,
  `gender` VARCHAR(20) NOT NULL,
  `age` INT(2) NOT NULL,
  `ticketprice` INT(20) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `ticketnumber` VARCHAR(20) PRIMARY KEY
)
