
CREATE TABLE account (  
>id INTEGER NOT NULL,  
>name VARCHAR(144) NOT NULL,  
>username VARCHAR(144) NOT NULL,  
>password VARCHAR(144) NOT NULL,  
>PRIMARY KEY (id)
);

CREATE TABLE "group" (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE task (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        done BOOLEAN NOT NULL,
        account_id INTEGER NOT NULL,
        group_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(group_id) REFERENCES "group" (id)
);
