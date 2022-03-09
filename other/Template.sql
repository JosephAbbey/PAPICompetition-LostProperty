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

INSERT INTO colour (name) VALUES ("Black");
INSERT INTO colour (name) VALUES ("White");
INSERT INTO colour (name) VALUES ("Green");
INSERT INTO colour (name) VALUES ("Purple");

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