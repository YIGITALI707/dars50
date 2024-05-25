import psycopg2
def main():
    conn= psycopg2.connect(
        dbname='fn19',
        user='postgres',
        host='localhost',
        password='soliey1998'
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows=cur.fetchall()
    print()
    print(rows)
    print()
    for row in rows:
        print(row)
    cur.close()
    conn.commit()
    conn.close()
if __name__=='__main__':