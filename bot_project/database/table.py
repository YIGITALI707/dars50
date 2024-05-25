def create_user_table(cursor,connect):
    """Create user table"""
    query = """CREATE TABLE IF NOT EXISTS users (
        id BIGSERIAL PRIMARY KEY,
        tgid BIGINT NOT NULL DEFAULT 0,
        username VARCHAR(255),
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) ,
        ad_date DATE NOT NULL DEFAULT NOW(),
        state VARCHAR(255)
        );"""
    cursor.execute(query)
    connect.commit()