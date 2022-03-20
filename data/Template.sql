CREATE TABLE title (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE (name)
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE (name)
);

CREATE TABLE colour (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE (name)
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE (name)
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title INTEGER NOT NULL,
    category INTEGER NOT NULL,
    colour INTEGER NOT NULL,
    image MEDIUMBLOB,
    location INTEGER NOT NULL,
    store INTEGER NOT NULL,
    inTime INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (title) REFERENCES title(id),
    FOREIGN KEY (category) REFERENCES category(id),
    FOREIGN KEY (colour) REFERENCES colour(id),
    FOREIGN KEY (location) REFERENCES location(id)
);

INSERT INTO category (name) VALUES ("Uniform");
INSERT INTO category (name) VALUES ("PE");
INSERT INTO category (name) VALUES ("Tech");
INSERT INTO category (name) VALUES ("Winter Clothes");
INSERT INTO category (name) VALUES ("Other");

INSERT INTO colour (name) VALUES ("Black");
INSERT INTO colour (name) VALUES ("Blue");
INSERT INTO colour (name) VALUES ("Brown");
INSERT INTO colour (name) VALUES ("Cyan");
INSERT INTO colour (name) VALUES ("Green");
INSERT INTO colour (name) VALUES ("Grey");
INSERT INTO colour (name) VALUES ("Orange");
INSERT INTO colour (name) VALUES ("Pink");
INSERT INTO colour (name) VALUES ("Purple");
INSERT INTO colour (name) VALUES ("Red");
INSERT INTO colour (name) VALUES ("White");
INSERT INTO colour (name) VALUES ("Yellow");
INSERT INTO colour (name) VALUES ("Other");