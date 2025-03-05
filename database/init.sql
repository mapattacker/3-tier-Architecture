CREATE DATABASE IF NOT EXISTS titanic_db;
USE titanic_db;

CREATE TABLE passengers (
    survived BOOLEAN,
    familysize INT,
    fare INT,
    sex INT,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
