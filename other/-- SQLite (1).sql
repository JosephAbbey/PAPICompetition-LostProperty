-- SQLite
DROP TABLE title;
DROP TABLE category;
DROP TABLE location;
DROP TABLE items;

CREATE TABLE title (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title INTEGER NOT NULL,
    category INTEGER NOT NULL,
    image MEDIUMBLOB,
    location INTEGER NOT NULL,
    store INTEGER NOT NULL,
    inTime INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (title) REFERENCES title(id),
    FOREIGN KEY (category) REFERENCES category(id),
    FOREIGN KEY (location) REFERENCES location(id)
);

INSERT INTO title (name) VALUES ("Tie");
INSERT INTO category (name) VALUES ("Uniform");
INSERT INTO location (name) VALUES ("C2");

INSERT INTO items (
    title,
    category,
    location,
    store
) VALUES (
    1,
    1,
    1,
    2
);