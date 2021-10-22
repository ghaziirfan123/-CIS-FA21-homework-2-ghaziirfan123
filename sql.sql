USE `homework2`; 



DROP TABLE IF EXISTS `homework2`.`car`;
DROP TABLE IF EXISTS `homework2`.`mechanic`;
DROP TABLE IF EXISTS `homework2`.`logs`;

CREATE TABLE `homework2`.`car` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `vin` VARCHAR(64) NULL,
  `make` VARCHAR(64) NULL,
  `model` VARCHAR(64) NULL,
  `year` INT NULL,
  `color` VARCHAR(64) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `homework2`.`mechanic` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(64) NULL,
  `lastname` VARCHAR(64) NULL,
  `title` VARCHAR(64) NULL,
  `currentcar` INT DEFAULT NULL,
  FOREIGN KEY (currentcar) REFERENCES car(id),
  PRIMARY KEY (`id`));
  
CREATE TABLE `homework2`.`logs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL,
  `name` VARCHAR(64) NULL,
  `message` VARCHAR(128) NULL,
  PRIMARY KEY (`id`));



INSERT INTO `homework2`.`car` ( `vin`, `make`, `model`, `year`,  `color`) 
VALUES ( '1532652462', 'honda', 'accord', 2020, 'black');
INSERT INTO `homework2`.`car` ( `vin`, `make`, `model`, `year`,  `color`) 
VALUES ( '3463646364', 'honda', 'city', 2021, 'grey');
INSERT INTO `homework2`.`car` ( `vin`, `make`, `model`, `year`,  `color`) 
VALUES ( '5736347366', 'bmw', 'v8', 2019, 'white');
INSERT INTO `homework2`.`car` ( `vin`, `make`, `model`, `year`,  `color`) 
VALUES ( '7573634638', 'toyota', 'corolla', 2019, 'white');
INSERT INTO `homework2`.`car` ( `vin`, `make`, `model`, `year`,  `color`) 
VALUES ( '9634636360', 'audi', 'a7', 2015, 'blue');

INSERT INTO `homework2`.`mechanic` ( `firstname`, `lastname`, `title`, `currentcar`) 
VALUES ( 'john', 'doe', 'head', 1);
INSERT INTO `homework2`.`mechanic` ( `firstname`, `lastname`, `title`, `currentcar`) 
VALUES ( 'mark', 'dale', 'worker', 2);
INSERT INTO `homework2`.`mechanic` ( `firstname`, `lastname`, `title`, `currentcar`) 
VALUES ( 'henry', 'phillips', 'worker', 3);
INSERT INTO `homework2`.`mechanic` ( `firstname`, `lastname`, `title`, `currentcar`) 
VALUES ( 'randy', 'orton', 'worker', 1);
INSERT INTO `homework2`.`mechanic` ( `firstname`, `lastname`, `title`) 
VALUES ( 'bill', 'gates', 'worker');




SELECT * FROM `car`;
SELECT * FROM `mechanic`;
SELECT * FROM `logs`;

