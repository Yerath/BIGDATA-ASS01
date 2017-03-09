-- MySQL Script generated by MySQL Workbench
-- Thu Mar  9 17:21:18 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema snowflake
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema snowflake
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `snowflake` DEFAULT CHARACTER SET utf8 ;
USE `snowflake` ;

-- -----------------------------------------------------
-- Table `snowflake`.`Phenomenon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Phenomenon` (
  `idPhenomenon` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idPhenomenon`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snowflake`.`Phenomenon_Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Phenomenon_Type` (
  `idPhenomenon_Type` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idPhenomenon_Type`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snowflake`.`Observation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Observation` (
  `idObservation` INT NOT NULL AUTO_INCREMENT,
  `Phenomenon_idPhenomenon` INT NOT NULL,
  `Phenomenon_Type_idPhenomenon_Type` INT NOT NULL,
  PRIMARY KEY (`idObservation`),
  INDEX `fk_Observation_Phenomenon1_idx` (`Phenomenon_idPhenomenon` ASC),
  INDEX `fk_Observation_Phenomenon_Type1_idx` (`Phenomenon_Type_idPhenomenon_Type` ASC),
  CONSTRAINT `fk_Observation_Phenomenon1`
    FOREIGN KEY (`Phenomenon_idPhenomenon`)
    REFERENCES `snowflake`.`Phenomenon` (`idPhenomenon`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Observation_Phenomenon_Type1`
    FOREIGN KEY (`Phenomenon_Type_idPhenomenon_Type`)
    REFERENCES `snowflake`.`Phenomenon_Type` (`idPhenomenon_Type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snowflake`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Person` (
  `idPerson` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `gender` INT NULL COMMENT '	',
  `birthdate` VARCHAR(45) NULL,
  `studentnr` INT NULL,
  PRIMARY KEY (`idPerson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snowflake`.`Unit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Unit` (
  `idUnit` INT NOT NULL AUTO_INCREMENT,
  `value` VARCHAR(45) NULL,
  `unit` VARCHAR(45) NULL,
  PRIMARY KEY (`idUnit`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snowflake`.`Measurements_Facts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snowflake`.`Measurements_Facts` (
  `idMeasurements_Facts` INT NOT NULL AUTO_INCREMENT,
  `Observation_idObservation` INT NOT NULL,
  `Person_idPerson` INT NOT NULL,
  `Unit_idUnit` INT NOT NULL,
  `timestamp` VARCHAR(45) NULL,
  PRIMARY KEY (`idMeasurements_Facts`),
  INDEX `fk_Measurements_Facts_Observation1_idx` (`Observation_idObservation` ASC),
  INDEX `fk_Measurements_Facts_Person1_idx` (`Person_idPerson` ASC),
  INDEX `fk_Measurements_Facts_Unit1_idx` (`Unit_idUnit` ASC),
  CONSTRAINT `fk_Measurements_Facts_Observation1`
    FOREIGN KEY (`Observation_idObservation`)
    REFERENCES `snowflake`.`Observation` (`idObservation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Measurements_Facts_Person1`
    FOREIGN KEY (`Person_idPerson`)
    REFERENCES `snowflake`.`Person` (`idPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Measurements_Facts_Unit1`
    FOREIGN KEY (`Unit_idUnit`)
    REFERENCES `snowflake`.`Unit` (`idUnit`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;