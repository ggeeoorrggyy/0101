CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    post INTEGER NOT NULL,
    FOREIGN KEY (post) REFERENCES post(id));

CREATE TABLE cafe(
    id INTEGER NOT NULL PRIMARY KEY,
    city VARCHAR (25)  NOT NULL,
    number INTEGER NOT NULL,
    name VARCHAR (15)  NOT NULL,
    address VARCHAR (35)  NOT NULL,
    menu_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    FOREIGN KEY (menu_id)
        REFERENCES menu(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (staff_id)
        REFERENCES Staff(id)
        ON DELETE SET NULL ON UPDATE NO ACTION );


CREATE TABLE staff(
    id integer not null primary key unique,
    name VARCHAR(15) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    patronymic VARCHAR(30) NOT NULL,
    datee INTEGER NOT NULL,
    cafe VARCHAR(20) NOT NULL,
    post_id VARCHAR(20) NOT NULL,
    FOREIGN KEY (post_id)
        REFERENCES post(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
);

CREATE TABLE menu(
    id INTEGER NOT NULL PRIMARY KEY,
    price INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    ingredient VARCHAR(30),
    availability VARCHAR(30),
    name_of_the_dish_ID INTEGER NOT NULL,
    FOREIGN KEY (name_of_the_dish_ID)
        REFERENCES name_of_the_dish(id)
);

CREATE TABLE name_of_the_dish(
    id INTEGER NOT NULL PRIMARY KEY,
    Dish VARCHAR(150)
);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name_post VARCHAR(150) NOT NULL);

INSERT INTO users(id, login, password, post)
VALUES (1, 'admin', 'admin', 1);

INSERT INTO cafe(city, number, name, address)
VALUES ('city', 'number', 'name', 'address'),('city1', 'number1', 'name1', 'address1');

INSERT INTO staff(name, surname, patronymic, datee, cafe, Post_id)
VALUES ('name','surname','patronymic','datee','cafe', 'post_id'),('name1','surname1','patronymic1','datee1' ,'cafe1', 'post_id1');

INSERT INTO menu(price, weight, ingredient, availability)
VALUES ('price','weight','ingredient','availability'),('price1','weight1','ingredient1','availability1');

INSERT INTO name_of_the_dish(Dish)
VALUES ('Dish'),('Dish1');

INSERT INTO post(name_post)
VALUES ('name_post'),('name_post1');
