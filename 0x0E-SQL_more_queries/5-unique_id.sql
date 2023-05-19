-- create table with unique id with default value
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
