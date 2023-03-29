-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema capivarinhas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema capivarinhas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `capivarinhas` ;
USE `capivarinhas` ;


-- -----------------------------------------------------
-- Table `capivarinhas`.`Professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `capivarinhas`.`capivaras` (
  `id` CHAR(11) NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `nascimento` DATE NOT NULL,
  `peso` VARCHAR(11) NULL,
  `cidade` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Data for table `SGA`.`Periodo`
-- -----------------------------------------------------
START TRANSACTION;
USE `capivarinhas`;
INSERT INTO `capivarinhas`.`capivaras` (`id`,`nome`,`nascimento`,`peso`, `cidade`);

COMMIT;

