-- QuickNotes Database Schema
-- Run this script to initialize the database

CREATE DATABASE IF NOT EXISTS quicknotes
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE quicknotes;

CREATE TABLE IF NOT EXISTS notes (
    id          INT UNSIGNED    NOT NULL AUTO_INCREMENT,
    title       VARCHAR(255)    NOT NULL,
    content     TEXT            NOT NULL,
    created_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
