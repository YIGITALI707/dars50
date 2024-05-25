create table users(
    id INT,
    name VARCHAR(512),
    sessionKey VARCHAR(1024),
    sessionKeyTimestamp INT,
    email VARCHAR(512)
);

create table userPermissions(
    id INT,
    userId INT,
    permissionId INT
);

create table facebookUsers(
    id INT,
    userId INT,
    facebookUserId INT
);

create table normalUsers(
    id INT,
    userId INT,
    username VARCHAR(512),
    password VARCHAR(1024)
);

create table normalUsers(
    id INT,
    name VARCHAR(512),
    description VARCHAR(1024)
);
