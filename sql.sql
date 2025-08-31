CREATE DATABASE IF NOT EXISTS job_prediction;
USE job_prediction;


CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS education_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    degree VARCHAR(50),
    specialization VARCHAR(50),
    cgpa FLOAT,
    certifications VARCHAR(200),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS job_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    job VARCHAR(100),
    confidence FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS admin_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(200),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- CREATE USER 'edu2job'@'localhost' IDENTIFIED BY 'passwo-- rd123';
-- GRANT ALL PRIVILEGES ON job_prediction.* TO 'edu2job'@'localhost';
-- FLUSH PRIVILEGES;  
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Iamkk0104@';
FLUSH PRIVILEGES;





SHOW DATABASES;
USE job_prediction;
SHOW TABLES;


