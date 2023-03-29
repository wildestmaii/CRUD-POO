-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema capivarinhas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `capivarinhas` ;
USE `capivarinhas` ;

-- -----------------------------------------------------
-- Table `capivarinhas`.`capivaras`
-- -----------------------------------------------------
  CREATE TABLE IF NOT EXISTS `capivarinhas`.`capivaras` (
  `id` VARCHAR(6), 
  `nome` VARCHAR(50) NOT NULL, 
  `sexo` VARCHAR(15) NOT NULL, 
  `peso` DECIMAL(10,2),
  `cidade` VARCHAR (15)
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- 
-- -----------------------------------------------------
START TRANSACTION;
USE `capivarinhas`;
INSERT INTO `capivarinhas`.`capivaras` (`id`,`nome`,`sexo`,`peso`, `cidade`);

COMMIT;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;