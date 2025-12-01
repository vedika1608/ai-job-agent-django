CREATE TABLE Job (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  company VARCHAR(200),
  skills VARCHAR(300),
  description TEXT
);

CREATE TABLE auth_user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(150),
  email VARCHAR(254),
  password VARCHAR(128)
);

CREATE TABLE core_application (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  job_id INT,
  status VARCHAR(50),
  applied_at DATETIME
);
