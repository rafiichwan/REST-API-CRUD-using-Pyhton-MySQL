CREATE DATABASE basic_coding_kulina;

USE basic_coding_kulina;

CREATE TABLE IF NOT EXISTS user_review (
	id INT AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    user_id INT,
    rating FLOAT,
    review VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

select * from user_review;
