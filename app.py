from flask import Flask
app = Flask(__name__)

# #####################DB connection option using SQLAlchemy#######################
# from sqlalchemy import create_engine, text

# # Define database connection parameters
# DB_USERNAME = "postgres"
# DB_PASSWORD = "Bongo6969"
# DB_HOST = "localhost" # or your database host
# DB_PORT = "5432" # default PostgreSQL port
# DB_NAME = "myFlaskDB"


# # Create the database URL
# DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# def connect_to_database_and_fetch_emails():
#     try:  
#         engine = create_engine(DATABASE_URL)
#         with engine.connect() as connection:
#             print ("Connection is successful!")
#             message = "Connected!"
#     except Exception as e:
#         print ("Unable to connect to Database")
#         print (f"Error: {e}")
#         message = "Unable to Connect!"
    
# #####################DB connection option using SQLAlchemy#######################



################DB connection option using psycopg2########################
import psycopg2
hostname = 'localhost'
database = 'MyFlaskDB'
username = 'postgres'
pwd = 'Bongo6969'
port_id = 5432

try:
    conn = psycopg2.connect (
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
    )
    cur = conn.cursor()
    print ('PostgreSQL version is')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    db_version = str(db_version)
    print (db_version)
    
    cur.execute ('SELECT useremail FROM userslist')
    user_email = cur.fetchone()
    user_email = str(user_email)
    print (user_email)
    cur.close()
    conn.close()
    print(conn.status)

except Exception as error:
    print (error)
finally:
    cur.close()
    conn.close()
    print (conn.status)
################DB connection option using psycopg2########################

#Date Generation
from datetime import date
today = date.today()
formatted_date = today.strftime("%Y-%m-%d") 
print (formatted_date)
import time
timestamp = time.time()
formatted_timestamp = str(timestamp)
print(formatted_timestamp)
import datetime
mytime = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print (mytime)

#String manipulation using regular expression
import re
stringtime = re.split(r"\s* \s*",mytime)
timeonly = stringtime[1]
dateonly = stringtime[0]

print (dateonly)
print (timeonly)






message = "Flask - Chuwuru Project" + "\n " + formatted_date + "\n " + timeonly + "\n " + formatted_timestamp + "\n " " Connected to " + db_version + " via psycopg \n " + " Created by " + user_email

@app.route("/")
def home():
    return message 
    
