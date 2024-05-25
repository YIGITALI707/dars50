import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

HOST=os.environ.get("HOST")
PORT=os.environ.get("PORT")
USER=os.environ.get("USER")
PASSWORD=os.environ.get("PASSWORD")
DBNAME=os.environ.get("DBNAME")

connect=psycopg2.connect(
    dbname=DBNAME,
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD
)
