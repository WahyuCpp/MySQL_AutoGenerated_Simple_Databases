CREATE DATABASE IF NOT EXISTS generate_data_db;
USE generate_data_db;

CREATE TABLE IF NOT EXISTS generated_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    value FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);