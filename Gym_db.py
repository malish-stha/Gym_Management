import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="poudel@7182"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE GYM")
print("Database Successfully Created")
conn.cursor().execute("USE GYM")
conn.cursor().execute('create table log_in(cust_name  varchar(65), account_no  int, password int)')
print("Log_in table created")
conn.cursor().execute('create table customer_table(f_name varchar(65),price int,weight int,cust_name varchar(65), phone_no bigint)')
print("Customer table created")
conn.commit()
print("DONE")

