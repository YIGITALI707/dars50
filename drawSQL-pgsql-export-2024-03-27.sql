CREATE TABLE "userPermission"(
    "id" INTEGER NOT NULL,
    "userId" INTEGER NOT NULL,
    "permissionId" INTEGER NOT NULL
);
ALTER TABLE
    "userPermission" ADD PRIMARY KEY("id");
CREATE TABLE "normalUsers"(
    "id" INTEGER NOT NULL,
    "userId" INTEGER NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "normalUsers" ADD PRIMARY KEY("id");
CREATE TABLE "users"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL DEFAULT '512',
    "sessionkey" VARCHAR(255) NOT NULL,
    "sessionkeytimestamp" INTEGER NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
CREATE TABLE "facebookUsers"(
    "id" INTEGER NOT NULL,
    "userId" INTEGER NOT NULL,
    "facebookId" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "facebookUsers" ADD PRIMARY KEY("id");
CREATE TABLE "permissions"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "permissions" ADD PRIMARY KEY("id");
ALTER TABLE
    "userPermission" ADD CONSTRAINT "userpermission_userid_foreign" FOREIGN KEY("userId") REFERENCES "permissions"("name");
ALTER TABLE
    "users" ADD CONSTRAINT "users_name_foreign" FOREIGN KEY("name") REFERENCES "facebookUsers"("userId");
ALTER TABLE
    "users" ADD CONSTRAINT "users_sessionkeytimestamp_foreign" FOREIGN KEY("sessionkeytimestamp") REFERENCES "normalUsers"("userId");