ALTER TABLE accounts ADD COLUMN student_id VARCHAR(36) UNIQUE NULL AFTER citizen_ref;
ALTER TABLE accounts ADD COLUMN centre_id INT NULL AFTER created_at;

CREATE TABLE IF NOT EXISTS subcategories (
  id int NOT NULL AUTO_INCREMENT,
  code varchar(24) NOT NULL,
  category_id int NOT NULL,
  name varchar(100) NOT NULL,
  description text,
  active tinyint(1) DEFAULT '1',
  PRIMARY KEY (id),
  UNIQUE KEY ix_subcategories_code (code),
  KEY category_id (category_id),
  CONSTRAINT subcategories_ibfk_1 FOREIGN KEY (category_id) REFERENCES categories (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE skills ADD COLUMN subcategory_id INT NULL AFTER category_name;
ALTER TABLE skills ADD COLUMN subcategory_name VARCHAR(100) NULL AFTER subcategory_id;

ALTER TABLE enrollments ADD COLUMN student_id VARCHAR(36) NULL AFTER code;
ALTER TABLE enrollments ADD COLUMN centre_id INT NULL AFTER updated_at;
ALTER TABLE enrollments ADD COLUMN rejection_reason TEXT NULL AFTER centre_id;
ALTER TABLE enrollments ADD COLUMN decision_by_admin_id INT NULL AFTER rejection_reason;
ALTER TABLE enrollments ADD COLUMN decision_timestamp DATETIME NULL AFTER decision_by_admin_id;
ALTER TABLE enrollments ADD COLUMN internal_notes TEXT NULL AFTER decision_timestamp;

ALTER TABLE training_centres ADD COLUMN latitude DOUBLE NULL AFTER active;
ALTER TABLE training_centres ADD COLUMN longitude DOUBLE NULL AFTER latitude;
ALTER TABLE training_centres ADD COLUMN approval_status VARCHAR(40) NOT NULL DEFAULT 'APPROVED' AFTER longitude;
ALTER TABLE training_centres ADD COLUMN rejection_reason TEXT NULL AFTER approval_status;
ALTER TABLE training_centres ADD COLUMN establishment_year INT NULL AFTER rejection_reason;
ALTER TABLE training_centres ADD COLUMN website VARCHAR(255) NULL AFTER establishment_year;
ALTER TABLE training_centres ADD COLUMN description TEXT NULL AFTER website;
ALTER TABLE training_centres ADD COLUMN history TEXT NULL AFTER description;
ALTER TABLE training_centres ADD COLUMN mission_objectives TEXT NULL AFTER history;
ALTER TABLE training_centres ADD COLUMN achievements TEXT NULL AFTER mission_objectives;
ALTER TABLE training_centres ADD COLUMN certifications TEXT NULL AFTER achievements;
ALTER TABLE training_centres ADD COLUMN classroom_count INT DEFAULT 5 AFTER certifications;
ALTER TABLE training_centres ADD COLUMN lab_details TEXT NULL AFTER classroom_count;
ALTER TABLE training_centres ADD COLUMN equipment_details TEXT NULL AFTER lab_details;

CREATE TABLE IF NOT EXISTS admin_centre_assignments (
  id int NOT NULL AUTO_INCREMENT,
  account_id int NOT NULL,
  centre_id int NOT NULL,
  assigned_at datetime DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_admin_centre (account_id,centre_id),
  KEY ix_admin_centre_assignments_account_id (account_id),
  KEY ix_admin_centre_assignments_centre_id (centre_id),
  CONSTRAINT admin_centre_assignments_ibfk_1 FOREIGN KEY (account_id) REFERENCES accounts (id) ON DELETE CASCADE,
  CONSTRAINT admin_centre_assignments_ibfk_2 FOREIGN KEY (centre_id) REFERENCES training_centres (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS otp_verification_sessions (
  id int NOT NULL AUTO_INCREMENT,
  reference varchar(80) NOT NULL,
  phone varchar(180) NOT NULL,
  citizen_ref varchar(80) DEFAULT NULL,
  purpose varchar(60) NOT NULL,
  provider varchar(40) DEFAULT NULL,
  provider_message_id varchar(120) DEFAULT NULL,
  hashed_code varchar(128) NOT NULL,
  attempts int DEFAULT NULL,
  max_attempts int DEFAULT NULL,
  is_verified tinyint(1) DEFAULT NULL,
  is_consumed tinyint(1) DEFAULT NULL,
  expires_at datetime NOT NULL,
  verified_at datetime DEFAULT NULL,
  created_at datetime DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY ix_otp_verification_sessions_reference (reference),
  KEY ix_otp_verification_sessions_phone (phone),
  KEY ix_otp_verification_sessions_citizen_ref (citizen_ref)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
