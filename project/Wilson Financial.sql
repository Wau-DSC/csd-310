-- Drop tables if they exist
DROP DATABASE wilson;
CREATE DATABASE wilson;
USE wilson;

-- Create Client table
CREATE TABLE Client (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(30) NOT NULL,
    managed_assets INT,
    date_registered DATETIME,
    primary_contact INT
);

-- Create Contact table
CREATE TABLE Contact (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    contact_name VARCHAR(30),
    contact_phone VARCHAR(22),
    contact_email VARCHAR(40),
    contact_address VARCHAR(60),
    contact_city VARCHAR(30),
    contact_state VARCHAR(13),
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);

-- Create Transaction table
CREATE TABLE Transaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    transaction_type ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL,
    transaction_date DATETIME,
    payment_amount INT,
    payment_status ENUM('Pending', 'Completed', 'Failed') NOT NULL,
    memo VARCHAR(100),
    contact_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(client_id),
    FOREIGN KEY (contact_id) REFERENCES Contact(contact_id)
);


ALTER TABLE Client ADD CONSTRAINT FOREIGN KEY (primary_contact) REFERENCES Contact(contact_id);
-- Insert records into Client table
INSERT INTO Client (client_name, managed_assets, date_registered) VALUES
('Jerry Lee', 1000, '2024-04-05 10:00:00'),
('Harold Johnson', 2000, '2024-03-07 11:00:00'),
('Candance Jones', 3000, '2024-03-19 12:00:00'),
('Andrew Smith', 4000, '2024-04-12 13:00:00'),
('Gabriel Rainey', 5000, '2024-07-01 14:00:00'),
('Elliott Wilson', 6000, '2024-09-02 15:00:00');

-- Insert records into Transaction table
INSERT INTO Transaction (client_id, transaction_type, transaction_date, payment_amount, payment_status, memo) VALUES
(1, 'Deposit', '2024-06-01 09:00:00', 1500, 'Completed', 'Initial deposit'),
(2, 'Withdrawal', '2024-06-05 10:00:00', 2000, 'Pending', 'Monthly withdrawal'),
(3, 'Transfer', '2024-06-07 11:00:00', 200, 'Failed', 'Transfer to savings'),
(4, 'Deposit', '2024-06-08 12:00:00', 3000, 'Completed', 'Check Deposit'),
(5, 'Withdrawal', '2024-06-09 13:00:00', 450, 'Completed', 'Car payment'),
(6, 'Transfer', '2024-06-10 14:00:00', 1000, 'Pending', 'Transfer to checking');

-- Insert records into Contact table
INSERT INTO Contact (client_id, contact_name, contact_phone, contact_email, contact_state) VALUES
(1,NULL,'324-665-5678', 'lee123@gmail.com','FL'),
(2,NULL,'435-564-9870', 'johnson@gmail345.com','UT'),
(3,NULL,'345-746-908', 'jones345@gmail.com','FL'),
(4,NULL,'890-645-3213', 'smith329@gmail.com','AK'),
(5,NULL,'890-703-4659', 'rainey@gmail.com','AK'),
(6,NULL,'927-860-2748', 'wilson342@gmail.com','CA'),
(6,'Emily Wilson','927-844-2700', 'ewilson@gmail.com','CA');

UPDATE Client JOIN Contact ON Client.client_id = Contact.client_id SET Client.primary_contact = Contact.contact_id;