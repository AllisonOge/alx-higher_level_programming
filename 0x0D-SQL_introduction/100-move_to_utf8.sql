-- a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf9mb4_unicode_ci)
-- the following should be converted to utf8
-- database hbtn_0c_0, table first_table and field name in first_table
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
