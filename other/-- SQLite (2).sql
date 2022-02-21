-- SQLite
DELETE FROM category;
DELETE FROM title;
DELETE FROM location;
DELETE FROM items;

INSERT INTO category (name) VALUES ("Uniform");
INSERT INTO category (name) VALUES ("PE");
INSERT INTO category (name) VALUES ("Tech");

INSERT INTO title (name) VALUES ("Boots");
INSERT INTO title (name) VALUES ("Shinpads");
INSERT INTO title (name) VALUES ("Blazer");
INSERT INTO title (name) VALUES ("Tie");
INSERT INTO title (name) VALUES ("Powerbank");

INSERT INTO location (name) VALUES ("C1");
INSERT INTO location (name) VALUES ("C2");
INSERT INTO location (name) VALUES ("C3");
INSERT INTO location (name) VALUES ("F1");
INSERT INTO location (name) VALUES ("Sports hall");